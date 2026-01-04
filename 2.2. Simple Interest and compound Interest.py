p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time (years): "))

# Simple Interest
si = (p * r * t) / 100
print("Simple Interest:", si)

# Compound Interest
ci = p * (1 + r / 100) ** t - p
print("Compound Interest:", ci)
