supplies = ["tent", "sleeping bags", "water", "raspberry pi","coffee", "knife", "ethernet cable", "flash drive", "beard oil", "marshmallows"]

camp_site = ["Crystal Lake", 404, 89.3, False]

supplies.extend(["toilet paper", "bidet"])
# ->supplies.clear() is used to clear a list
#supplies.clear()
# ->supplies.clear() is used to clear a list


# ->supplies.remove("tent") is used to remove a item from a list
supplies.remove("tent")

# ->print("This item was just deleted: " + supplies.pop(0)) is used to remove a item from a list and print it with a message)

print("This item was just deleted: " + supplies.pop(0))
# ->supplies.pop(index) is used to remove a item from a list)
supplies.pop(0)
print(supplies)