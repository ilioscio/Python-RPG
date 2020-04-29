from random import randint

from hero import hero
from bootGame import bootGame

output = bootGame()

rstr = randint(1,10)
rdex = randint(1,10)
rint = randint(1,10)
rvit = randint(1,10)
print("Rolled random stats: {} str, {} dex, {} int, {} vit".format(rstr,rdex,rint,rvit))
player = hero(output[0],100,20,[rstr,rdex,rint,rvit])
print(player.name)
#        def __init__(self,name,maxhealth,maxmana,stats=[]):
