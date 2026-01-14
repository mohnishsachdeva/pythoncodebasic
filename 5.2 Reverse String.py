def reverse_string(s):
    return s[::-1]

print("Reversed string:", reverse_string("Python"))


def reverse_string(s):
    rev = ""
    for ch in s:
        rev = ch + rev
    return rev

print("Reversed string:", reverse_string("Python"))
