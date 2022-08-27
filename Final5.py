#18-21 จงเขียนการทำงานให้ถูกต้อง
#กำหนด x = ["dog" , "cat" , "hamster"]
#18. เพิ่มข้อมูล"snake" ไปที่ท้ายสุดของlist
#19. เพิ่มข้อมูล "bird" ไปที่ตำแหน่งที่ 2
#20. ลบข้อมูลตัวสุดท้าย
#21. ลบข้อมูล "dog"
x = ["dog" , "cat" , "hamster"]
x.append("snake")
print(x)
x.insert(2,"bird")
print(x)
x.pop(4)  #ใช้ .remove("snake") เอาก็ได้
print(x)
x.remove("dog") #ใช้ .pop(0) ได้เหมือนกัน
print(x)

#22. เขียนโปรแกรมรับ int ถ้าเป้น int+ ให้พิมพ์หลักเลขออกมาทีละหลักต่อหนึ่งบรรทัด เริ่มจากหลักน้อยสุด
    #ถ้าเป็น 0 หรือ int- ให้พิมพ์ "ERROR"

number = int(input("Please enter number : "))
if (number > 0):
  reversed = int(str(number)[::-1])
  for result in str(reversed):
    print(result)
else:print("ERROR")

#23. รับข้อความเข้ามา แล้วตรวจว่ามีสระทั้งหมดกี่ตัว โดยให้แสดงดังนี้
     #input = hello python 
     #output = a=0 e=1 i=0 o=2 u=0 total = 3









#24. เขียนโปรแกรมเพื่อตรวจสอบว่าตั้ง username ถูกต้องมั้ย โดยมีเกณฑ์ดังนี้
     #username ต้องอยู่ระหว่าง 4-25 ตัวอักษร
     #ต้องขึ้นต้นด้วยตัวอักษร
     #สามารถประกอบด้วยตัวอักษร,ตัวเลข และ(_)ได้
     #ต้องไม่ลงท้ายด้วย (_)
username = input("Enter username : ")
if username.endswith("_"):
  print("ERROR")