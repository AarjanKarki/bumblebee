import pgzrun, random
HEIGHT=500
WIDTH=500
bee=Actor('bee')
bee.pos=100,100
flower=Actor('flower')


def draw():
    screen.blit('background',(0,0))
    bee.draw()
    flower.draw()








pgzrun.go()

