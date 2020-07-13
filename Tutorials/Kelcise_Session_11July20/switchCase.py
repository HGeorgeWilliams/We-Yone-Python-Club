# implementation of switch case in Python
def week(i):
    switchCase = {0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday'}
    return switchCase.get(i, "Invalid day of week")

print(week(3))