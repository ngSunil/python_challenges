# Write a Python generator class to generate all the even numbers upto n

def genEven(n):
    for i in range (0 ,n+1):
        if i%2 ==0:
            yield i


for i in genEven(int(input('Please enter a number: '))):
    print(i)