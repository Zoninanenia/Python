#1. แสดงผล "Hello World!"
print("\"Hello World!\"")

#2. birthday = 25  ฉันเกิดวันที่ 25
x = input()
print("ฉันเกิดวันที่ " + str(x))


#3. รับค่า & เข้ามา 1 ครั้ง จากนั้นรับ int แล้วแสดงผล
a = str(input())
x = int(input())
print(a * x)


#4. เขียนโปรแกรมรับข้อมูลนน.สส. 
    #input1 รับค่า weight เป็น int
    #input2 รับค่า height เป็น int
    #output แสดงข้อมูลนน.สส.เป็น int โดยเว้น 1 ช่อง
weight = int(input())
height = int(input())
print(str(weight) + " " + str(height))


#5. เขียนโปรแกรมคำนวณหาพท.สามเหลี่ยม
    #input1 รับค่า base เป็น float
    #input2 รับค่า height เป็น float
    #output แสดงพท.สามเหลี่ยม เป็น float
base = float(input())
height = float(input())
print(1/2 * base * height)