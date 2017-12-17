from tkinter import Tk, Canvas, mainloop, NW
from PIL import Image, ImageTk

window_width = 1200
window_height = 600

game_map = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

block_width = 50
block_height = 50

tk = Tk()
c = Canvas(tk, width=window_width, height=window_height, bg='white')
c.pack()

brick = ImageTk.PhotoImage((Image.open("brick.jpg").resize((block_width, block_height))))
grass = ImageTk.PhotoImage((Image.open("grass.jpg").resize((block_width, block_height))))

for i in range(20):
    for j in range(12):
        if game_map[i][j] == 0:
            c.create_image(i * block_width, j * block_height, image=grass, anchor=NW)
        if game_map[i][j] == 1:
            c.create_image(i * block_width, j * block_height, image=brick, anchor=NW)


player_image = ImageTk.PhotoImage((Image.open("brick.jpg").resize((block_width, block_height))))
speed_x = 0
speed_y = 0
x = 6
y = 1

player = c.create_image(x * block_width, y * block_height, image=player_image, anchor=NW)

def is_available(i, j):
    if i < 0 or i >= 550 or j < 0 or j >= 550:
        return False
    if game_map[i][j] == 1:
        return False
    return True

def PhysMove():
    global player, speed_y, speed_x
    x1, y1 = c.coords(player)
    if speed_x > 0:
        speed_x = speed_x - 1
        c.move(player, speed_x, speed_y)
    if speed_x < 0:
        speed_x = speed_x + 1
        c.move(player, speed_x, speed_y)
    if y1 >= 500:
        y1 = 450
        speed_y = 0
        c.move(player, speed_x, speed_y)
    elif y1 < 500:
        speed_y = speed_y + 5
        c.move(player, speed_x, speed_y)
    c.after(50, PhysMove)

def PhysKey(key):
    global player, speed_y, speed_x
    x1, y1 = c.coords(player)
    print("Хз что")
    if key.char == "d" and speed_x < 10:
        speed_x = speed_x + 5
        c.move(player, speed_x, speed_y)
        print("Чото игрик")
    if key.char == "a" and speed_x > -10:
        speed_x = speed_x - 5
        c.move(player, speed_x, speed_y)
        print("Какаха бдыщ")
    if key.char == "w" and speed_y == 0:
        speed_y = speed_y - 50
        print("Еще фигня")
        c.move(player, speed_x, speed_y)
        
c.after(50, PhysMove)    
tk.bind("<KeyPress>", PhysKey)
mainloop()
