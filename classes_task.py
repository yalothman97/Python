from datetime import date

class Employee:
	def __init__(self,name,age,salary,employment_date,**kwargs):
		self.name=name
		self.age=age
		self.salary=salary
		self.employment_date=employment_date

		for attributes,values in kwargs.items():
			setattr(self,attributes,values)

	def get_working_years(self):
		return date.today().year-self.employment_date

class Manager(Employee):
	def __init__(self,name,age,salary,employment_date,bonus_percentage,**kwargs):
		super().__init__(name, age, salary, employment_date)
		self.bonus_percentage=bonus_percentage

		for attributes,values in kwargs.items():
			setattr(self,attributes,values)

	def get_working_years(self):
		return date.today().year-self.employment_date

	def get_bonus(self):
		return self.bonus_percentage*self.salary

print('\nHR"R"us" Program\n')
dash='-'*30
employee_list=[]
manager_list=[]

while True:
	print('Options:')
	print('1. Show employees\n2. Show managers\n3. Add employee\n4. Add manager\n5. Quit')
	try:
		option=int(input('\nChoose from the above options: '))
	except ValueError:
		print(dash)
		print('Values only, try again.')
		print(dash)
	else:
		print(dash)
		if option==1:
			if len(employee_list)==0:
				print('No employees added yet.')
			for employee in employee_list:
				print('Name: '+employee.name+', Age: '+str(employee.age)+', Salary: '+str(employee.salary)+', Working Years: '+str(employee.get_working_years()))
			print(dash)
		elif option==2:
			if len(manager_list)==0:
				print('No managers added yet.')
			for manager in manager_list:
				print('Name: '+manager.name+', Age: '+str(manager.age)+', Salary: '+str(manager.salary)+', Working Years: '+str(manager.get_working_years())+', Bonus: '+str(manager.get_bonus()))
			print(dash)
		elif option==3:
			employee=Employee(input('Name: ').title(),input('Age: '),float(input('Salary: ')),int(input('Employment date: ')))
			employee_list.append(employee)
			print('\nEmployee added\n')
		elif option==4:
			manager=Manager(input('Name: ').title(),input('Age: '),float(input('Salary: ')),int(input('Employment date: ')),float(input('Bonus Percentage: ')))
			manager_list.append(manager)
			print('\nManager added.\n')
		elif option==5:
			break
		else:
			print('Values only, try again.')
			print(dash)