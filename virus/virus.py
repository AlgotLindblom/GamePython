import os
import tkinter as tk
import random as rand

class Biden:
    root = tk.Tk()
    img = os.getcwd() + r"\img.gif"
    photo_image = tk.PhotoImage(file=img)
    frm = tk.ttk.Frame(root, padding=10)
    
    photo_img = photo_image
    frm.grid()
    top = rand.randint(0, 500)
    left = rand.randint(0, 800)
    root.geometry(f" 300x300 + {top} + {left}")
    label = tk.Label(root, photo_img)

    root.mainloop()
                
Biden()