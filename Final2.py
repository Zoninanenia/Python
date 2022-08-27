#6. อ่านข้อมูลองศาเซลเซียส แล้วคำนวณเป็นองศาฟาเรนไฮต์และเคลวิน
    #input 1 บรรทัดประกอบด้วยค่าองศาเซลเซียส เป็น float
    #output 1 บรรทัดประกอบด้วย float 2 จน. คั่นด้วยเว้นวรรค
              #จน.แรกคือฟาเรนไฮต์ จน.สองคือเคลวิน
c = float(input())
f = 9/5 * c + 32
k = c + 273.15
print(str(f) + " " + str(k))


#7. เขียนโปรแกรมรับ int มา 2 จน. แสดงผลโดยใช้ op + 
    #input1 รับ int a
    #input2 รับ int b 
    #output1 แสดง "Addition: " ตามด้วย a + b
    #output2 แสดง "Concatenation: " ตามด้วยข้อความที่เป็นการเชื่อมระหว่าง a & b
a = int(input())
b = int(input())
print("Addition : " + str(a+b))
print("Concatenation : " + str(a)+str(b))


#8. เขียนโปรแกรมเพื่อแปลงเลขint- เป็นint+
    #input1 รับint-
    #output1 แสดงint+
import math
a = int(input())
print(abs(a))
