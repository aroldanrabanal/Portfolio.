from vpython import *
scene=canvas()
scene.title= 'Monografia'
scene.width = 640
scene.height = 400
scene.center = vector(0,0.5,0)
scene.forward = vector(-.3,0,-1)


omega=float(input ('Escriba el valor de omega (-2 a 2 rad/s)= '))
floor = box(length=54, height=0.1, width=30, color=color.green)
ball = sphere(pos=vector(0,0.3,0), radius=0.3, color=color.white, make_trail = True) #Objeto Pos = posicion del balon en x, y y z
poste = box(pos=vector(25.5,2,-4), length=0.2, height=4, width=0.2, color=color.white)
poste1 = box(pos=vector(25.5,2,4), length=0.2, height=4, width=0.2, color=color.white)
poste2 = box(pos=vector(27,4,0), length=0.2, height=0.2, width=8, color=color.white)
poste3 = box(pos=vector(26.4,4,-4), length=1.6, height=0.2, width=0.2, color=color.white)
poste4 = box(pos=vector(26.4,4,4), length=1.6, height=0.2, width=0.2, color=color.white)
poste5 = box(pos=vector(27,2,-4), length=0.2, height=4, width=0.2, color=color.white)
poste6 = box(pos=vector(27,2,4), length=0.2, height=4, width=0.2, color=color.white)
poste7 = box(pos=vector(25.5,4,0), length=0.2, height=0.2, width=8, color=color.white)
linea=box(pos=vector(0,0,-15), length=51.5, height=0.2, width=0.2, color=color.white)
linea1=box(pos=vector(0,0,15), length=51.5, height=0.2, width=0.2, color=color.white)
linea3=box(pos=vector(-20,0,0), length=0.2, height=0.2, width=30, color=color.white)
linea4=box(pos=vector(25.7,0,0), length=0.2, height=0.2, width=30, color=color.white)
Centro=ring(pos=vector(-20,0,0), radius=5.5, axis= vector(0,1,0), thickness=0.1)
Texto=label(pos=vector(25,10,15), text='Efecto Magnus', height=10, border=2, color = color.white)
guia=box(pos=vector(0,0,0), length=0.15, height=0.15, width=33, color=color.black)
guia1=box(pos=vector(0,0,0), length=56, height=0.15, width=0.15, color=color.black)
ejex=label(pos=vector(28,0,0), text='X', height=10, border=2, color = color.white)
ejez=label(pos=vector(0,0,16), text='Z', height=10, border=2, color = color.white)
g = 9.8 #Aceleracion debido a la gravedad m/s^2
gama = 0.02 #Friccion debida al aire
Cm = 0.2 #Constante de Magnus
ball.v = vector(10,10,0) #Velocidad inicial de objeto
ball.vw = vector(0,0,omega) #Velocidad angular
dt = 0.005
def fa (a, b, c, d, e, f):
    return -gama*sqrt(a*a+b*b+c*c)*a+Cm*(-omega*b)
def fb (a, b, c, d, e, f):
    return -gama*sqrt(a*a+b*b+c*c)*b +Cm*(omega*a)-g
def fc (a, b, c, d, e, f):
    return -gama*sqrt(a*a+b*b+c*c)*c
def fd (a, b, c, d, e, f):
    return a
def fe (a, b, c, d, e, f):
    return b
def ff (a, b, c, d, e, f):
    return c
