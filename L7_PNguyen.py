#Authors: Peter Nguyen
#Assignment: Lab #6
#Completed (or last revision): 10/25/2022
from random import *
#Task 1
words = ("python is an easy language python is easy to learn and easy to code a lot of python modules that are easy to use go python")
wordsList = words.split(" ")
list(wordsList)
wordsList.sort()
finalDictionary = {x:wordsList.count(x) for x in wordsList}
frequency = finalDictionary.values()
print(finalDictionary)
sortedDictionary = sorted(finalDictionary, key = finalDictionary.get)
counter = len(sortedDictionary)
amount = counter-1
for i in range(3):
     print(sortedDictionary[amount-i])

#Output for Task 1
# {'a': 1, 'an': 1, 'and': 1, 'are': 1, 'code': 1, 'easy': 4, 'go': 1, 'is': 2, 'language': 1, 'learn': 1, 'lot': 1, 'modules': 1, 'of': 1, 'python': 4, 'that': 1, 'to': 3, 'use': 1}
# python
# easy
# to
     
#Task 2
R1 = []
R2 = []
R3 = []
L1 = [randint(1,100) for i in range(100)]
print("This is L1", L1)

L2 = [L1[i] for i in range(100) if((L1[i]%4) == 0 or L1[i]%3 == 0)]
print("This is L2", L2)

S1 = [x for x in L1]
print("This is S1", S1)

S2 = [x for x in L2]
print("This is S2", S2)

for i in L1:
     R1.append(L1)
for i in L2:
     R1.append(L2)
print("The length of R1 is ", len(R1))

for i in range(len(L2)):
     for k in range(len(L1)):
          if L2[i] == L1[k]:
               R2.append(L2[i])       
print("The length of R2 is ", len(R2))

for i in L1[:]:
     if i in L2:
          L1.remove(i)   
for i in range(len(L1)):
     R3.append(L1[i])
print("The length of R3 is ", len(R3))

#Output for Task 2
# This is L1 [80, 60, 51, 81, 38, 44, 42, 67, 7, 99, 66, 35, 51, 34, 1, 60, 46, 95, 51, 45, 54, 20, 18, 19, 10, 59, 52, 66, 54, 35, 67, 92, 83, 75, 72, 27, 21, 31, 15, 48, 8, 96, 77, 30, 34, 55, 64, 45, 18, 54, 45, 27, 72, 15, 92, 32, 30, 79, 70, 54, 5, 75, 62, 85, 63, 10, 33, 31, 16, 86, 91, 63, 88, 12, 80, 63, 48, 79, 2, 100, 99, 43, 57, 18, 62, 66, 67, 35, 74, 59, 23, 40, 28, 37, 68, 53, 30, 70, 30, 41]
# This is L2 [80, 60, 51, 81, 44, 42, 99, 66, 51, 60, 51, 45, 54, 20, 18, 52, 66, 54, 92, 75, 72, 27, 21, 15, 48, 8, 96, 30, 64, 45, 18, 54, 45, 27, 72, 15, 92, 32, 30, 54, 75, 63, 33, 16, 63, 88, 12, 80, 63, 48, 100, 99, 57, 18, 66, 40, 28, 68, 30, 30]
# This is S1 [80, 60, 51, 81, 38, 44, 42, 67, 7, 99, 66, 35, 51, 34, 1, 60, 46, 95, 51, 45, 54, 20, 18, 19, 10, 59, 52, 66, 54, 35, 67, 92, 83, 75, 72, 27, 21, 31, 15, 48, 8, 96, 77, 30, 34, 55, 64, 45, 18, 54, 45, 27, 72, 15, 92, 32, 30, 79, 70, 54, 5, 75, 62, 85, 63, 10, 33, 31, 16, 86, 91, 63, 88, 12, 80, 63, 48, 79, 2, 100, 99, 43, 57, 18, 62, 66, 67, 35, 74, 59, 23, 40, 28, 37, 68, 53, 30, 70, 30, 41]
# This is S2 [80, 60, 51, 81, 44, 42, 99, 66, 51, 60, 51, 45, 54, 20, 18, 52, 66, 54, 92, 75, 72, 27, 21, 15, 48, 8, 96, 30, 64, 45, 18, 54, 45, 27, 72, 15, 92, 32, 30, 54, 75, 63, 33, 16, 63, 88, 12, 80, 63, 48, 100, 99, 57, 18, 66, 40, 28, 68, 30, 30]
# The length of R1 is  160
# The length of R2 is  132
# The length of R3 is  40