
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
def ChooseToLogin():
    Choose_AccountFrame.destroy()
    #LoginForm()

def ChooseToCompanion():
    Choose_AccountFrame.destroy()
    #LoginCompanionForm()

