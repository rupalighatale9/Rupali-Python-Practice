##for i in range(21):
##    if i == 11:
##        break
##    print(i)
##print("stop")

##for i in range(21):
##    if i%2==1:
##        continue
##    print(i)
##
##for i in range(50):
##    if i < 11:
##        continue
##    print(i,end=" ")
    
name = input('Enter employee name - ')
id = input('Enter employee ID -')
salary = int(input('Enter employee salary(Monthly)-'))
leave_days = int(input('Enter leave(Days) -'))
tds = int(input('TDS % -'))
month = int(input('month - '))
year = int(input('year -'))

print('employee name = ',name)
print('employee ID = ',id)
print('employee salary(Monthly)',salary)
ctc = salary*12
print('ctc yearly salary =',ctc)
if month == 1 or month ==3 or month ==5 or month == 7 or month == 8 or month == 10 or month == 12:
    day_salary = salary/31
else:
    day_salary = salary/30
print('Day_salary = ',day_salary)
leave_amount = leave_days * day_salary
print('leave Amount = ',leave_amount)





















