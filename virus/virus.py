import os
import tkinter as tk
import random as rand

class Cat:
    root = tk.Tk()
    img = os.getcwd() + r"\cat.gif"
    print(img)
    photo_image = tk.PhotoImage(file=img)
    #frm = tk.Frame(root)
    
    photo_img = photo_image
    top = rand.randint(0, 400)
    left = rand.randint(0, 800)
    root.geometry('%dx%d+%d+%d' % (300, 300, top, left))
    label = tk.Label(root, image=photo_img)
    label.pack()

    root.mainloop()

    os.system('cmd /k "run.bat"')
Cat()