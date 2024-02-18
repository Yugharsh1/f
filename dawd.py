from tkinter import*
import random
root=Tk()
root.geometry("600x400")

dictionary = {"Color": ["maroon1","lawn green","magenta2","purple1","springgreen2","chocolate1",
"deep pink","cyan"]}

def bg_color():
    random_color=random.randint(0, 7)
    print(dictionary["Color"][random_color])
    root.configure(background=dictionary["Color"][random_color])
    
btn = Button(root, text="Click to change the background color!", command=bg_color)
btn.place(relx=0.5,rely=0.5,anchor=CENTER)

root.mainloop()
    
