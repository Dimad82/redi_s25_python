groceries = ["milk", "bread", "rice", "tomatoes", "potatoes", "chocolate"]
#for i in groceries:
#    print(i)

#list_of_stuff = [16, "ten", -8.9546, [1, 3, 5, 7, 9]]
#for x in range(0, len(list_of_stuff)):
#print(list_of_stuff[x] + 10)

print(groceries)

groceries.append("carrot")

print(groceries)

groceries.insert(2, "raddish")
print(groceries)
groceries[2] = "onions" 
print(groceries)
del(groceries[2])
print(groceries)


groceries.append("bread")
print(groceries)
print(groceries.count("bread"))

while groceries.count("bread") > 0:
    groceries .remove("bread")

print(groceries)
groceries.append("rice")
print(groceries)
print(groceries.index("rice"))
print(groceries)
