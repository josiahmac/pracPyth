from calendar import weekday
import random
import time, sys


# # print("First num")
# # x = int(input())

# # print("Second num")
# # y = int(input())

# # x+=y
# # print(x)   




# # x, counter = 0,0

# # while True:
# #     x = random.randint(0,9)
# #     print(x)
# #     counter+=1
# #     print("Counter: "+str(counter))

# #     if(x==5):
# #         break




# # try game

# win = 0
# lose = 0
# tie =0

# while True:
#     print("ROCK, PAPER, SCISSORS")
    
#     # User move
#     while True:
#         print("Enter move: ")
#         player = input()

#         if player == 'r':
#             break
#         elif player == 'p':
#             break
#         elif player == 's':
#             break
#         else:
#             print("Input r for ROCK, s for SCISSORS, p for PAPER ")


#     # Computer move
#     bot = ''
#     randomnum = random.randint(1,3)

#     if randomnum == 1:
#         bot = 'r'
#     elif randomnum == 2:
#         bot = 'p'
#     elif randomnum == 3:
#         bot = 's'

#     print(bot)
#     #win lose
#     if player == bot:
#         print("It's a tie")
#         tie+=1
#     elif player == 'r' and bot == 'p':
#         print("You lose!")
#         lose+=1
#     elif player == 'r' and bot == 's':
#         print("You win!")
#         win+=1
#     elif player == 's' and bot == 'p':
#         print("You win!")
#         win+=1
#     elif player == 's' and bot == 'r':
#         print("You lose!")
#         lose+=1
#     elif player == 'p' and bot == 'r':
#         print("You win!")
#         win+=1
#     elif player == 'p' and bot == 's':
#         print("You lose!")
#         lose+=1
# def tryNum(num):
#     if num==1:
#         return "One"
#     else:
#         return "Not One"

# print(tryNum(1))
# print(tryNum(random.randint(1,9)))

# print('Hello', end=' ')
# print('World')

# #Global Variables Can Be Read from a Local Scope
# def spam():
#     print(eggs)
# eggs = 42
# spam()
# print(eggs)

# def spam(divideBy):
#     return 42 / divideBy

# # print(spam(2))
# # print(spam(12))
# # print(spam(0))
# print(spam(1))

# def zigZag():
#     indent = 0
#     indentIncreasing = True

#     try:
#         while True:
            
#                 print(' '*indent, end='')
#                 print('**********')

#                 time.sleep(0.1) 

#                 if indentIncreasing:
#                     indent+=random.randint(1,3)

#                     if indent>=random.randint(5,25):
#                         indentIncreasing = False
                
#                 else:
#                     indent-=random.randint(1,3)
#                     if indent<=0:
#                         indentIncreasing = True
#     except KeyboardInterrupt:
#         sys.exit


# zigZag()


listahan = ['rawr', 'rar', 'rur', 'ror', 'rauwr']

# listatu= listahan[1:4]*3+listahan

# print(listatu)

# for i in listahan:
#     print(i)

# print('dlalja' in listahan)

# for index, item in enumerate(listahan): *****
#     print(str(index)+' = '+item)

# print(random.choice(listahan))

# random.shuffle(listahan)

# for i in listahan:
#     print(i)

# for i in random.choice(listahan):
#     print(i)
# print(listahan.index('ror'))

listahan.append('hkhk')
listahan.insert(0,'kokokok')

# for i in listahan:
#     print(i)

# listahan.remove('hkhk')

# for i in listahan:
#     print(i)

# listahan.sort()

# for i in listahan:
#     print(i)

# listahan.sort(reverse=True)

# for i in listahan:
#     print(i)

# listahan.sort(key=str.upper)
# print(listahan)

