print('Hello , welcome to the Coffee Shop !!!')

name = input("What is your name ? \n")
if name == "Robbert" or name == "Patricia" or name == "Loki":
  evil_status = input("Are you evil " + name + "?\n")
  good_deeds = int(input(How many good deeds have you done today?\n=))
  if evil_status == "yes" and good_deeds < 4:
    print("You're not welcome here " + name + "! Get out !")
    exit()
else:
  print("Hello "  + name + ", thank you for coming in today !\n\n")

menu = "Black Coffee, Espresso, Latte, Cappucino, Frappucino"

print(name + ", what would you like from our menu today? Here is what we are serving. \n" + menu)

order = input()

price = 8

if order == "Frappucino":
  price = 10
elif order == "Black Coffee":
  price = 8
elif order == "Espresso":
  price = 6
elif order == "Latte":
  price = 4
elif order == "Cappucino":
  price = 2
else:
  print("Sorry, we dont have that here.")
  goback = input("Would you like to order other product ?\n")
  if goback == "yes":
    print(menu)
    order = input()
  elif goback == "no":
    print("Thank you for visiting us !")
    exit()
  
quantity = input("How many coffees would you like ?\n")

total = price * int(quantity)


print("Thank you. Your total is: $" + str(total))


print("Sounds good " + name + ", we'll have your " + quantity + " " + order + " ready for you in a moment.")