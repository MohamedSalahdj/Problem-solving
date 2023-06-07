# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar
from  datetime import datetime
d = input()
d = datetime.strptime(d, '%d %m %Y')

# print(d.day)
# print(d.strftime('%A'))
print(calendar.day_name[calendar.weekday(d.year, d.month, d.day)])

