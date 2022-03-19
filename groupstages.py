import random
from tokenize import group

a, b, c, d, e, f, g, h = input('Enter 8 teams: \n').split()
list1 = [a, b, c, d, e, f, g, h]

print('Fixtures for the Quarter Finals\n\n')

group1 = random.sample(list1, 2)
print(f'{group1}\n')

newlist = [x for x in list1 if x not in group1]
group2 = random.sample(newlist, 2)
print(f'{group2}\n')

newlist2 = [x for x in newlist if x not in group2]
group3 = random.sample(newlist2, 2)
print(f'{group3}\n')

newlist3 = [x for x in newlist2 if x not in group3]
group4 = random.sample(newlist3, 2)
print(f'{group4}\n')

