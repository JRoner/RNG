import tkinter as tk
import random
import os
import sys

def on_button_click(): 
    try:
        x = random.randint(int(entry.get()), int(entry2.get()))
    except:
        x = 0
        
    HorT = random.randint(0,1)
    
    entry3.config(text= x)
    
    if(HorT == 0):{
        HTentry.config(text="Heads")
    }
    else:{
        HTentry.config(text="Tails")
    }
    
    

root = tk.Tk()
root.title("Random Number Generator")

# Function to get the path of the data (like images) in the bundled executable
def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

image_path = resource_path('dice.png')


from PIL import Image, ImageTk
img = Image.open(image_path)
tk_img = ImageTk.PhotoImage(img)

root.iconphoto(False, tk_img)

#root.geometry("")
#Height: 328 Width: 204

#Creating labels and entries, assigning them to root
label = tk.Label(root, text="Enter a Minimum:")
entry = tk.Entry(root)
label2 = tk.Label(root, text="Enter a Maximum:")
entry2 = tk.Entry(root)
label3 = tk.Label(root, text="Random Number:")
entry3 = tk.Label(root)
HTlabel = tk.Label(root, text="Heads or Tails:" )
HTentry = tk.Label(root)
button = tk.Button(root, text="Generate Number", command=on_button_click)


#create all the labels and entries: places them vertically
HTlabel.pack(padx = 40, pady=20)  
HTentry.pack(padx = 40, pady=10)
label.pack(padx = 40, pady=20)
entry.pack(padx = 40, pady=10)
label2.pack(padx = 40, pady=10)
entry2.pack(padx = 40, pady=10)
label3.pack(padx = 40, pady=10)
entry3.pack(padx = 40, pady=10)
button.pack(padx = 40, pady=10)

#grid layout for reference:
#label.grid(row=0, column=0, padx=10, pady=10)
#entry.grid(row=0, column=1, padx=10, pady=10)
#label2.grid(row=1, column=0, padx=10, pady=10)
#entry2.grid(row=1, column=1, padx=10, pady=10)
#label3.grid(row=2, column=0, padx=10, pady=10)
#entry3.grid(row=2, column=1, padx=10, pady=10)
#button.grid(row=3, column=0, columnspan=2, pady=10) 

root.mainloop()