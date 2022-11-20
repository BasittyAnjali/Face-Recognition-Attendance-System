from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognisation System")

        title_lbl = Label(self.root, text="Help Disk", font=("times new roman", 35, "bold"), bg="white", fg="navyblue")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # firstimage
        img_top = Image.open(r"college_images\16.jpeg")
        img_top = img_top.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        # set image as lable
        f_lb1 = Label(self.root, image=self.photoimg_top)
        f_lb1.place(x=0, y=55, width=1530, height=720)

        dev_label = Label(f_lb1, text="Email: basittyanjali11200@gmail.com", font=("times new roman", 20, "bold"), bg="white")
        dev_label.place(x=550, y=220)


if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()