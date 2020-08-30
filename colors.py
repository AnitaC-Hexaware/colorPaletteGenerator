from tkinter import *
import random

my_window = Tk()

h = input() #hex input

red = int(h[0:2],16) 
green = int(h[2:4],16)
blue = int(h[4:6],16) 

l=30 #limit or range

cl=[]
for _ in range(5):
    a = random.randint(-l, l)
    b = random.randint(-l, l)
    c = random.randint(-l, l)
    rr = red+a 
    gg = green+b
    bb = blue+c
    
    if rr<0: rr=-rr # -3 = 3
    if rr>255: rr=255-(rr-255) #257 = 253

    if gg<0: gg=-gg
    if gg>255: gg=255-(gg-255)

    if bb<0: bb=-bb
    if bb>255: bb=255-(bb-255)

    if rr>=0 and rr<16: #0 - f
        rr = '0' + hex(rr)[2:] #0xa = 0a
    else:
        rr = hex(rr)[2:] #0xaa = #aa
    if gg>=0 and gg<16:
        gg = '0' + hex(gg)[2:]
    else:
        gg = hex(gg)[2:]
    if bb>=0 and bb<16:
        bb = '0' + hex(bb)[2:]
    else:
        bb = hex(bb)[2:]
   
    color = rr+gg+bb
    cl.append('#'+color)


l0 = Label(my_window,width="100",height="3",bg='#'+h)
l01 = Label(my_window,width="20",height="1",bg='white')
l1 = Label(my_window,width="20",height="3",bg=cl[0])
l2 = Label(my_window,width="20",height="3",bg=cl[1])
l3 = Label(my_window,width="20",height="3",bg=cl[2])
l4 = Label(my_window,width="20",height="3",bg=cl[3])
l5 = Label(my_window,width="20",height="3",bg=cl[4])

l0.grid(row=0,columnspan=5)
l01.grid(row=1,column=0)
l1.grid(row=2,column=0)
l2.grid(row=2,column=1)
l3.grid(row=2,column=2)
l4.grid(row=2,column=3)
l5.grid(row=2,column=4)

# l0.grid(row=0,columnspan=5)
# l01.grid(row=1,column=0)
# l1.grid(row=2,column=0)
# l2.grid(row=2,column=1)
# l3.grid(row=2,column=2)
# l4.grid(row=2,column=3)
# l5.grid(row=2,column=4)

my_window.mainloop()

