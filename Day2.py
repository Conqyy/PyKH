#if statement

if 4>2:
    print("Hello")

#if else statements
# age = int(input("How old are you? "))
# if age >= 18:
#     print("You are an adult")
# else:
#     print("You are not an adult")
#
# #if elif statements
# age = int(input("How old are you? "))
# if age >= 18:
#     print("You are an adult")
# elif age >= 13:
#     print("You are a teenager")
# else:
#     print("You are a kid")

#loops

#for loops
for i in range(5):
    print(i)
print("-----------------------------------------")
for i in range(1,6):
    print(i)
print("-----------------------------------------")
for i in range(0,10,2):
    print(i)
print("-----------------------------------------")

liist = [1,2,4,5,6,7,8]
for i in liist:
    print(i)
print("-----------------------------------------")
string = "Hello"
for char in string:
    print(char)
print("-----------------------------------------")

#while loops
while True:
    msg = input("exit?: ")
    if msg == "yes":
        break # exits the loop
    else:
        print("try again")
        continue # skips current iteration