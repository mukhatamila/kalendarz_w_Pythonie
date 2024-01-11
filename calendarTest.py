# Kalendarz w Python

import calendar
yy = 2023
mm = 6
print(calendar.month(yy, mm))

yy = 2023
mm = 0
print(calendar.month(yy, mm))
# error

yy = -2023
mm = 6
print(calendar.month(yy, mm))

yy = 2023
mm = -6
print(calendar.month(yy, mm))
# error

yy = 0
mm = 6
print(calendar.month(yy, mm))
# print (calendar.calendar(2018)) 