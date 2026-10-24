#age checker
# age = 34

# if(age >= 18):
#     print("can vote")
# else:
    # print("can not vote")
# print("--------------------------------------------")
# # calculater
# user1 = int(input("enter your first output"))  
# oprater = input("enter your oprater (+, -, /, * )")
# user2 = int(input("enter your second output"))
# if( oprater == "+"):
#     print( "final answer", user1+user2)
# elif(oprater == "-"):
#     print(  "final answer", user1-user2)
# elif(oprater == "*"):
#  print("final answer:", user1 * user2)
# elif(oprater == "/"):
#    print("final answer:", user1 / user2)
# ////////////////////////////////////////////////////
# list = [23, 45, 78, 46]
# print(list.sort)
# print(list)
#           # print("--------------------------------------")
# list = [10, 20, 30, 40, 50]
# list.reverse()
# print(list)
# ////////
# insert an element
# list =[ 10, 20, 40, 50]
# list.insert(2, 30)
# print(list)
# ///////////////////
# insert an eliment in the end of the list
# list = [ "apple", "pea", "seeds"]
# list.append("grapees")
# print(list)
# ////////////////////////
# list = [1, 2, 1]
# list_copy = list.copy()

# if(list_copy == list):
#     print("this is pendrome")
# else:
#     print("this is not pendrome")
# ////////////////////////////////////
# movies= []
# MOV1=input("enter name of your movies:")
# MOV2=input("enter name of your second movies:")
# MOV3=input("enter name of your third movies:")
# movies.append(MOV1)
# movies.append(MOV2)
# movies.append(MOV3)
# print(movies)
# ////////////////////////////////////
# price1 = float(input("Enter your price of the 1st product"))
# price2 = float(input("Enter your price of the 2nd product"))
# totle_price = price1 + price2
# print("Totle price :", totle_price)
# ////////////////////////////////////
# balance = float(input("Enter your balance here:"))
# withdrawal = float(input("Enter how much amount you want to withdrawal:"))
# if(withdrawal<=balance):
#     print("withdrawal successful")
# else:
#     print("Insufficient balance")
# ////////////////////////////////////
# birth_year = int(input("enter your date of birth"))
# current_year = 2026
# age = current_year - birth_year
# print("this is your age:", age)
# /////////////////////////////////////////
# Celsius = float(input("enter the temprature in Celsius:"))
# Fahrenheit =(Celsius * 9/5) + 32
# print("here is your temprature in Fahrenheit:", Fahrenheit)
# Topic 2: Operators & Arithmetic
# Ask for the total food bill. Calculate a 5% service charge and print the final bill.
# food_bill = int(input("enter your food bill amount:"))
# service_charge = food_bill *5/100
# totle_bill = food_bill + service_charge
# print(totle_bill)
# ////////////////////////////////
# Question 5. Shopping Discount
# shoping_amount= int(input("enter your shoping amount:"))
# if(shoping_amount >= 5000):
#     discount = shoping_amount *20/100
# elif(shoping_amount >= 2000):
#     discount = shoping_amount *10/100
# else:
#     print("no discount applicable")
# totle_amount = shoping_amount - discount
# print("here is your totle bill:",totle_amount)
# Topic 3: Strings & Built-in Functions
# Question 7. Username Formatter
# user_name= input("enter your name: ")
# clean_name =user_name.strip()
# Formate_name = clean_name.title()
# lenght_user = len(clean_name)
# print("your formate name;", Formate_name)
# print("lenght of the carecter:", lenght_user)
# ////////////////////////////////////////////////
# Question 8. Password Length Checker
# password_user = input("enter your password:")
# lenght_ofPass = len(password_user)
# if(lenght_ofPass >= 8):
#     print("password lenght is accepted ")
# else:
#     print("password too short")
# //////////////////////////
# Question 9. Email Formatter
Email_user = input("enter your email:")
clean_email = Email_user.strip()
lower_caseEmail = clean_email.lower()
print("filtered Email:",lower_caseEmail)