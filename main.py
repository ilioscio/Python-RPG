from random import randint

from hero import hero
from bootGame import bootGame
from repl import repl

output = bootGame()

player = hero(output[0],100,20,output[2])

repl(player)
