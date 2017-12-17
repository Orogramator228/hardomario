from tkinter import Tk, Canvas, mainloop, NW
from PIL import Image, ImageTk

window_width = 1000
window_height = 600

game_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 2],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 2],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 2],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 2],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 2],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

block_width = 50
block_height = 50

tk = Tk()
c = Canvas(tk, width=window_width, height=window_height, bg='cyan')
c.pack()

brick = ImageTk.PhotoImage((Image.open("brick.jpg").resize((block_width, block_height))))
#grass = ImageTk.PhotoImage((Image.open("grass.jpg").resize((block_width, block_height))))
water = ImageTk.PhotoImage((Image.open("water.jpg").resize((block_width, block_height))))

ww = []
wh = []

for i in range(20):
    for j in range(12):
        '''if game_map[i][j] == 0:
            c.create_image(i * block_width, j * block_height, image=grass, anchor=NW)'''
        if game_map[i][j] == 1:
            c.create_image(i * block_width, j * block_height, image=brick, anchor=NW)
            ww.append(i * block_width)
            wh.append(j * block_height)

        if game_map[i][j] == 2:
            c.create_image(i * block_width, j * block_height, image=water, anchor=NW)
            ww.append(i * block_width)
            wh.append(j * block_height)
print(len(ww))
print(len(wh))
player_image = ImageTk.PhotoImage((Image.open("player.jpg").resize((block_width, block_height))))
speed_x = 0
speed_y = 0
x = 6
y = 1

player = c.create_image(x * block_width, y * block_height, image=player_image, anchor=NW)

def is_available(i, j):
    if i < 0 or i >= 900 or j < 0 or j >= 600:
        return False
#    for a in range(0, 57):
#        if i == ww[a] or i + 50 == ww[a] or j == wh[a] or j + 50 == wh[a]:
#            return False
    return True

def PhysMove():
    global player, speed_y, speed_x
    x1, y1 = c.coords(player)
    if speed_x > 0:
        speed_x = speed_x - 1
        if is_available(x1, y1):
            c.move(player, speed_x, speed_y)
    if speed_x < 0:
        speed_x = speed_x + 1
        c.move(player, speed_x, speed_y)
    if is_available(x1, y1+100):
        speed_y = speed_y +5
        c.move(player,  speed_x, speed_y)
    else:
        speed_y = 0
        y1 = 600
        c.move(player, speed_x, speed_y)
    if x1 < 50:
        speed_x = 0
    c.after(50, PhysMove)

def PhysKey(key):
    global player, speed_y, speed_x
    print("с.coords")
    x1, y1 = c.coords(player)
    if key.char == "d" and speed_x < 10 and is_available(x1+50, y1):
       speed_x = speed_x + 10
       c.move(player, speed_x, speed_y)
       print("right")
    if key.char == "a" and speed_x > -10 and is_available(x1-50, y1):
        speed_x = speed_x - 10
        c.move(player, speed_x, speed_y)
        print("left")
    if key.char == " "   and speed_y == 0:
        speed_y = speed_y - 40
        print("space")
        c.move(player, speed_x, speed_y)

    
        
c.after(50, PhysMove)    
tk.bind("<KeyPress>", PhysKey)
mainloop()

