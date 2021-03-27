# Print numbers (1...20). 
# Expect if the number divisable by 3 insert the word 'fizz'.
# If the number is divisable by 5, insert the word 'bop'.
# If the number is divisable by both 3 and 5, then print the word 'fizzbop'.
# Ask the user, 'What is the max number they'd like to go up to?'.
# Creating a class.

max_num = int(input("What is the max number you'd like to go up to?: " ))

class FizzBop:
    def __init__(self, fizz, bop):
        self.fizz = fizz
        self.bop = bop

    def run(self, max):
        for num in range(1,max+1):
            if num % self.fizz == 0 and num % self.bop == 0:
                print('fizzbop')
            elif num % self.bop == 0:
                print('bop')
            elif num % self.fizz == 0:
                print('fizz')
            else:
                print(num)


fizzbop = FizzBop(3, 5)
fizzbop.run(max_num)

fizzbop2 = FizzBop(2, 7)
fizzbop2.run(max_num)