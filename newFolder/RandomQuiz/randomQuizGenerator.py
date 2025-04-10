# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.

import random

# The quiz data Keys are states and values are their capitals.

capitals = {
    'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock',
    'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover',
    'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise',
    'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka',
    'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis',
    'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City',
    'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany',
    'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia',
    'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
    'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'
}

# generate 35 quiz files
for quizNum in range(35):
    # Create the quiz and answer key files.
    quizFile = open(f'capitalsquiz{quizNum+1}.txt', 'w') # e.g. capitalsquiz1.txt
    answerKeyFile = open(f'capitalsquiz_answers{quizNum+1}.txt', 'w') 

    # Write out the header for the quiz.
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + f'State Capitals Quiz (Form{quizNum + 1})')
    quizFile.write('\n\n')

    # Shuffle the order of the states.
    states = list(capitals.keys())
    random.shuffle(states)


    # Loop through all 50 states, making a question for each.
    for questionNum in  range(50):

        # Get right and wrong answers.
        # states is the key of capitals here as we have set earlier 
        # it will store correct capital of the state
        correctAnswer = capitals[states[questionNum]]

        # create list of all available states in the capitals
        wrongAnswers = list(capitals.values())
        # remove correct answer from it
        # index() returns the index of correctAnswer from  wrong answers 
        del wrongAnswers[wrongAnswers.index(correctAnswer)]

        # pick 3 randome wrong options 
        wrongAnswers = random.sample(wrongAnswers, 3)

        # merge corrctAnswer element to the wrongAnswers list
        answerOptions = wrongAnswers + [correctAnswer]

        # shuffle the answerOptions so the correct answer is not in the end always
        random.shuffle(answerOptions)

        # Write the question and the answer options to the quiz file.
        quizFile.write(f'{questionNum + 1}: What is the capital of {states[questionNum]}?\n')

        for i in range(4):
            # {'ABCD'[i]} means A, then B, then C, then D on each loop cycle
            quizFile.write(f"   {'ABCD'[i]}. { answerOptions[i]}\n")
            quizFile.write('\n')
        
        # write the correct key to the answer key file for each question
        # from ABCD, the correct match will be picked according to index number
        # since ABCD is always in this form even in the answerOptions.
        # so if 1 is returned, it means B in answerOptions, and then from our 
        # 'ABCD' B will be picked and stored in answerKeyFile together with
        # its question number
        answerKeyFile.write(f"{questionNum + 1}: {'ABCD'[answerOptions.index(correctAnswer)]}\n")
        
    # close
    quizFile.close()
    answerKeyFile.close()



