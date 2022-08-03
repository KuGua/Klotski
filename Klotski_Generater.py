'''
Klotski：
Map size(wide * length)：4*5
block (number * size)：4*1，5*2，1*4

Size () represent as ()：
    4，1
    2，2
    1，3
    0，0

Mod for could use：
    numpy
    list

Example：
[[2,1,1,2],
 [2,1,1,2],
 [0,2,2,0],
 [2,3,3,2],
 [2,3,3,2]]

This file is Klotski generater
'''

import random
import numpy as np

Matrix = []

for number in range(0,5):
    row =[]
    Matrix.append(row)

# insert 2*2 blocks

a = random.randint(0,3)
b = random.randint(0,2)

for row in range(0,5):
    for number in range(0,4):
        Matrix[row].append(0)

Matrix[a][b] = 1
Matrix[a][b+1] = 1
Matrix[a+1][b] = 1
Matrix[a+1][b+1] = 1

# print("Inital:")
# print(Matrix,end='\n\n')

# insert 1*2 blocks
Avaliability = []

row = 0

for num_list in Matrix:
    num = 0
    for number in num_list:
        if number == 0:
            position = []
            position.append(row)
            position.append(num)
            Avaliability.append(position)
            num += 1
        
        else:
            num += 1
    row += 1

remain_Avaliability = Avaliability.copy()
unusable_position = []
identity = 0.1
label = 0

for trial in range(0,5):

    position_choices = []

    while position_choices == []:
        choice = random.choice(remain_Avaliability)

        if [choice[0] - 1, choice[1]] in remain_Avaliability:
            position_choices.append([choice[0] - 1, choice[1]])

        if [choice[0] + 1, choice[1]] in remain_Avaliability:
            position_choices.append([choice[0] + 1, choice[1]])

        if [choice[0], choice[1] - 1] in remain_Avaliability:
            position_choices.append([choice[0], choice[1] - 1])

        if [choice[0], choice[1] + 1] in remain_Avaliability:
            position_choices.append([choice[0], choice[1] + 1])

    conf_pos = random.choice(position_choices)

    Matrix[choice[0]][choice[1]] = 2 + identity
    Matrix[conf_pos[0]][conf_pos[1]] = 2 + identity

    remain_Avaliability.remove(choice)
    remain_Avaliability.remove(conf_pos)

    identity += 0.1

    # print("Choiced position:")
    # print(choice)
    # print("Near by avaliable positions:")
    # print(position_choices)
    # print("Choiced near by position:")
    # print(conf_pos,end='\n\n')

for trial in range(0,4):
    choice = random.choice(remain_Avaliability)
    Matrix[choice[0]][choice[1]] = 3
    remain_Avaliability.remove(choice)

# print("Final:")
# print(Matrix,end='\n\n')

print("Final Presentation:")
Final_Matrix = np.array(Matrix)
print(Final_Matrix)