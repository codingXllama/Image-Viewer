from tkinter import *
# Importing Python Image Library
from PIL import ImageTk,Image

from PIL import ImageTk, Image

window =Tk()
window.title("Nature Image Viewer")
# window.geometry("800x600")
# logo=PhotoImage(file="x.xbm")
logo= window.iconbitmap("@/home/x/Documents/GithubFiles/Image Viewer App /x.xbm")
# window.call('wm','iconphoto',window._w,logo)


img1=ImageTk.PhotoImage(Image.open("images/bg1.jpg"))
img2=ImageTk.PhotoImage(Image.open("images/bg2.jpg"))
img3=ImageTk.PhotoImage(Image.open("images/bg3.jpg"))
img4=ImageTk.PhotoImage(Image.open("images/bg4.jpg"))
img5=ImageTk.PhotoImage(Image.open("images/bg5.jpg"))

# Creating image list to store all images
bgImageCollection=[img1,img2,img3,img4,img5]
myImg1_Label=Label(image=img1)
myImg1_Label.grid(row=0,column=0,columnspan=3)



















# Creating Buttons
backBtn=Button(window,text="<<",bg="cyan")
exitBtn = Button(window, text="Exit Program",command=window.quit, bg="red")
forwardBtn=Button(window,text=">>", bg="green")


# Adding the Button onto the window
backBtn.grid(row=1,column=0)
exitBtn.grid(row=1,column=1)
forwardBtn.grid(row=1,column=2)


mainloop()