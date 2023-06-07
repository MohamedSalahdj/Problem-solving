# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar
from  datetime import datetime
date = input()
date = datetime.strptime(date, '%m %d %Y')

print(calendar.day_name[calendar.weekday(date.year, date.month, date.day)].upper())

