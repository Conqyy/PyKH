#lists

fruits = ['apple', 'banana', 'cherry']
fruits.append('orange') # adds a new item to the end of the list
fruits.insert(0, 'grape')# adds a new item to a certain position of the list
fruits.remove('banana') # removes the first item that matches the value
fruits.pop()# removes the item of the list and returns it
fruits.pop(1) # removes the item of the list at a certain position and returns it

fruitsWithoutApple = fruits[1:]
name = 'KHalid Abdulaziz Alluhaydan'
nameList = name.split(' ')# splits the string into a list separated by spaces
print(name[0])
print(nameList[0])

nums = [10,20,30]
print(nums)
for i, num in range(len(nums)): # going through each item in the list (i is the index)
    nums[i]=24
print(nums)

#maps
map = {'name':'Khalid', 'age':24}
print(map['name'])