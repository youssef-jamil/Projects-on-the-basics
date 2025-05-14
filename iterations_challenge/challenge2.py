# second challenge
# ? Create a list named fruits
fruits = ["apples", "bananas", "grapes", "mangos", "nectarines", "pears"]
# ? will print the all the elements in the list by type list
print("I have a list of fruits:", fruits, "in the list")


print("======================================================")
# ? will print each element in the list in a new line
for fruit in fruits:
    print(fruit)

print("======================================================")
# ? will print each element in the list until the index 4
counter = 0
while fruits[counter] != "nectarines":
    print(fruits[counter])
    counter += 1


print("======================================================")

# ? using break statement in the for loop
for f in fruits:
    if f == "nectarines":
        break
    print(f)
