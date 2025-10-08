age = int(input("Enter your age: "))


is_eligible = age >= 18
is_minor = age < 18 


print(f"age: {age}")
print(f"Elligible to vote: {is_eligible}")
print(f"Still a minor: {is_minor}")
