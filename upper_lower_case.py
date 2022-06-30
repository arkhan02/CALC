patient_name = input("Please enter patient name: ")
birth_year =int(input("Please enter patient birth year: "))
patient_age = 2022 - birth_year
print("Hi " + str(patient_name.upper()) )
print("You are " + str(patient_age) + " years old")
print(patient_name.replace(patient_name,'Hi Arshad'))