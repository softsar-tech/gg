def Database():
    global conn, cursor
    conn = sqlite3.connect("myapp.db")
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS `customer` (username TEXT, password TEXT, phone TEXT, email TEXT, nameprofile TEXT,dataprofile TEXT)")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS `seller` (username TEXT, password TEXT, phone TEXT, email TEXT, nameprofile TEXT,dataprofile TEXT)")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS `search` (username TEXT)")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS `products` (username TEXT, name TEXT, type TEXT, color TEXT, price TEXT, namepicfile TEXT, datapicfile TEXT)")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS `saved_pictures` (username TEXT, namephoto TEXT, dataphoto TEXT)")
#log in
Customer= StringVar()
Customerpass= StringVar()
def LoginCompanionForm():
    global LoginCompanionFrame, lbl_resul1

    LoginCompanionFrame = Frame(app)
    LoginCompanionFrame.pack()

    lbl_result_empty = Label(LoginCompanionFrame, text="Login For Customer", font=('arial', 18), fg="blue")
    lbl_result_empty.grid(row=0, columnspan=2)

    lbl_username = Label(LoginCompanionFrame, text="Customer Username:", font=('arial', 18), bd=18)
    lbl_username.grid(row=2)

    lbl_password = Label(LoginCompanionFrame, text="Customer Password:", font=('arial', 18), bd=18)
    lbl_password.grid(row=3)

    lbl_resul1 = Label(LoginCompanionFrame, text="", font=('arial', 18))
    lbl_resul1.grid(row=4, columnspan=2)

    username = Entry(LoginCompanionFrame, font=('arial', 20), textvariable=USERNAME, width=15)
    username.grid(row=2, column=1)


    password = Entry(LoginCompanionFrame, font=('arial', 20), textvariable=PASSWORD, width=15, show="*")
    password.grid(row=3, column=1)


    btn_login = Button(LoginCompanionFrame, text="Login", font=('arial', 18), width=35, command=LoginCompanion,
                       fg='red')
    btn_login.grid(row=5, columnspan=2, pady=20)


    btne_register = Button( LoginCompanionFrame, text="Creat Account", fg="red", width=35, font=('arial', 18),
                           command=ToggleToRegister2)
    btne_register.grid(row=6, columnspan=2, pady=20)
def LoginCompanion():
    Database()

    if Customer.get == "" or Customerpass.get() == "":
        lbl_resul1.config(text="Empty fields!", fg="purple")
    else:
        cursor.execute("SELECT * FROM `customer` WHERE `username` = ? and `password` = ?",
                       (Customer.get(), Customerpass.get()))
        if cursor.fetchone() is not None:
            lbl_resul1.config(text="You Successfully Login", fg="blue", command=ToCompanion())
        else:
            lbl_resul1.config(text="Invalid Username or password", fg="red")
