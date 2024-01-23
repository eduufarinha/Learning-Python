alist = ["coffee", "tea"]
# A list can be changed but its slower
alist[0] = "milk"

print(alist)

atuple = ("coffee" , "tea")

# A tuple cant be changed but its faster
#atuple[0] = "milk"
print(atuple)