from http.client import UnimplementedFileMode
import random

u = 'United'
m = 'madrid'
c = 'chelsea'
b = 'barcelona'
mc = 'man city'
l = 'liverpool'
bm = 'bayern munich'
j = 'juventus' 

def play():
    user = input("Choose your team: united, madrid, chelsea, barcelona, 'mc' for man city, liverpool, bayern munich and juventus\n")
    if input =='united':
        user = u
    elif input =='madrid':
        user = m
    elif input =='chelsea':
        user = c
    elif input =='barcelona':
        user = b
    elif input =='man city':
        user = mc
    elif input =='liverpool':
        user = l
    elif input =='bayern munich':
        user = bm
    elif input =='juventus':
        user = j
    computer = random.choice([u, m, c, b, mc, l, bm, j])
    
    return(f'{user} vs {computer}')

print(play())