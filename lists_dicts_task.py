print("\nWelcome to Coded, the first coding bootcamp in the Middle East")
print("Fresh Grad Bootcamp - Apply Here:\n")

skills = ["python", "javascript", "java"]

cv = {}

name = input("What is your name?  ")
cv['name'] = name

age = int(input("How old are you?  "))
cv['age'] = age

experience = int(input("Years of experience?  "))
cv['experience'] = experience

cv['skills'] = ''

print("\n")

skill_num = 1
for skill in skills:
	print("Skill #{}) {}".format(skill_num, skill))
	skill_num += 1

choose_skill_1 = input("\nChoose a skill from the above options (word form):  ")

cv['skills'] = choose_skill_1


choose_skill_2 = input("Choose another skill:  ")
cv['skills2'] = choose_skill_2

if age >= 18 and age <= 26 and experience >= 2 and (choose_skill_1 == "java" or choose_skill_2 == "java"):
	print("APPLICATION ACCEPTED")
else:
	print("Unfortunately, your application does not meet the requirements")