x = bool(0)
print(x)

x = bool("")
print(x)

#รับค่า a,b เป็นจำนวนเต็ม แล้วสลับคตัวแปร
#input1 - รับ  a  เป็น int
#input2 - รับ b เป็น int
#output1 - สลับค่าจากตัวแปร a ให้เป็น b
#output2 - สลับค่าจากตัวแปร b ให้เป็น a
a = int(input())
b = int(input())

a = a + b
b = a - b

a -= b

print(a,b)