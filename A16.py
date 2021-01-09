def totrackdes():
    ser.destroy()
    totrack()
em= StringVar()
phone=StringVar()
c=StringVar()
s=int()
s=0
n=int()
n=0

def totrack():
    global  lbl_result1,tr, lbl_result2
    tr = Frame(app)
    tr.pack()
    lbl_user = Label(tr, text="personal page", font=('arial', 18), width=35, fg='purple')
    lbl_user.grid(row=2)
    btne_back = Button(tr, text="return to menu", fg="purple", width=20, font=('arial', 18), command=re)
    btne_back.grid(row=1, columnspan=2, pady=20)
    lbl_seller = Label(tr, text="name of the seller:", font=('arial', 18), width=18, fg='black')
    lbl_seller.grid(row=3)
    lbl_phone = Label(tr, text="phone number:", font=('arial', 18), width=18, fg='black')
    lbl_phone.grid(row=4)
    lbl_email = Label(tr, text="email:", font=('arial', 18), width=18, fg='black')
    lbl_email.grid(row=5)
    lbl_result2 = Label(tr, text="", font=('arial', 18))
    lbl_result2.grid(row=6, columnspan=2)
    lbl_num = Label(tr, text=track.get(), font=('arial', 18), fg="black")
    lbl_num.grid(row=3, column=1)
    details()
    lbl_num = Label(tr, text=phone, font=('arial', 18), fg="black")
    lbl_num.grid(row=4, column=1)
    lbl_num = Label(tr, text=em, font=('arial', 18), fg="black")
    lbl_num.grid(row=5, column=1)

    btn_add = Button(tr, text="search", font=('arial', 18), width=35, command=Re, fg='red')
    btn_add.grid(row=6, columnspan=2, pady=20)
