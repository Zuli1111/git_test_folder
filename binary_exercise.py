num = int(input("Enter a number:"))
bit = int (input("Enter how many bits do you want? (2-16):"))
bin = format(num, f"0{bit}b")
neg = format((1 << bit) - num, f"0{bit}b")


print(f"{num} in binary is {bin}")
print(f"{num} negative in binary is {neg}")