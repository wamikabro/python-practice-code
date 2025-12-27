from datetime import datetime, timedelta, date, time

date1 = date(2025, 12, 25)
time1 = time(15, 30, 45)
datetime1 = datetime(2025, 12, 25, 15, 30, 45)
print("Date:", date1)
print("Time:", time1)
print("Datetime1:", datetime1)
datetime2 = datetime1 + timedelta(days=5, hours=2)
print("Datetime1 after adding 5 days and 2 hours becoming Datetime2:", datetime2)

difference = datetime2 - datetime1 # it it delta
print("Type of difference:", type(difference))
print("Difference between datetime2 and datetime1:", difference)


# replace
datetime3 = datetime1.replace(year=2026, month=1)
print("Datetime1 after replace:", datetime3)