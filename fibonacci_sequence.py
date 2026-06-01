terms=int(input("Enter number of terms: "))

# for first two terms
n1,n2=0,1
count=0

# checking if term is valid
if terms<=0:
    print("Invalid! Enter positive integer")
# generating fibonacci sequence
elif terms==1:
    print("Fibonacci sequence upto",terms,"term: ")
    print(n1)
else:
    print("Fibonacci sequence upto",terms,"terms: ")
    while count<terms:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1
