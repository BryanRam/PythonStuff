# If number is even, then collatz() should print number // 2 and
#return this value. If number is odd, then collatz() should print
#and return 3 * number + 1.

def collatz(num):
    if num % 2 == 0:
        result = num // 2
        print(str(result))
        return int(result)
    else:
        result = 3 * num + 1
        print(str(result))
        return int(result)

print('Please enter a number')
while True:
    try:
        num = int(input())
    except ValueError:
        print ('Error. You must enter an integer')
        continue
    break

while num != 1:
    num = collatz(num)
