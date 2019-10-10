# Numbers

#     str()
# num1=28
# print (str(num1))
# print(str(num1) + ' days in FEB')
# print('------------------')
# int()  & float()

# f_num='5'
# l_num='6'
#
# print (int(f_num) + float(l_num))
# print (int(f_num) + int(l_num))


#     datetime
from datetime import datetime, timedelta
today=datetime.now()
print(today)
print(str(today))
print('day :' + str(today.day))
print('Month :' + str(today.month))
print('Year :' + str(today.year))

# section 2 timedelta#
delta_days= input('Input How many days before? > ')
date_before= today - timedelta(days=float(delta_days))
print( str(delta_days) + ' days before is :' + str(date_before))

# section 3 datetime.strptime
# birthday = input('When is your birthday (yyyy/mm/dd)?')
# birthday_date = datetime.strptime(birthday,'%Y%m%d')
# print('birthday =' + str(birthday_date))
