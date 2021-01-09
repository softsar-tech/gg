fnt = ('tahoma', 60)

def profile():
    global prof, eml, USERNAME, phn, user
    prof = Frame(app)
    prof.pack()
    Database()
    global cursor
    cursor.execute("SELECT * FROM 'seller' WHERE username=?", (USERNAME.get(),))
    row = cursor.fetchall()
    for i in row:
        name = i[4]
        imager = i[5]
    if not name or not imager:
        btn_add = Button(prof, text="personal picture", font=('arial', 10), width=10, fg='black',
                         command=lambda: saveprofile(filedialog.askopenfilename(filetypes=[("Image File", '.png')])))
        btn_add.grid(row=3, columnspan=1, pady=20)
    else:
        btn_re = Button(prof, text="profile photo", font=('arial', 10), width=10, fg='black', command=sho)
        btn_re.grid(row=2, columnspan=1, pady=20)
    btn_re = Button(prof, text="return to menu", font=('arial', 10), width=10, fg='black', command=returnprof)
    btn_re.grid(row=0, columnspan=1, pady=20)
    btn_cat = Button(prof, text="categories", font=('arial', 10), width=10, fg='black', command=cat)
    btn_cat.grid(row=4, columnspan=1, pady=20)
    Database()

    cursor.execute("SELECT * FROM 'seller' WHERE username=?", (USERNAME.get(),))
    row = cursor.fetchall()
    for i in row:
        emll = i[3]
        phonee = i[2]
    lbl_n = Label(prof, text="user name:", font=('arial', 15), fg="purple")
    lbl_n.grid(row=5)

    lbl_p = Label(prof, text="Phone number", font=('arial', 15), fg="purple")
    lbl_p.grid(row=6)

    lbl_e = Label(prof, text="Email", font=('arial', 15), fg="purple")
    lbl_e.grid(row=7)
    lbl_result2 = Label(prof, text="", font=('arial', 15))
    lbl_result2.grid(row=9, columnspan=2)
    lbl_num1 = Label(prof, text=USERNAME.get(), font=('arial', 15), fg="black")
    lbl_num1.grid(row=5, column=1)
    lbl_num2 = Label(prof, text=emll, font=('arial', 15), fg="black")
    lbl_num2.grid(row=6, column=1)
    lbl_num3 = Label(prof, text=phonee, font=('arial', 15), fg="black")
    lbl_num3.grid(row=7, column=1)

def cat():
    prof.destroy()
    #category()
def sho():
    prof.destroy()
    #show()
