dob = input("Enter Date of Birth (DD-MM-YYYY): ")

parts = dob.split("-")

birthday = {
    "Day": parts[0],
    "Month": parts[1],
    "Year": parts[2]
}

print("Birthday details dictionary:")
print(birthday)

# Using join method
formatted_date = "/".join(parts)
print("Formatted Date:", formatted_date)
