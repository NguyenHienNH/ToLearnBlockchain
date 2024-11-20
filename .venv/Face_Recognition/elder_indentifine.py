from linecache import cache
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk



class elder:
    def __init__(self,root):
        self.root = root
        self.root.geometry('1530x790+0+0')
        self.root.title('Face Recognition System')

        # first image
        img = Image.open(r"D:\HAR\Human_acti\ToLearnBlockchain\.venv\image\images.jpg")
        img = img.resize((425, 130), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=425, height=130)

        # second image
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

        title_lbl = Label(bg_img, text="Elder Management System", font=("Arial", 35, "bold"), fg="black", bg="white")
        title_lbl.place(x=0, y=0, width=1275, height=45)



        main_frame = Frame(bg_img, bd = 2)
        main_frame.place(x=5, y=50, width=1260, height=605)

        left_frame = LabelFrame(main_frame, bd = 2, relief=RIDGE, text="Elder Details", font=("Arial", 15, "bold"))
        left_frame.place(x=5, y=5, width=630, height=525)

        # left label Frame
        '''img_left = Image.open(r"D:\HAR\Human_acti\ToLearnBlockchain\.venv\image\end.jpg")
        img_left = img_left.resize((425, 130), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)'''
        # curent left

        current_frame = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE, text="Elder Information",font=("Arial", 13, "bold"))
        current_frame.place(x=5, y=5, width=615, height=150)

        #dep_label
        dep_label = Label(current_frame, text="Department", font=("Arial", 11, "bold"))
        dep_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        dep_combo = ttk.Combobox(current_frame,font=("Arial", 11, "bold"),width=16)
        dep_combo["values"] =("select Deparment", "computer", "IT", "Engineer")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=5, pady=15, sticky=W)

        # year_label
        year_label = Label(current_frame, text="Year", font=("Arial", 11, "bold"))
        year_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)

        year_combo = ttk.Combobox(current_frame, font=("Arial", 11, "bold"), width=16)
        year_combo["values"] = ("select Year", "2024-25", "2025-26", "2026-27")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=5, pady=10, sticky=W)

        # course_label
        Caregiver_label = Label(current_frame, text="Caregiver", font=("Arial", 11, "bold"))
        Caregiver_label.grid(row=0, column=3, padx=25, pady=15, sticky=W)

        Caregiver_combo = ttk.Combobox(current_frame, font=("Arial", 11, "bold"), width=16)
        Caregiver_combo["values"] = ("select Caregiver", "1", "2", "3","4","5")
        Caregiver_combo.current(0)
        Caregiver_combo.grid(row=0, column=4, padx=5, pady=10, sticky=W)
        # semester_label
        quarter_label = Label(current_frame, text="Quarter", font=("Arial", 11, "bold"))
        quarter_label.grid(row=1, column=3, padx=25, pady=15, sticky=W)

        quarter_combo = ttk.Combobox(current_frame, font=("Arial", 11, "bold"), width=16)
        quarter_combo["values"] = ("select Semester", "quarter_1", "quarter_2","quarter_3","quarter_4")
        quarter_combo.current(0)
        quarter_combo.grid(row=1, column=4, padx=5, pady=10, sticky=W)


        # class Elder frame
        class_elder_frame = LabelFrame(left_frame,bd=2,bg = "white",text="Class elder Information", font=("Arial", 13, "bold"))
        class_elder_frame.place(x=5, y=160, width=615, height=225)

        # Id
        ElderID_label = Label(class_elder_frame, text="Elder ID:", font=("Arial", 11, "bold"))
        ElderID_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        eldelID_entry = ttk.Entry(class_elder_frame, font=("Arial", 11, "bold"),width=16)
        eldelID_entry.grid(row=0, column=1, padx=25, pady=5, sticky=W)

        # Name
        ElderName_label = Label(class_elder_frame, text="Elder Name:", font=("Arial", 11, "bold"))
        ElderName_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)

        eldelName_entry = ttk.Entry(class_elder_frame, font=("Arial", 11, "bold"), width=16)
        eldelName_entry.grid(row=1, column=1, padx=25, pady=5, sticky=W)

        # gender
        Eldergender_label = Label(class_elder_frame, text="Gender:", font=("Arial", 11, "bold"))
        Eldergender_label.grid(row=2, column=0, padx=5, pady=5, sticky=W)

        eldelgender_entry = ttk.Entry(class_elder_frame, font=("Arial", 11, "bold"), width=16)
        eldelgender_entry.grid(row=2, column=1, padx=25, pady=5, sticky=W)

        # health _ condition
        Elderhealth_label = Label(class_elder_frame, text="Health Condition:", font=("Arial", 11, "bold"))
        Elderhealth_label.grid(row=3, column=0, padx=5, pady=5, sticky=W)

        elderhealth_entry = ttk.Entry(class_elder_frame, font=("Arial", 11, "bold"), width=16)
        elderhealth_entry.grid(row=3, column=1, padx=25, pady=5, sticky=W)

        # Personal_note
        Eldernote_label = Label(class_elder_frame, text="Personal Notes", font=("Arial", 11, "bold"))
        Eldernote_label.grid(row=4, column=0, padx=5, pady=5, sticky=W)

        eldernote_entry = ttk.Entry(class_elder_frame, font=("Arial", 11, "bold"), width=16)
        eldernote_entry.grid(row=4, column=1, padx=25, pady=5, sticky=W)
        # mail
        ElderMail_label = Label(class_elder_frame, text="Mail:", font=("Arial", 11, "bold"))
        ElderMail_label.grid(row=0, column=3, padx=5, pady=5, sticky=W)

        elderMail_entry = ttk.Entry(class_elder_frame, font=("Arial", 11, "bold"), width=16)
        elderMail_entry.grid(row=0, column=4, padx=25, pady=5, sticky=W)

        # emergency contract
        Elderphone_label = Label(class_elder_frame, text="Phone:", font=("Arial", 11, "bold"))
        Elderphone_label.grid(row=1, column=3, padx=5, pady=5, sticky=W)

        elderphone_entry = ttk.Entry(class_elder_frame, font=("Arial", 11, "bold"), width=16)
        elderphone_entry.grid(row=1, column=4, padx=25, pady=5, sticky=W)
        #  admission date
        Elderdate_label = Label(class_elder_frame, text="Admission Date", font=("Arial", 11, "bold"))
        Elderdate_label.grid(row=2, column=3, padx=5, pady=5, sticky=W)

        elderdate_entry = ttk.Entry(class_elder_frame, font=("Arial", 11, "bold"), width=16)
        elderdate_entry.grid(row=2, column=4, padx=25, pady=5, sticky=W)

        #  Address
        ElderAddress_label = Label(class_elder_frame, text="Address", font=("Arial", 11, "bold"))
        ElderAddress_label.grid(row=3, column=3, padx=5, pady=5, sticky=W)

        elderAddress_entry = ttk.Entry(class_elder_frame, font=("Arial", 11, "bold"), width=16)
        elderAddress_entry.grid(row=3, column=4, padx=25, pady=5, sticky=W)

        #  DOB
        ElderDOB_label = Label(class_elder_frame, text="DOB", font=("Arial", 11, "bold"))
        ElderDOB_label.grid(row=4, column=3, padx=5, pady=5, sticky=W)

        elderDob_entry = ttk.Entry(class_elder_frame, font=("Arial", 11, "bold"), width=16)
        elderDob_entry.grid(row=4, column=4, padx=25, pady=5, sticky=W)

        # radio button
        radion_btn1 = ttk.Radiobutton(class_elder_frame, text="Take photo sample", value="yes")
        radion_btn1.grid(row=5, column=0, padx=5, pady=5, sticky=W)

        # radio button
        radion_btn2 = ttk.Radiobutton(class_elder_frame, text="No photo sample", value="no")
        radion_btn2.grid(row=5, column=3, padx=5, pady=5, sticky=W)


        # button FRame
        button_frame = Frame(left_frame,bd=2, relief=RAISED,bg = "white")
        button_frame.place(x = 5,y = 395, width = 615, height = 100)

        # save button
        save_btn =Button(button_frame, text="Save", width=14, font=("Arial", 11, "bold"),fg="white", bg="darkblue")
        save_btn.grid(row = 0, column = 0, padx=5, pady=5, sticky=W)
        # update button
        update_btn = Button(button_frame, text="Update", width=14, font=("Arial", 11, "bold"), fg="white", bg="darkblue")
        update_btn.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        # delete button
        delete_btn = Button(button_frame, text="Delete", width=14, font=("Arial", 11, "bold"), fg="white",
                            bg="darkblue")
        delete_btn.grid(row=0, column=2, padx=5, pady=5, sticky=W)

        # Reset  button
        reset_btn = Button(button_frame, text="Reset", width=14, font=("Arial", 11, "bold"), fg="white",
                            bg="darkblue")
        reset_btn.grid(row=0, column=3, padx=5, pady=5, sticky=W)



        # take photo
        takephoto_btn = Button(button_frame, text="Take photo Sample", width=14, font=("Arial", 11, "bold"), fg="white",
                           bg="darkblue")
        takephoto_btn.grid(row=1, column=0, padx=5, pady=5, sticky=W)
        #update
        updatephoto_btn = Button(button_frame, text="Update Photo Sample ", width=14, font=("Arial", 11, "bold"), fg="white",
                               bg="darkblue")
        updatephoto_btn.grid(row=1, column=2, padx=5, pady=5, sticky=W)



        # right frame
        right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Elder Details", font=("Arial", 15, "bold"))
        right_frame.place(x=640, y=5, width=610, height=525)

        Search_frame = LabelFrame(right_frame, bd=2, bg="white", relief=RIDGE, text="Search System",
                                   font=("Arial", 13, "bold"))
        Search_frame.place(x=5, y=5, width=600, height=150)

        # search
        search_label = Label(Search_frame, text="Search by:", font=("Arial", 11, "bold"))
        search_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        search_combo = ttk.Combobox(Search_frame, font=("Arial", 11, "bold"), width=16)
        search_combo["values"] = ("select","Phone", "Name")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=5, pady=10, sticky=W)

        # search  button
        rearch_btn = Button(Search_frame, text="Search", width=15, font=("Arial", 11, "bold"), fg="white",
                            bg="darkblue")
        rearch_btn.grid(row=0, column=2, padx=5, pady=5, sticky=W)

        # search  All
        rearchAll_btn = Button(Search_frame, text="Search All", width=15, font=("Arial", 11, "bold"), fg="white",
                            bg="darkblue")
        rearchAll_btn.grid(row=0, column=3, padx=5, pady=5, sticky=W)

        # ==== table Frame----

        table_frame = LabelFrame(right_frame, bd=2, bg="white")
        table_frame.place(x=5, y=160, width=600, height=340)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.elder_table =ttk.Treeview(table_frame,column=("dep","year","care","qua","id","name","gen","heal","notes","mail","phone","date","add","dob"), xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.elder_table.xview)
        scroll_y.config(command=self.elder_table.yview)

        self.elder_table.heading("dep", text="Deparment")
        self.elder_table.heading("year", text="Year")
        self.elder_table.heading("care", text="Caregiver")
        self.elder_table.heading("qua", text="quarter")
        self.elder_table.heading("id", text="ID")
        self.elder_table.heading("name", text="Name")
        self.elder_table.heading("gen", text="gender")
        self.elder_table.heading("heal", text="Health Condition")
        self.elder_table.heading("notes", text="Notes")
        self.elder_table.heading("mail", text="Mail")
        self.elder_table.heading("phone", text="Phone")
        self.elder_table.heading("date", text="Date")
        self.elder_table.heading("add", text="Address")
        self.elder_table.heading("dob", text="DOB")
        self.elder_table["show"] = "headings"

        self.elder_table.column("dep", width=100)
        self.elder_table.column("year", width=100)
        self.elder_table.column("care", width=100)
        self.elder_table.column("qua", width=100)
        self.elder_table.column("id", width=100)
        self.elder_table.column("name", width=100)
        self.elder_table.column("gen", width=100)
        self.elder_table.column("heal", width=100)
        self.elder_table.column("notes", width=100)
        self.elder_table.column("mail", width=100)
        self.elder_table.column("phone", width=100)
        self.elder_table.column("date", width=100)
        self.elder_table.column("add", width=100)
        self.elder_table.column("dob", width=100)

        self.elder_table.pack(fill=BOTH, expand=1)

if __name__ == '__main__':
    root = Tk()
    obj = elder(root)
    root.mainloop()