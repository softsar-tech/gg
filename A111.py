#data base
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
def Login():
    Database()

    if USERNAME.get == "" or PASSWORD.get() == "":
        lbl_result1.config(text="Empty fields!", fg="purple")
    else:
        cursor.execute("SELECT * FROM `seller` WHERE `username` = ? and `password` = ?",
                       (USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            lbl_result1.config(text="You Successfully Login", fg="blue", command=ToCompanion())
        else:
            lbl_result1.config(text="Invalid Username or password", fg="red")

def LoginForm():
    global LoginFrame, lbl_result1

    LoginFrame = Frame(app)
    LoginFrame.pack()

    lbl_result_empty = Label(LoginFrame, text="Login For seller", font=('arial', 18), fg="blue")
    lbl_result_empty.grid(row=0, columnspan=2)

    lbl_username = Label(LoginFrame, text="seller Username:", font=('arial', 18), bd=18)
    lbl_username.grid(row=2)

    lbl_password = Label(LoginFrame, text="seller Password:", font=('arial', 18), bd=18)
    lbl_password.grid(row=3)

    lbl_result1 = Label(LoginFrame, text="", font=('arial', 18))
    lbl_result1.grid(row=4, columnspan=2)

    username = Entry(LoginFrame, font=('arial', 20), textvariable=USERNAME, width=15)
    username.grid(row=2, column=1)
    user=USERNAME

    password = Entry(LoginFrame, font=('arial', 20), textvariable=PASSWORD, width=15, show="*")
    password.grid(row=3, column=1)


    btn_login = Button(LoginFrame, text="Login", font=('arial', 18), width=35, command=Login, fg='red')
    btn_login.grid(row=5, columnspan=2, pady=20)

    btne_register = Button(LoginFrame, text="Creat Account", fg="red", width=35, font=('arial', 18), command=ToggleToRegister1)
    btne_register.grid(row=6, columnspan=2, pady=20)
