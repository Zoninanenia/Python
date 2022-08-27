#9. เขียนโปรแกรมแปลงfloat- เป็น int+
    #input1 รับfloat-
    #output1 แสดงเลขที่ปัดทศนิยมขึ้น และ เป็นint+
import math
x = float(input())
print(math.ceil(abs(x)))


#10. รับint+ มา 1 จน. แล้วหาว่าน้อยกว่า 90 มั้ย
x = int(input())
if x < 90:
    print("yes")
elif x >= 90:
    print("no")


#11. รับint+มา 1 จน. แล้วดูว่าเป็นจน.คู่ที่หารด้วย 3 ลงตัวมั้ย
x = int(input())
if x % 2 == 0:
    if x == 0:
        print('no')
    elif x % 3 == 0:
        print('yes')
    else: print('no')
else: print('no')


#12. รับ int แล้วหาจน.ที่มากที่สุด
a = int(input())
b = int(input())
c = int(input())
number = (a , b , c)
import math
print(max(number))


#13. เขียนคำสั่งโดยใช้ loop while เพื่อให้แสดงผลบนหน้าจอดังนี้
     #1 , 3 , 5 , 7 , 9 , 11 , 13 , 15 หยุดที่ 15
     #2 , 5 , 8 , 11 , 14 , 17 หยุดที่ 17
     #30 , 20 , 10 , 0 , -10 , -20 , -30 หยุดที่ -30
for i in range( 1 , 16 , 2 ):
 print(i)
 
for i in range( 2, 18 , 3 ):
    print(i)

for i in range(30 , -31 , -10):
    print(i)


#13. เขียนคำสั่งโดยใช้ loop while เพื่อให้แสดงผลบนหน้าจอดังนี้
     #1 , 3 , 5 , 7 , 9 , 11 , 13 , 15 หยุดที่ 15
     #2 , 5 , 8 , 11 , 14 , 17 หยุดที่ 17
     #30 , 20 , 10 , 0 , -10 , -20 , -30 หยุดที่ -30
for i in range( 1 , 16 , 2 ):
 print(i)
 
for i in range( 2, 18 , 3 ):
    print(i)

for i in range(30 , -31 , -10):
    print(i)