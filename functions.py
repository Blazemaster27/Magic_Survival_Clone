from gamedata import *
from objects import *

def checkMovement(direct, event):
    if event.type == pg.KEYDOWN:
        if event.key == pg.K_RIGHT:
            direct.append("right")
        if event.key == pg.K_LEFT:
            direct.append("left")
        if event.key == pg.K_DOWN:
            direct.append("down")
        if event.key == pg.K_UP:
            direct.append("up")
    try:
        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT:
                direct.remove("left")
            if event.key == pg.K_RIGHT:
                direct.remove("right")
            if event.key == pg.K_UP:
                direct.remove("up")
            if event.key == pg.K_DOWN:
                direct.remove("down")
    except:
        pass
    return direct

def spawnObj(objType, props=[]):
    if objType=="enemy":
        xl0, yl0, xh0, yh0 = e_xmin, e_ymin, e_xmax, e_ymax
        xl1, yl1, xh1, yh1 = xmin, ymin, xmax, ymax
    if objType=="mana item" or "chest":
        xl0, yl0, xh0, yh0 = fs_xmin, fs_ymin, fs_xmax, fs_ymax
        xl1, yl1, xh1, yh1 = fr_xmin, fr_ymin, fr_xmax, fr_ymax
        rarity = rd.randint(1,100)
        rarity = "small" if rarity < 51 else "medium" if rarity < 91 else "large"
    x1, y1 = rd.randint(xl0, xl1), rd.randint(yl0, yl1)
    x2, y2 = rd.randint(xh1, xh0), rd.randint(yh1, yh0)
    x = rd.randint(1,2)
    y = rd.randint(1,2)
    z = rd.choice([True, False])
    if z:
        x = x1 if x==1 else x2
        y = rd.randint(yl0, yh0)
    else:
        x = rd.randint(xl0, xh0)
        y = y1 if y==1 else y2
    pos = [x,y]
    if objType=="enemy":
        return Enemy(pos, props[0], props[1], props[2], props[3], gameSpeed)
    if objType=="mana item":
        return Mana(pos, rarity, props[0], gameSpeed)
    if objType=="chest":
        return Background(pos, "chest.png", gameSpeed)
    if objType=="projectile":
        return Projectile(props[0], props[1], props[2], props[3], props[4], gameSpeed)

def boxCollision(obj1, obj2):
    X1 = obj1.hitbox[1][0] < obj2.hitbox[0][0]
    X2 = obj1.hitbox[0][0] > obj2.hitbox[1][0]
    Y1 = obj1.hitbox[1][1] < obj2.hitbox[0][1]
    Y2 = obj1.hitbox[0][1] > obj2.hitbox[1][1]
    col = not(X1 or X2) and not(Y1 or Y2)
    return col

def inBox(point, box):
    return (point[0]>box[0][0] and point[0]<box[1][0]) and (point[1]>box[0][1] and point[1]<box[1][1])

def ballCollision(obj1, obj2):
    distance = m.sqrt(m.pow(obj1.center[0]-obj2.center[0],2)+m.pow(obj1.center[1]-obj2.center[1],2))
    return distance < obj1.rad

if __name__ == "__main__": pass