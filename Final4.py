#18. จงเขียนโปรแกรมหาค่าBMIโดยแสดงผลตามเกณฑ์ที่กำหนด
#Underweight เมื่อ BMIน้อยกว่า 18.5
#Normal weight เมื่อ BMI มีค่าตั้งแต่ 18.5แต่ไม่ถึง25
#Overweight เมื่อ BMI ตั้งแต่ 25 แต่ไม่ถึง 30
#Obesity เมื่อ BMI มีค่าไม่ต่ำกว่า 30
import math

weight = float(input("Weight (kg.) : "))
height = float(input("Height (m.) : "))

BMI = round(weight/height**2, 1)
if (BMI < 18.5):
  print("BMI is " + str(BMI) + "  " + "Underweight")
elif (BMI >= 18.5 and BMI < 25):
    print("BMI is " + str(BMI) + "  " + "Normal weight")
elif (BMI >= 25 and BMI < 30):
    print("BMI is " + str(BMI) + "  " + "Overweight")
elif (BMI >= 30):
    print("BMI is " + str(BMI) + "  " + "Obesity")
else:print("error")




#19. เขียนโปรแกรมเพื่อตรวจสอบ Username , Password เพื่อตรวจสอบว่าเป็น Admin มั้ย
# Username = admin
# Password = Ad13n@23t
Username = input("Username : ")
Password = input("Password : ")
if Username == "admin" and Password == "Ad13n@23t":
    print("Welcome, admin")
else:print("You are not admin")