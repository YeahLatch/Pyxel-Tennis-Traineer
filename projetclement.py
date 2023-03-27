import pyxel

pyxel.init(128, 128, title="Tennis trainner")
pyxel.load("4.pyxres")

u = 1
def bouge_balle():

    global x, y, vx, vy, score
    if x < 1:
        score -= 1
 
    if x < 1 or x > 127: 
        vx = - vx
    if y < 1 or y > 127:
        vy = - vy


    x = x + vx
    y = y + vy
    if score >= 10:
        u = 2
    if score >= 100:
        u = 3
        
    if score >= 200:
        u = 4
        
    if score >= 300:
        u = 6

def affiche_balle():

    pyxel.circ(x, y, 2, 8)



def update():
    bouge_vaisseau()
    vaisseau_suppression()
    bouge_balle()

def draw():
    global vaisseau_x,vaisseau_y,score
    pyxel.text(100,100,str(score), 4)
    pyxel.blt(0, 0, 0,32,0,128,128)
    pyxel.blt(vaisseau_x, vaisseau_y, 0,0,0,16,16)
    pyxel.text(90,0,"score:"+str(score), 8)
    affiche_balle()




def bouge_vaisseau():

    global vaisseau_x, vaisseau_y

    if pyxel.btn(pyxel.KEY_RIGHT): 
        if (vaisseau_x < 45) :
            vaisseau_x = vaisseau_x + 3
    if pyxel.btn(pyxel.KEY_LEFT):
        if (vaisseau_x > 0) :
            vaisseau_x = vaisseau_x - 3
    if pyxel.btn(pyxel.KEY_DOWN):
        if (vaisseau_y < 116) :
            vaisseau_y = vaisseau_y + 3
    if pyxel.btn(pyxel.KEY_UP):
        if (vaisseau_y > 0) :
            vaisseau_y = vaisseau_y - 3


def vaisseau_suppression():

    global vaisseau_x,vaisseau_y,x,y,vx,vy,score
    if x <= vaisseau_x+16  and y <= 16+vaisseau_y and x+16 >= vaisseau_x and vaisseau_y+16 >= y:
        vy= -vy
        vx = -vx
        score += 1
        x = 50
        y = 10



score = 0

x = 50
y = 10

vx = u
vy = u
vaisseau_x = 10
vaisseau_y = 10

pyxel.run(update, draw)