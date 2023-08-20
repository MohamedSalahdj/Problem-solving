"""
The number I'm afraid of depends on which day of the week it is... This is a concrete description of my mental illness:

Monday --> 12

Tuesday --> numbers greater than 95

Wednesday --> 34

Thursday --> 0

Friday --> numbers divisible by 2

Saturday --> 56

Sunday --> 666 or -666

Write a function which takes a string (day of the week) and an integer (number to be tested) so it tells the doctor if I'm afraid or not. (return a boolean)


"""

def am_I_afraid(day,num):
    days_with_number = {
        'Monday' : 12,
        'Wednesday' : 34,
        'Thursday' : 0,
        'Saturday' : 56,
    }
    if day in days_with_number:
        if days_with_number[day] == num:
            return True
        else : 
            return False
    elif day == 'Tuesday':
        if num > 95:
            return True
        else:
            return False
    elif day == 'Friday':
        if num % 2 == 0:
            return True
        else:
            return False
    elif day == 'Sunday' and num in (666, -666) :
            return True
    else:
        return False
    
    