first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
org_name = input("Enter organization name: ")

email = first_name.lower() + "." + last_name.lower() + "@" + org_name.lower() + ".com"

print("Generated Email ID:")
print(email)
