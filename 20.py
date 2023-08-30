# Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.
# Suppose the following input is supplied to the program:
# 7
# Then, the output should be:
# 0
# 7
# 14
class DivisibleBy7:
    def byseven(self, n):
        for number in range(0, n+1):
            if (number%7==0):
                yield number
divisible  = DivisibleBy7()
for i in divisible.byseven(int(input('Pleaes enter a number'))):
    print(i)