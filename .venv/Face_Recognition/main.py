from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

#from elder_indentifind import elder


class Face_Recognition_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry('1530x790+0+0')
        self.root.title('Face Recognition System')

        # first image
        img = Image.open(r"D:\HAR\Human_acti\ToLearnBlockchain\.venv\image\images.jpg")
        img = img.resize((425,130),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0 , width=425, height=130)

        #second image
        img1 = Image.open(r"D:\HAR\Human_acti\ToLearnBlockchain\.venv\image\Human-Activity-Recognition-1-320.jpg")
        img1 = img1.resize((425, 130), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=425, y=0, width=425, height=130)

        # third image
        img2 = Image.open(r"D:\HAR\Human_acti\ToLearnBlockchain\.venv\image\end.jpg")
        img2 = img2.resize((425, 130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=850, y=0, width=425, height=130)

        # bg image
        img3 = Image.open(r"D:\HAR\Human_acti\ToLearnBlockchain\.venv\image\background.jpg")
        img3 = img3.resize((1275, 660), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1275, height=660)

        title_lbl = Label(bg_img, text="Face Recognition System",font=("Arial",35,"bold"),fg="black",bg="white")
        title_lbl.place(x=0, y=0, width=1275, height=45)

        # Hover effect
        def on_enter(e):
            b1['relief'] = 'sunken'

        def on_leave(e):
            b1['relief'] = 'raised'

        # button 1
        img4 = Image.open(r"D:\HAR\Human_acti\ToLearnBlockchain\.venv\image\end.jpg")
        img4 = img4.resize((200, 200), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)



        b1 = Button(bg_img, image=self.photoimg4 , cursor="hand2", borderwidth=0)
        b1.place(x=150, y=100, width=200, height=200)

        b1_1 = Button(bg_img, image=self.photoimg4, text="Human dicription", compound="center",
                    font=("Arial", 12, "bold"), fg="white", bg="darkblue",
                    cursor="hand2")
        b1_1.place(x=150, y=275, width=200, height=40)
        b1.bind("<Enter>", on_enter)
        b1.bind("<Leave>", on_leave)

        # detect face and activity button
        img5 = Image.open(r"D:\HAR\Human_acti\ToLearnBlockchain\.venv\image\end.jpg")
        img5 = img5.resize((200, 200), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, image=self.photoimg5, cursor="hand2", borderwidth=0)
        b1.place(x=400, y=100, width=200, height=200)

        b1_1 = Button(bg_img, image=self.photoimg5, text="detect face and activity", compound="center",font=("Arial", 12, "bold"),fg="white", bg="darkblue", cursor="hand2")
        b1_1.place(x=400, y=275, width=200, height=40)
        b1.bind("<Enter>", on_enter)
        b1.bind("<Leave>", on_leave)

        # detect face and activity button
        img5 = Image.open(r"D:\HAR\Human_acti\ToLearnBlockchain\.venv\image\end.jpg")
        img5 = img5.resize((200, 200), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, image=self.photoimg5, cursor="hand2", borderwidth=0)
        b1.place(x=400, y=100, width=200, height=200)

        b1_1 = Button(bg_img, image=self.photoimg5, text="detect face and activity", compound="center",
                      font=("Arial", 12, "bold"), fg="white", bg="darkblue", cursor="hand2")
        b1_1.place(x=400, y=275, width=200, height=40)
        b1.bind("<Enter>", on_enter)
        b1.bind("<Leave>", on_leave)

        # Attendance button
        img6 = Image.open(r"D:\HAR\Human_acti\ToLearnBlockchain\.venv\image\end.jpg")
        img6 = img6.resize((200, 200), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img, image=self.photoimg6, cursor="hand2", borderwidth=0)
        b1.place(x=650, y=100, width=200, height=200)

        b1_1 = Button(bg_img, image=self.photoimg6, text="detect face and activity", compound="center",
                      font=("Arial", 12, "bold"), fg="white", bg="darkblue", cursor="hand2")
        b1_1.place(x=650, y=275, width=200, height=40)
        b1.bind("<Enter>", on_enter)
        b1.bind("<Leave>", on_leave)

        # Help desk button
        img7 = Image.open(r"D:\HAR\Human_acti\ToLearnBlockchain\.venv\image\end.jpg")
        img7 = img7.resize((200, 200), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_img, image=self.photoimg7, cursor="hand2", borderwidth=0)
        b1.place(x=900, y=100, width=200, height=200)

        b1_1 = Button(bg_img, image=self.photoimg7, text="detect face and activity", compound="center",
                      font=("Arial", 12, "bold"), fg="white", bg="darkblue", cursor="hand2")
        b1_1.place(x=900, y=275, width=200, height=40)
        b1.bind("<Enter>", on_enter)
        b1.bind("<Leave>", on_leave)

        # train data
        img8 = Image.open(r"D:\HAR\Human_acti\ToLearnBlockchain\.venv\image\end.jpg")
        img8 = img8.resize((200, 200), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img, image=self.photoimg8, cursor="hand2", borderwidth=0)
        b1.place(x=150, y=350, width=200, height=200)

        b1_1 = Button(bg_img, image=self.photoimg8, text="Train Data", compound="center",
                      font=("Arial", 12, "bold"), fg="white", bg="darkblue",
                      cursor="hand2")
        b1_1.place(x=150, y=525, width=200, height=40)
        b1.bind("<Enter>", on_enter)
        b1.bind("<Leave>", on_leave)

        # Developer data
        img9 = Image.open(r"D:\HAR\Human_acti\ToLearnBlockchain\.venv\image\end.jpg")
        img9 = img9.resize((200, 200), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img, image=self.photoimg9, cursor="hand2", borderwidth=0)
        b1.place(x=400, y=350, width=200, height=200)

        b1_1 = Button(bg_img, image=self.photoimg9, text="Developer", compound="center",
                      font=("Arial", 12, "bold"), fg="white", bg="darkblue",
                      cursor="hand2")
        b1_1.place(x=400, y=525, width=200, height=40)
        b1.bind("<Enter>", on_enter)
        b1.bind("<Leave>", on_leave)

        # pohoto data
        img10 = Image.open(r"D:\HAR\Human_acti\ToLearnBlockchain\.venv\image\end.jpg")
        img10 = img10.resize((200, 200), Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1 = Button(bg_img, image=self.photoimg10, cursor="hand2", borderwidth=0)
        b1.place(x=650, y=350, width=200, height=200)

        b1_1 = Button(bg_img, image=self.photoimg10, text="Photo", compound="center",
                      font=("Arial", 12, "bold"), fg="white", bg="darkblue",
                      cursor="hand2")
        b1_1.place(x=650, y=525, width=200, height=40)
        b1.bind("<Enter>", on_enter)
        b1.bind("<Leave>", on_leave)

        # exit
        img11 = Image.open(r"D:\HAR\Human_acti\ToLearnBlockchain\.venv\image\end.jpg")
        img11 = img11.resize((200, 200), Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1 = Button(bg_img, image=self.photoimg11, cursor="hand2", borderwidth=0)
        b1.place(x=900, y=350, width=200, height=200)

        b1_1 = Button(bg_img, image=self.photoimg11, text="exit", compound="center",
                      font=("Arial", 12, "bold"), fg="white", bg="darkblue",
                      cursor="hand2")
        b1_1.place(x=900, y=525, width=200, height=40)
        b1.bind("<Enter>", on_enter)
        b1.bind("<Leave>", on_leave)


if __name__ == '__main__':
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
