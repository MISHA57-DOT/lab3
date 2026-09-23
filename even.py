total=0
even_count=0
odd_count=0
for i in range(1,11):
    number=int(input("enter ur number:"))
    total+=number
    if(i==1):
        largest=number
        smallest=number
    if(number%2==0):
           even_count+=1
    else:
           odd_count+=1
    if(number>largest):
        largest=number
    if(number<smallest):
        smallest=number

average=float(total/10)
print("average is:",average)
print("even count:",even_count)
print("odd count:",odd_count)
print("largest:",largest)
print("smallest:",smallest)




