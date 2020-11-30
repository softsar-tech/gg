import time
from builtins import range, open
from tkinter import *
from tkinter import ttk
import tkinter.messagebox as tkMessageBox
from functools import partial
import os
import tkinter
import sqlite3
import datetime
date_object = datetime.date.today()

app = Tk()
app.geometry('400x150')
app.title('Your Ad Here!')
#app.resizable(0, 0)

#data base
def Database():
    global conn, cursor
    conn = sqlite3.connect("db_admins.db")
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS `customer` (emp_num INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, password TEXT, emp_em TEXT)")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS `seller` (sell_num INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, password TEXT,sell_email TEXT)")

def Choose_Account_Form():
    global Choose_AccountFrame
    Choose_AccountFrame = Frame(app)
    Choose_AccountFrame.pack()

    lbl_ = Label(Choose_AccountFrame, text="", font=('arial', 18), bd=18)
    lbl_.grid(row=0)

    btn_companion = Button(Choose_AccountFrame, text="For Customers", font=('arial', 18), width=35, fg='purple',
                           command=ChooseToCompanion)
    btn_companion.grid(row=2, columnspan=2, pady=20)

    btn_admin = Button(Choose_AccountFrame, text="For Sellers", font=('arial', 18), width=35, fg='purple',
                       command=ChooseToLogin)
    btn_admin.grid(row=5, columnspan=2, pady=20)

USERNAME = StringVar()
PASSWORD = StringVar()
def ChooseToCompanion():
    Choose_AccountFrame.destroy()
    LoginCompanionForm()

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

    username = Entry(LoginCompanionFrame, font=('arial', 20), textvariable=Customer, width=15)
    username.grid(row=2, column=1)

    password = Entry(LoginCompanionFrame, font=('arial', 20), textvariable=Customerpass, width=15, show="*")
    password.grid(row=3, column=1)

    btn_login = Button(LoginCompanionFrame, text="Login", font=('arial', 18), width=35, command=LoginCompanion,
                       fg='red')
    btn_login.grid(row=5, columnspan=2, pady=20)

    #btne_register = Button(LoginCompanionFrame, text="Creat Account", fg="red", width=35, font=('arial', 18),
                          # command=ToggleToRegisterCompanion)
    #btne_register.grid(row=6, columnspan=2, pady=20)

def LoginCompanion():
    Database()

    if Customer.get == "" or Customerpass.get() == "":
        lbl_resul1.config(text="Empty fields!", fg="purple")
    else:
        cursor.execute("SELECT * FROM `customer` WHERE `username` = ? and `password` = ?",
                       (Customer.get(), Customerpass.get()))
        if cursor.fetchone() is not None:
            lbl_resul1.config(text="You Successfully Login", fg="blue")
            #ToCompanion()
        else:
            lbl_resul1.config(text="Invalid Username or password", fg="red")
def ChooseToLogin():
    Choose_AccountFrame.destroy()
    LoginForm()
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

    password = Entry(LoginFrame, font=('arial', 20), textvariable=PASSWORD, width=15, show="*")
    password.grid(row=3, column=1)

    btn_login = Button(LoginFrame, text="Login", font=('arial', 18), width=35, command=Login, fg='red')
    btn_login.grid(row=5, columnspan=2, pady=20)

    #btne_register = Button(LoginFrame, text="Creat Account", fg="red", width=35, font=('arial', 18),
     #                      command=ToggleToRegister)
    #btne_register.grid(row=6, columnspan=2, pady=20)
def Login():
    Database()

    if USERNAME.get == "" or PASSWORD.get() == "":
        lbl_result1.config(text="Empty fields!", fg="purple")
    else:
        cursor.execute("SELECT * FROM `seller` WHERE `username` = ? and `password` = ?",
                       (USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            lbl_result1.config(text="You Successfully Login", fg="blue")
            #LoginToAdmin()
        else:
            lbl_result1.config(text="Invalid Username or password", fg="red")
def insert_customer(username, password, number):
	try:
		cursor.execute("INSERT INTO `customer` (username, password, number,email) VALUES(?, ?,?,?,?,?)",
					   (username, password, number, 0))
		conn.commit()
	except ValueError:
		print(ValueError)

def IsExist(name, password):
    Database()
    cursor.execute("SELECT * FROM `customer` WHERE `username` =? and `password` = ?", (name, password,))
    if cursor.fetchone() is not None:
        return True

    return False
#Choose_Account_Form()



app.mainloop()
