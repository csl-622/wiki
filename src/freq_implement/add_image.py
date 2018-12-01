from PIL import Image, ImageTk 
import tkinter as tk 

root = tk.Tk()
img = Image.open("ico.png")
tkimage = ImageTk.PhotoImage(img)
tk.Label(root, image=tkimage).pack()
root.mainloop()
