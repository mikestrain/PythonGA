import os
import pygame
import tkinter as tk
from tkinter.filedialog import askdirectory
# lets initalize the music mixer here. Why not
pygame.mixer.init()
# I am using Tkinter askdirectory function. Tkinter auto opens a window on your computer and this hides that window. Keep it clean.
root = tk.Tk()
root.withdraw()

# clears the screen, let's start fresh
os.system("clear")

# this class controls the menu for the music player function
class menu_buttons:
    def __init__(self, track=""):
        self.track = track
    
    def stop(self):
        pygame.mixer.music.stop()
    
    def next_track(self):
        pygame.mixer.music.stop()
        print("\n..............................\n")
        print(f"\n Playing the track\n \n {self.track}")
        print("\n..............................\n")
    def last_track(self):
        pygame.mixer.music.stop()
        print("\n..............................\n")
        print(f"\n Playing the track\n \n {self.track}")
        print("\n..............................\n")
    
    def restart(self):
        pygame.mixer.music.rewind()
        print("\n..............................\n")
        print(f"\n Restarting the track\n \n {self.track}")
        print("\n..............................\n")
    
    def pause(self):
        pygame.mixer.music.pause()
        print("\n..............................\n")
        print("\nThe music is paused\n")
        print("\n..............................\n")
    
    def unpause(self):
        pygame.mixer.music.unpause() 
        print("\n..............................\n")
        print("\nPlaying...\n")
        print("\n..............................\n")

# Here is the music player function
def music_player():
# Welcome message
    print("\nWELCOME TO ADAM'S MUSIC PLAYER!\n")
    print("\nplease choose a folder containing music files\n")
# this uses Tkinter askdirectory to open a directory chooser window. Then we change working directory to that directory. List the contents in a sorted order. Then prints it.
    directory = askdirectory()
    os.chdir(directory)
    list_dir = os.listdir(directory)
    list_dir.sort()
    print(f"\n{directory}\n")
    print("\nHere is an available track listing\n")

# Here we are making a list of songs in our working directory. Only mp3 files are going to be added to this list.
    list_of_songs = []
    for files in list_dir:
        if files.endswith(".mp3"):
            list_of_songs.append(files)
            print(files)
# Asks user what track they want to hear.
    track_num = int(input("\nWhat track do you want to play?: "))
    
# Lets start this music player in a while loop.
    another_track = ""
    while another_track != "s":
# some files cause a pygame error. This try/except keeps the program from crashing.       
        try:
# Here is where most of the action is. button gets the menu_button class going.
            button = menu_buttons()
# stop the player just in case. Then initalizing it again. print the track selected then plays it. lets you know it's playing then open up menu options.
            pygame.mixer.music.stop()
            pygame.mixer.init()
            print("\n..............................\n")
            print(f"{list_of_songs[int(track_num)-1]}")
            pygame.mixer.music.load(list_of_songs[int(track_num)-1])
            pygame.mixer.music.play()
            print("\nPlaying...")
            another_track = input("""\na to pick another track\n \ns to stop the program\n \n> to go to next track\n \n< to go to track before this one\n 
r to restart song\n \np to pause the music\n \nu to unpause the music\n \n""")
        
# Here are all the menu option (pick another track, stop program, next track, previous track, restart current track, pause and un-pause) each option reopens menu options again.
            if another_track == "a":
                track_num = int(input("\nWhat track do you want to play?: "))
            if another_track == "s":
                button.stop()
            if another_track == ">":
                button = menu_buttons(track=str(list_of_songs[int(track_num)]))
                track_num += 1
                button.next_track()
                
            if another_track == "<":
                button = menu_buttons(track=str(list_of_songs[int(track_num)-2]))
                track_num -= 1
                button.last_track()
                
            if another_track == "r":
                button = menu_buttons(track=str(list_of_songs[int(track_num)-1]))
                print("\n..............................\n")
                print(f"\nRestarting the track\n")
                print("\n..............................\n")
            while another_track == "p":
                button.pause()
                another_track = input("""\na to pick another track\n \ns to stop the program\n \n> to go to next track\n \n< to go to track before this one\n 
r to restart song\n \np to pause the music\n \nu to unpause the music\n \n""")
                if another_track == "u":
                    button.unpause()
                    another_track = input("""\na to pick another track\n \ns to stop the program\n \n> to go to next track\n \n< to go to track before this one\n 
r to restart song\n \np to pause the music\n \nu to unpause the music\n \n""")
                if another_track == ">":
					button = menu_buttons(track=str(list_of_songs[int(track_num)]))
					track_num += 1
					button.next_track()
                if another_track == "<":
					button = menu_buttons(track=str(list_of_songs[int(track_num)-2]))
					track_num -= 1
					button.last_track()
            
                
# Here are some errors that came up while testing. I bet there are more but I found these.           
        except pygame.error:
            print("\n..............................\n")
            print("\nsorry, something is wrong with that file.\n")
            print("\nI will play the next song\n")
            print("\n..............................\n")
            
            track_num += 1
            track_num = int(track_num)
        except IndexError:
            print("\n..............................\n")
            print("\nThat is not a valid track number\n")
            print("\n..............................\n")
            track_num = int(input("\nWhat track do you want to play?: "))

# Here we run the music function.
music_player()

# Goodbye message when program is stopped.
print("\n..............................\n")
print("\nGoodbye! Thanks for listening!\n")
print("\n..............................\n")

# There are a few bugs but pretty happy with how it turned out. 
# I tried using default input values to auto play next tracks but asking for user input stops the grogram until you enter something.