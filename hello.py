# create a list with 10 different types of fruit
fruit = [
    "apple",
    "banana",
    "cherry",
    "orange",
    "kiwi",
    "melon",
    "mango",
    "pear",
    "pineapple",
    "grape",
]
# loop through the fruits and count the total fruits in the list
for i in fruit:
    # use an f-string to print the fruit name and the number of the fruit in the list
    print(f"{i} is fruit number {fruit.index(i) + 1} in the list")

# the total number of fruits in the list
print(f"There are {len(fruit)} fruits in the list")
