name = input("Enter name:")
hour_week = int(input("Enter number of hours worked weekly:"))
hour_pay = float(input("Enter hourly pay rate:"))
CPF = float(input("Enter CPF contribution rate(%):"))

gross_pay = hour_week*hour_pay
contribution = gross_pay*CPF/100
net_pay = gross_pay - contribution


print('\nPayroll statement for', name,
      '\nNumber of hours worked weekly:', hour_week,
      '\nHourly pay rate: $',"%.2f" % hour_pay,
      '\nGross pay = $',"%.2f" % gross_pay ,
      '\nCPF contribution at',CPF,'% = $', "%.2f" % contribution,
      '\n',
      '\nNet pay = $', "%.2f" % net_pay)
