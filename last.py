#Restaurant_Menu_Program
print("---Welcome to Zania Coffee---"+"\n")
x = str(input("Please type 1 to show menu : "))
if (x == "1") :
  print("\n")
  print("---Choose the menu---")
  print("1.Espresso")
  print("2.Cappucino")
  print("3.Latte"+"\n")
  coffee = int(input("Select coffee : "))
  if (coffee >= 1 and coffee <= 3):
    menu = ["Espresso","Cappucino","Latte"]
    print("\n")
    print("---Choose the type of the coffee---")
    print("1.Hot 55 baht")
    print("2.Cold 60 baht")
    print(" ")
    coffee_type = int(input("Select type : "))
    if (coffee_type == 1):
      print("---You choose hot " + menu[coffee-1] + " 55 baht---"+"\n")
    elif (coffee_type == 2):
      print("---You choose cold " + menu[coffee-1] + " 60 baht---"+"\n")
    else:print("Error,please type again")
  else:print("Error,please try again")
  price = [55,60]
  money = int(input("Input your money : "))
  while money < price[coffee_type-1]:
    money = int(input("Input your money : "))
  else:
    change = money-price[coffee_type-1]
    print("You received a change of " + str(change) + " baht")
    print("---Thank you---")
else:print("Error,please enter 1 in input again")