name = input("Enter name:")
hour_week = int(input("Enter number of hours worked weekly:"))
hour_pay = float(input("Enter hourly pay rate:"))
CPF = float(input("Enter CPF contribution rate(%):"))

gross_pay = hour_week*hour_pay
contribution = gross_pay*CPF/100
net_pay = gross_pay - contribution

print('\nPayroll statement for', name)
print('Number of hours worked weekly:', hour_week)
print("Hourly pay rate: ${0:.2f}".format(hour_pay))
print("Gross pay = ${0:.2f}".format(gross_pay))
print("CPF contribution at {0}% = ${1:.2f}".format(CPF, contribution))
print('\n')
print("Net pay = ${0:.2f}".format(net_pay))
