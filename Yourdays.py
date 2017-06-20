from datetime import date

x = date.today()

print 'Enter Year, month, Day of your Birthday:'
y, m, d = map(int, raw_input().split(","))

print y, m, d
birthday = date(y, m, d)

print (x - birthday).days
