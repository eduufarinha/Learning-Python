#camp_stuff = "tent, sleeping bags, water, raspberry pi, coffee, knife, ethernet cable , flash drive, beard oil, marshmallows"

#PYTHON List

camping_list = ["tent", "sleeping bags", "water", "raspberry pi","coffee", "knife", "ethernet cable", "flash drive", "beard oil", "marshmallows"]

camp_site = ["Crystal Lake", 404, 89.3, True]

me = camping_list[4]
you = camping_list[-1]

print(me)
print(you)


#camping_list.append("toilet paper") only 1 item added to list

#camping_list.extend( ["toilet paper", "bidet"]) add more than 1 item to list
#camping_list = camping_list + ["toilet paper", "bidet"] add more than 1 item to list

camping_list.insert(0 , "toilet paper") #add item to list at specific index
camping_list.insert(-1 , "bidet") #add

print(camping_list)