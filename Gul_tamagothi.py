from tkinter import *
from tkinter import messagebox as msgbox
from PIL import Image, ImageTk
from time import *
import os
from winsound import *



# Lose parameters
def lose_par():
    check_eat()
    check_sleep()
    check_play()

    # Using try-expect to open fiels
    # And checking if pars < 0 (same as death)


def check_eat():
    try:
        with open('last_eat_time.txt', 'r') as file:
            last_eat_time = int(file.read())
    except:
        last_eat_time = time()

    elapsed_time = time() - last_eat_time
    life = int(elapsed_time)
    if life < 0:
        msgbox.showerror(title="Гуль сдох", message="Вы не кромили его 12 часов")
        os.remove("last_eat_time.txt")


def check_sleep():
    try:
        with open('last_sleep_time.txt', 'r') as file:
            last_sleep_time = int(file.read())
    except:
        last_sleep_time = time()

    elapsed_time = time() - last_sleep_time
    life = int(elapsed_time)
    if life < 0:
        msgbox.showerror(title="Гуль сдох", message="Вы не ложили его спать 12 часов")
        os.remove("last_sleep_time.txt")


def check_play():
    try:
        with open('last_play_time.txt', 'r') as file:
            last_play_time = int(file.read())
    except:
        last_play_time = time()

    elapsed_time = time() - last_play_time
    life = int(elapsed_time)
    if life < 0:
        msgbox.showerror(title="Гуль сдох", message="Вы не играли с ним 12 часов")
        os.remove("last_play_time.txt")


# Buttons
def eat_button():
    last_eat_time = time()
    with open('last_eat_time.txt', 'w') as file:
        file.write(str(last_eat_time))
    PlaySound("eat_sound.wav", SND_ASYNC)

def sleep_button():
    last_sleep_time = time()
    with open('last_sleep_time.txt', 'w') as file:
        file.write(str(last_sleep_time))
    PlaySound("sleep_sound.wav", SND_ASYNC)

def play_button():
    last_play_time = time()
    with open('last_play_time.txt', 'w') as file:
        file.write(str(last_play_time))
    PlaySound("play_sound.wav", SND_ASYNC)


# GUI
game = Tk()
game.title("Гуль тамогочи")

gul_true_kaneki = Image.open("gul.PNG")
gul_true_kaneki_1 = gul_true_kaneki.resize((720, 500), Image.ANTIALIAS)
gul_true_kaneki_show = ImageTk.PhotoImage(gul_true_kaneki_1)

Label(game, image=gul_true_kaneki_show).pack()
Button(game, text='Кормить(Людьими)', width=100, height=5, command=eat_button).pack()
Button(game, text='Спать', width=100, height=5, command=sleep_button).pack()
Button(game, text='Играть(С костями)', height=5, width=100, command=play_button).pack()

game.after(60000, lose_par)

mainloop()
