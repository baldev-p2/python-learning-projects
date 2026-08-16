# Print a multiplication table for a given number

user = int(input("Enter a number: "))

for i in range(1,11):
    print(f"{user} x {i} = {user * i}")
