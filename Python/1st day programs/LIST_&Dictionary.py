List1=[1,2,3,4,5,6,7,8,9,34,1,45,23]

List2even=[]
List3odd=[]

for x in List1 :
    if (x%2==0) :
        List2even.append(x)
    else:
        List3odd.append(x)

print("Even Numbers in List" ,List2even)
print("odd Numbers in List" ,List3odd)

evenSum=sum(List2even)
oddSum=sum(List3odd)

Dict={"Even Sum is " : evenSum,
      "Odd Sum is ":oddSum}
print("Dictionary Output =",Dict)






