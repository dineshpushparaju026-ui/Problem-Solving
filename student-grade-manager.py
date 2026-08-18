student=[]
for i in range (3):
 studentname=input()
 mathsmark=int(input())
 sciencemark=int(input())
 englishmark=int(input())


 average=(mathsmark+sciencemark+englishmark)/3



 if average>=90:
    grade="A"
    print("GRADE:",grade)


 elif average>=80:
    grade="B"
    print("GRADE:",grade)

 elif average>=70:
    grade="C"
    print("GRADE:",grade)

 elif average>=60:
    grade="D"
    print("GRADE:",grade)

 else:       
    grade="FAIL"
    print("GRADE:",grade) 

 one_student=[studentname,average,grade]
 student.append(one_student)
 print(student)



for i in student:
  print("STUDENT NAME:",i[0])
  print("STUDENT AVERAGE:",i[1])
  print("STUDENT GRADE:",i[2])



