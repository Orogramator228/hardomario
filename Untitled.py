from tkinter import Tk, Canvas, mainloop, NW
from PIL import Image, ImageTk

# размер карты в пикселях
window_width = 600
window_height = 600

# карта
game_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1]
]

# размеры блока
block_width = window_width // 12
block_height = window_height // 12

# создаем холст
tk = Tk()
c = Canvas(tk, width=window_width, height=window_height, bg='white')
c.pack()

# картинки со стеной и травой
brick = ImageTk.PhotoImage((Image.open("brick.jpg").resize((block_width, block_height))))
grass = ImageTk.PhotoImage((Image.open("grass.jpg").resize((block_width, block_height))))



# картинка с игроком
player_image = ImageTk.PhotoImage((Image.open("gameplay.gif").resize((block_width, block_height))))

# координаты игрока
x = 6
y = 6


direct = [0, 0]

def draw():
    # рисуем карту
    global game_map, c, grass, brick, block_width, block_height, window_width, window_height,player_image, player
    for i in range(12):
        for j in range(12):
            if game_map[i][j] == 0:
                c.create_image(i * block_width, j * block_height, image=grass, anchor=NW)
            if game_map[i][j] == 1:
                c.create_image(i * block_width, j * block_height, image=brick, anchor=NW)

            
    # создаем игрока
    player = c.create_image(x * block_width, y * block_height, image=player_image, anchor=NW)
  

# проверка доступности клетки
def is_available(i, j):
    global game_map
    if i < 0 or i >= 12 or j < 0 or j >= 12:
        return False
    if game_map[i][j] == 1:
        return False
    return True

# нажатие клавиши
def keyDown(key):
    global x, y, player, direct, game_map
    if key.char == 'a':
        if is_available(x - 1, y):
            x -= 1
            direct = [-1, 0]
    if key.char == 'd':
        if is_available(x + 1, y):
            x += 1
            direct = [1, 0]
    if key.char == 'w':
        if is_available(x, y - 1):
            y -= 1
            direct = [0, -1]
    if key.char == 's':
        if is_available(x, y + 1):
            y += 1
            direct = [0, 1]
    if key.char == ' ':
        if is_available(x, y + 1):
            y -= 2

    if key.char == 'e':
        if game_map[x + direct[0]][y + direct[1]]:
            game_map[x + direct[0]][y + direct[1]] = 0
            
    c.coords(player, x * block_width, y * block_height)
    draw()
# при нажатии любой клавишы вызываем keyDown
tk.bind("<KeyPress>", keyDown)
draw()

mainloop()

