global LoginFrame
def RegisterForm():
    global RegisterFrame11, lbl_result2, last
    last=datetime

    RegisterFrame11 = Frame(app)
    RegisterFrame11.pack()

    lbl_result_empty = Label(RegisterFrame11, text="Register For seller", font=('arial', 18), fg="blue")
    lbl_result_empty.grid(row=0, columnspan=2)

    lbl_username = Label(RegisterFrame11, text="seller Username:", font=('arial', 18), bd=18)
    lbl_username.grid(row=2)

    lbl_password = Label(RegisterFrame11, text="seller Password:", font=('arial', 18), bd=18)
    lbl_password.grid(row=3)

    lbl_phonenum = Label(RegisterFrame11, text="seller phone number:", font=('arial', 18), bd=18)
    lbl_phonenum.grid(row=4)


    lbl_email = Label(RegisterFrame11, text="seller email:", font=('arial', 18), bd=18)
    lbl_email.grid(row=5)

    lbl_result2 = Label(RegisterFrame11, text="", font=('arial', 18))
    lbl_result2.grid(row=6, columnspan=2)

    username = Entry(RegisterFrame11, font=('arial', 20), textvariable=USERNAME, width=15)
    username.grid(row=2, column=1)

    password = Entry(RegisterFrame11, font=('arial', 20), textvariable=PASSWORD, width=15, show="*")
    password.grid(row=3, column=1)

    phonenumber = Entry(RegisterFrame11, font=('arial', 20), textvariable=PHONENUM, width=15)
    phonenumber.grid(row=4, column=1)

    email = Entry(RegisterFrame11, font=('arial', 20), textvariable=EMAIL, width=15)
    email.grid(row=5, column=1)

    btn_login = Button(RegisterFrame11, text="Register", font=('arial', 18), width=35, command=Register, fg='red')
    btn_login.grid(row=7, columnspan=2, pady=20)

    btne_login = Button(RegisterFrame11, text="Return To Login", fg="red", width=35, font=('arial', 18),
                        command=ToggleToLogin)
    btne_login.grid(row=8, columnspan=2, pady=20)
    #######################################################

def RegisterForm1():
    global RegisterFrame, lbl_result2

    RegisterFrame = Frame(app)
    RegisterFrame.pack()

    lbl_result_empty = Label(RegisterFrame, text="Register For Customer", font=('arial', 18), fg="blue")
    lbl_result_empty.grid(row=0, columnspan=2)

    lbl_username = Label(RegisterFrame, text="custome Username:", font=('arial', 18), bd=18)
    lbl_username.grid(row=2)

    lbl_password = Label(RegisterFrame, text="custome Password:", font=('arial', 18), bd=18)
    lbl_password.grid(row=3)

    lbl_phonenum = Label(RegisterFrame, text="custome phone number:", font=('arial', 18), bd=18)
    lbl_phonenum.grid(row=4)

    lbl_email = Label(RegisterFrame, text="custome email:", font=('arial', 18), bd=18)
    lbl_email.grid(row=5)

    lbl_result2 = Label(RegisterFrame, text="", font=('arial', 18))
    lbl_result2.grid(row=6, columnspan=2)

    username = Entry(RegisterFrame, font=('arial', 20), textvariable=USERNAME, width=15)
    username.grid(row=2, column=1)

    password = Entry(RegisterFrame, font=('arial', 20), textvariable=PASSWORD, width=15, show="*")
    password.grid(row=3, column=1)

    phonenumber = Entry(RegisterFrame, font=('arial', 20), textvariable=PHONENUM, width=15)
    phonenumber.grid(row=4, column=1)

    email = Entry(RegisterFrame, font=('arial', 20), textvariable=EMAIL, width=15)
    email.grid(row=5, column=1)

    btn_login = Button(RegisterFrame, text="Register", font=('arial', 18), width=35, command=Register, fg='red')
    btn_login.grid(row=7, columnspan=2, pady=20)

    btne_login = Button(RegisterFrame, text="Return To Login", fg="red", width=35, font=('arial', 18),
                        command=tocust)
    btne_login.grid(row=8, columnspan=2, pady=20)



def Register():

    Database()
    if USERNAME.get == "" or PASSWORD.get() == "" or PHONENUM.get() == "" or EMAIL.get() == "":
        lbl_result2.config(text="Empty fields!", fg="purple")
    else:
        cursor.execute("SELECT * FROM `seller` WHERE `username` = ?", (USERNAME.get(),))
        if cursor.fetchone() is not None:
            lbl_result2.config(text="Username is already taken", fg="red")
        cursor.execute("SELECT * FROM `customer` WHERE `username` = ?", (USERNAME.get(),))
        if cursor.fetchone() is not None:
            lbl_result2.config(text="Username is already taken", fg="red")

        else:
            insert_seller(str(USERNAME.get()), str(PASSWORD.get()), str(PHONENUM.get()), str(EMAIL.get()))
            insert_customer(str(USERNAME.get()), str(PASSWORD.get()), str(PHONENUM.get()), str(EMAIL.get()))
            USERNAME.set("")
            PASSWORD.set("")
            PHONENUM.set("")
            EMAIL.set("")
            lbl_result2.config(text="Successfully Created!", fg="black")
        cursor.close()
        conn.close()

def insert_seller(username, password, num, email):
    try:
        cursor.execute("INSERT INTO `seller` (username, password, phone, email) VALUES(?, ?, ?, ?)", (username, password, num, email))
        conn.commit()
    except ValueError:
        print(ValueError)


def insert_customer(username, password, num, email):
    try:
        cursor.execute("INSERT INTO `customer` (username, password, phone, email) VALUES(?, ?,?,?,?,?)", (username, password, num, email))
        conn.commit()
    except ValueError:
        print(ValueError)