def rK6 (a, b, c, d, e, f, fa, fb, fc, fd, fe, ff, hs):
    a1 = fa(a, b, c, d, e, f)*hs
    b1 = fb(a, b, c, d, e, f)*hs
    c1 = fc(a, b, c, d, e, f)*hs
    d1 = fd(a, b, c, d, e, f)*hs
    e1 = fe(a, b, c, d, e, f)*hs
    f1 = ff(a, b, c, d, e, f)*hs
    ak = a + a1*0.5
    bk = b + b1*0.5
    ck = c + c1*0.5
    dk = d + d1*0.5
    ek = e + e1*0.5
    fk = f + f1*0.5
    a2 = fa(ak, bk, ck, dk, ek, fk)*hs
    b2 = fb(ak, bk, ck, dk, ek, fk)*hs
    c2 = fc(ak, bk, ck, dk, ek, fk)*hs
    d2 = fd(ak, bk, ck, dk, ek, fk)*hs
    e2 = fe(ak, bk, ck, dk, ek, fk)*hs
    f2 = ff(ak, bk, ck, dk, ek, fk)*hs
    ak = a + a2*0.5
    bk = b + b2*0.5
    ck = c + c2*0.5
    dk = d + d2*0.5
    ek = e + e2*0.5
    fk = f + f2*0.5
    a3 = fa(ak, bk, ck, dk, ek, fk)*hs
    b3 = fb(ak, bk, ck, dk, ek, fk)*hs
    c3 = fc(ak, bk, ck, dk, ek, fk)*hs
    d3 = fd(ak, bk, ck, dk, ek, fk)*hs
    e3 = fe(ak, bk, ck, dk, ek, fk)*hs
    f3 = ff(ak, bk, ck, dk, ek, fk)*hs
    ak = a + a3
    bk = b + b3
    ck = c + c3
    dk = d + d3
    ek = e + e3
    fk = f + f3
    a4 = fa(ak, bk, ck, dk, ek, fk)*hs
    b4 = fb(ak, bk, ck, dk, ek, fk)*hs
    c4 = fc(ak, bk, ck, dk, ek, fk)*hs
    d4 = fd(ak, bk, ck, dk, ek, fk)*hs
    e4 = fe(ak, bk, ck, dk, ek, fk)*hs
    f4 = ff(ak, bk, ck, dk, ek, fk)*hs
    a = a + (a1 + 2*(a2 + a3) + a4)/6
    b = b + (b1 + 2*(b2 + b3) + b4)/6
    c = c + (c1 + 2*(c2 + c3) + c4)/6
    d = d + (d1 + 2*(d2 + d3) + d4)/6
    e = e + (e1 + 2*(e2 + e3) + e4)/6
    f = f + (f1 + 2*(f2 + f3) + f4)/6
    return a, b, c, d, e, f
while True:
    rate(25)


    #ball.v[0], ball.pos[0] = rK6(ball.v[0], ball.pos[0], fa, fb, fc, fd, fe, ff, dt)
    #ball.v[1], ball.pos[1] = rK6(ball.v[1], ball.pos[1], fa, fb, fc, fd, fe, ff, dt)
    #ball.v[2], ball.pos[2] = rK6(ball.v[2], ball.pos[2], fa, fb, fc, fd, fe, ff, dt)
    Rebote = rK6(ball.v[0],ball.v[1],ball.v[2],ball.pos[0],ball.pos[1],ball.pos[2], fa, fb, fc, fd, fe, ff, dt)
    ball.v[0],ball.v[1],ball.v[2],ball.pos[0],ball.pos[1],ball.pos[2] = Rebote
   
    # ball.v[0]= rK6(ball.v[0],fa, fb, fc, fd, fe, ff, dt)
    # ball.pos[0]=rK6(ball.pos[0], fa, fb, fc, fd, fe, ff, dt)
    # ball.v[1]= rK6(ball.v[1], fa, fb, fc, fd, fe, ff, dt)
    # ball.pos[1]= rK6(ball.pos[1], fa, fb, fc, fd, fe, ff, dt)
    # ball.v[2]= rK6(ball.v[2], fa, fb, fc, fd, fe, ff, dt)
    # ball.pos[2]= rK6(ball.pos[2], fa, fb, fc, fd, fe, ff, dt)
    
    if (ball.pos[1]<0.3):
        ball.v[1]=-ball.v[1]
    if (ball.pos[0]>26.5):
        break
    if (ball.pos[2]>15):
        break
    if (ball.pos[2]<-15):
        break
    if (ball.pos[1]<0.3):
        break
print (ball.pos)