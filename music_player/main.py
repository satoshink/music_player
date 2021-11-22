# import import import import
from tkinter import *
import pygame
from tkinter import filedialog
from PIL import ImageTk, Image

# laying the foundations
pygame.init()
pygame.mixer.init()
root = Tk()
root.title("Music Player")
root.iconbitmap("textures/icon.ico")
root.configure(bg="white")


# declaring button functions
def start_song():
    song = song_box.get(ACTIVE)
    song = "music/{}".format(song)
    pygame.mixer.music.unload()
    try:
        pygame.mixer.music.load(song)
        pygame.mixer.music.play(loops=0)
    except:
        song_box.delete(ACTIVE)


def pause():
    pygame.mixer.music.pause()


def add_song():
    song = filedialog.askopenfilename(initialdir="music/", title="Add Song", filetypes=(("MP3 Files", "*.mp3"),))
    has_slashes = True

    while has_slashes:
        slash_index = song.find("/")
        print(slash_index)
        if slash_index != -1:
            song = song.replace(song[0:slash_index + 1], "")
            print(1)
        else:
            has_slashes = False
    if song == "":
        return
    else:
        song_box.insert(END, song)


def stop():
    pygame.mixer.music.stop()
    song_box.selection_clear(ACTIVE)
    pygame.mixer.music.unload()


def unpause():
    pygame.mixer.music.unpause()


# declaring Stuff
stop_image = ImageTk.PhotoImage(Image.open("textures/stop.png"))
start_song_image = ImageTk.PhotoImage(Image.open("textures/play.png"))
pause_image = ImageTk.PhotoImage(Image.open("textures/pause.png"))
unpause_image = ImageTk.PhotoImage(Image.open("textures/unpause.png"))
page_title = Label(root, text=" Welcome to Music Player ", bg="white")
page_title.config(font=("Calibri", 40))
other_text = Label(root, text="Music Files:", bg="white")
other_text.config(font=("Arial", 20))
play_button = Button(root, image=start_song_image, borderwidth=0, bg="white", command=start_song)
pause_button = Button(root, image=pause_image, borderwidth=0, bg="white", command=pause)
stop_button = Button(root, image=stop_image, borderwidth=0, bg="white", command=stop)
song_box = Listbox(root, bg="black", fg="white", width=60)
add_song_button = Button(root, text="Add Song", padx=50, borderwidth=0, bg="lime", fg="white", command=add_song)
unpause_button = Button(root, image=unpause_image, borderwidth=0, bg="white", command=unpause)
spacer_0 = Label(root, text="", bg="white")
spacer_1 = Label(root, text="", bg="white")
spacer_2 = Label(root, text="", bg="white")

# putting stuff on the screen
page_title.grid(row=0, column=0, columnspan=4)
other_text.grid(row=1, column=0, columnspan=4)
spacer_1.grid(row=2)
play_button.grid(row=3, column=0)
pause_button.grid(row=3, column=1)
unpause_button.grid(row=3, column=2)
stop_button.grid(row=3, column=3)
spacer_2.grid(row=4)
song_box.grid(row=5, column=0, columnspan=4)
add_song_button.grid(row=6, column=1, columnspan=2)
spacer_0.grid(row=7)

root.mainloop()
