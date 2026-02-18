import random 

x = random.randint(0,100)
y = random.randint(0,100)

print(f'what is {x} + {y}?')

answer = x + y

response = int(input("what is the answer? "))

if answer == response:
    print('correct')
else:
    print('incorrect')


