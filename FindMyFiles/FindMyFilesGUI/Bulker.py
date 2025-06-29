import sys
import os
import shutil
from pathlib import Path
from datetime import datetime
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QVBoxLayout,
                             QHBoxLayout, QFileDialog, QRadioButton, QButtonGroup,
                             QMessageBox, QTextEdit, QComboBox)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon




def resource_path(relative_path):
    """ Get absolute path to resource - works in dev and PyInstaller """
    try:
        # PyInstaller stores data in a temp folder using _MEIPASS
        base_path = Path(sys._MEIPASS)
    except AttributeError:
        base_path = Path(__file__).resolve().parent

    return base_path / relative_path

logo_path = resource_path("logo.png")

class FileFinder(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bulker - Copy | Move Same File Type")
        self.setWindowIcon(QIcon(str(logo_path)))
        self.resize(900, 640)
        self.setMinimumSize(800, 600)

        self.initUI()

    def initUI(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #ffffff;
                font-family: 'Segoe UI', sans-serif;
            }
            QPushButton {
                background-color: #2f855a;
                border-radius: 6px;
                padding: 10px 16px;
                font-size: 14px;
                color: white;
                font-weight: 500;
            }
            QPushButton:hover {
                background-color: #276749;
            }
            QLabel {
                font-size: 15px;
                font-weight: 500;
                color: #1a202c;
            }
            QTextEdit {
                background-color: #f7fafc;
                border: 1px solid #e2e8f0;
                border-radius: 6px;
                padding: 10px;
                font-size: 13px;
                color: #2d3748;
            }
            QRadioButton {
                font-size: 13px;
                color: #2d3748;
            }
            QComboBox {
                background-color: #edf2f7;
                border-radius: 6px;
                padding: 6px;
                font-size: 13px;
            }
        """)

        layout = QVBoxLayout()
        layout.setSpacing(15)

        self.fileTypeLabel = QLabel("Select File Type:")
        layout.addWidget(self.fileTypeLabel)

        fileTypeLayout = QHBoxLayout()
        self.fileTypes = ["mp3", "mp4", "jpg", "png", "pdf", 'gif', 'doc', 'docx', 'xls', 'xlsx']
        self.fileTypeButtons = QButtonGroup(self)
        for ft in self.fileTypes:
            btn = QRadioButton(ft.upper())
            self.fileTypeButtons.addButton(btn)
            fileTypeLayout.addWidget(btn)
        layout.addLayout(fileTypeLayout)

        self.srcBtn = QPushButton("Choose Source Folder")
        self.srcBtn.clicked.connect(self.chooseSource)
        layout.addWidget(self.srcBtn)

        self.destBtn = QPushButton("Choose Destination Folder")
        self.destBtn.clicked.connect(self.chooseDestination)
        layout.addWidget(self.destBtn)

        layout.addWidget(QLabel("Choose Operation:"))
        self.copyMoveCombo = QComboBox()
        self.copyMoveCombo.addItems(["Copy", "Move"])
        layout.addWidget(self.copyMoveCombo)

        self.processBtn = QPushButton("Start Processing")
        self.processBtn.clicked.connect(self.startProcessing)
        layout.addWidget(self.processBtn)

        self.resultBox = QTextEdit()
        self.resultBox.setReadOnly(True)
        layout.addWidget(self.resultBox)

        self.setLayout(layout)

    def chooseSource(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Source Folder")
        if folder:
            self.sourcePath = Path(folder)
            self.srcBtn.setText(f"Source: {folder}")

    def chooseDestination(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Destination Folder")
        if folder:
            self.destinationPath = Path(folder)
            self.destBtn.setText(f"Destination: {folder}")

    def log(self, message):
        self.resultBox.append(message)

    def startProcessing(self):
        selectedBtn = self.fileTypeButtons.checkedButton()
        if not selectedBtn:
            self.log("Please select a file type.")
            return

        if not hasattr(self, 'sourcePath') or not self.sourcePath.exists():
            self.log("Please select a valid source folder.")
            return

        if not hasattr(self, 'destinationPath') or not self.destinationPath.exists():
            self.log("Please select a valid destination folder.")
            return

        fileType = selectedBtn.text().lower()
        copyOrMove = self.copyMoveCombo.currentText().lower()

        self.processFileType(fileType, copyOrMove)

    def processFileType(self, fileType, copyOrMove):
        if self.sourcePath.drive == self.destinationPath.drive and copyOrMove == 'move':
            generator, stats = self.scanAndCollectForMove(self.sourcePath, fileType)
            files = list(generator)
            self.log(f"{stats['numberOfMatchedFiles']}/{stats['numberOfFoundFiles']} matched .{fileType} files")
            self.log(f"{stats['potentialFilesNo']} can be moved | {stats['rejectedFilesNo']} rejected due to size")

            if self.confirmationDialog("Do you want to continue the moving process?"):
                self.copyMoveFiles(files, fileType, copyOrMove)
        else:
            gen, counters, freeSpace = self.scanAndCollectForDifferentDestination(self.sourcePath, self.destinationPath, fileType)
            filesWithSizes = list(gen)

            totalSize = counters['sumOfFilesSize'] / (1024**3)
            self.log(f"Total: {counters['numberOfFoundFiles']} | Matched: {counters['numberOfMatchedFiles']} | Size: {totalSize:.2f} GB")

            if totalSize > freeSpace:
                self.showSpaceOptions(filesWithSizes, freeSpace, fileType, copyOrMove)
            else:
                self.copyMoveFiles([x[0] for x in filesWithSizes], fileType, copyOrMove)

    def scanAndCollectForMove(self, sourcePath, fileType):
        counters = {'numberOfFoundFiles': 0, 'numberOfMatchedFiles': 0, 'potentialFilesNo': 0, 'rejectedFilesNo': 0}
        freeSpace = shutil.disk_usage(sourcePath.drive).free / (1024 ** 3)

        def generator():
            for foldername, _, filenames in os.walk(sourcePath):
                for filename in filenames:
                    counters['numberOfFoundFiles'] += 1
                    filePath = Path(foldername) / filename
                    size = os.path.getsize(filePath) / (1024**3)
                    if filePath.suffix[1:] == fileType:
                        counters['numberOfMatchedFiles'] += 1
                        if freeSpace >= size:
                            counters['potentialFilesNo'] += 1
                            yield filePath
                        else:
                            counters['rejectedFilesNo'] += 1
        return generator(), counters

    def scanAndCollectForDifferentDestination(self, sourcePath, destPath, fileType):
        counters = {'numberOfFoundFiles': 0, 'numberOfMatchedFiles': 0, 'sumOfFilesSize': 0}
        freeSpace = shutil.disk_usage(destPath.drive).free / (1024 ** 3)

        def generator():
            for foldername, _, filenames in os.walk(sourcePath):
                for filename in filenames:
                    counters['numberOfFoundFiles'] += 1
                    filePath = Path(foldername) / filename
                    if filePath.suffix[1:] == fileType and filePath.is_file():
                        size = os.path.getsize(filePath)
                        counters['sumOfFilesSize'] += size
                        counters['numberOfMatchedFiles'] += 1
                        yield (filePath, size)

        return generator(), counters, freeSpace

    def showSpaceOptions(self, fileList, freeSpaceGB, fileType, copyOrMove):
        bigger = sorted(fileList, key=lambda x: x[1], reverse=True)
        smaller = sorted(fileList, key=lambda x: x[1])
        default = fileList

        def countFit(sortedList):
            total, count = 0, 0
            for _, size in sortedList:
                sizeGB = size / (1024 ** 3)
                if total + sizeGB <= freeSpaceGB:
                    total += sizeGB
                    count += 1
                else:
                    break
            return count, total

        smallCount, smallSize = countFit(smaller)
        bigCount, bigSize = countFit(bigger)
        defaultCount, defaultSize = countFit(default)

        msg = QMessageBox()
        msg.setWindowTitle("Choose Copy/Move Strategy")
        msg.setText("Not enough space. Choose how to proceed:")

        btn1 = msg.addButton(f"Smaller First ({smallCount} files, {smallSize:.2f} GB)", QMessageBox.AcceptRole)
        btn2 = msg.addButton(f"Bigger First ({bigCount} files, {bigSize:.2f} GB)", QMessageBox.AcceptRole)
        btn3 = msg.addButton(f"Default Order ({defaultCount} files, {defaultSize:.2f} GB)", QMessageBox.AcceptRole)
        cancelBtn = msg.addButton("Cancel Operation", QMessageBox.RejectRole)

        msg.exec_()

        if msg.clickedButton() == btn1:
            finalList = smaller[:smallCount]
        elif msg.clickedButton() == btn2:
            finalList = bigger[:bigCount]
        elif msg.clickedButton() == btn3:
            finalList = default[:defaultCount]
        else:
            self.log("Operation cancelled by user.")
            return

        self.copyMoveFiles([x[0] for x in finalList], fileType, copyOrMove)

    def copyMoveFiles(self, files, fileType, operation):
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        folder = f"{operation}_{fileType}_{timestamp}"
        finalDest = self.destinationPath / folder
        finalDest.mkdir(parents=True, exist_ok=True)

        for file in files:
            try:
                destFile = finalDest / file.name
                if operation == 'copy':
                    shutil.copy2(file, destFile)
                    self.log(f"Copied: {file.name}")
                else:
                    shutil.move(file, destFile)
                    self.log(f"Moved: {file.name}")
            except Exception as e:
                self.log(f"Failed to {operation} {file.name}: {e}")

    def confirmationDialog(self, message):
        return QMessageBox.question(self, "Confirm", message, QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FileFinder()
    window.show()
    sys.exit(app.exec_())
