def check_birthdate(year, month, day):
	from datetime import date
	if year > date.today().year and month > date.today().month and day > date.today().day:
		return False
	else:
		return True

def calculate_age(year, month, day):
	from datetime import date
	calc_year = date.today().year - year
	calc_month = date.today().month - month
	calc_day = date.today().day - day
	print("You are {} year(s), {} month(s), and {} day(s) old".format(calc_year, calc_month, calc_day))

year = int(input("Enter birth year: "))
month = int(input("Enter birth month: "))
day = int(input("Enter birth day: "))

if check_birthdate(year, month, day) == True:
	calculate_age(year, month, day)
else:
	print("Invalid birthday")