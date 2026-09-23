total=0
result="passed"
for i in range(1,6):
 mark=int(input("enter marks:"))
 if(mark<50):
     result="failed"
 total=total+mark
per=total/500*100
print("your result is:",result)
print("total_marks is:",total)
if(per>=90):
    print("you got A+")
elif(per>=80):
    print("you got A")
elif(per>=70):
    print("you got B")
elif(per>=60):
    print("you got C")
elif(per>=50):
    print("you got D")
else:
    print("you got F")

