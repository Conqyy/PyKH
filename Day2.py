#if statement

if 4>2:
    print("Hello")

#if else statements
age = int(input("How old are you? "))
if age >= 18:
    print("You are an adult")
else:
    print("You are not an adult")

#if elif statements
age = int(input("How old are you? "))
if age >= 18:
    print("You are an adult")
elif age >= 13:
    print("You are a teenager")
else:
    print("You are a kid")
