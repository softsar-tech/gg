
def MenuForm():
    global mm
    mm = Frame(app)
    mm.pack()

    lbl_ = Label(mm, text="", font=('arial', 18), bd=18)
    lbl_.grid(row=0)
    btn_setting = Button(mm, text="setting", font=('arial', 18), width=35, fg='purple', command=#ChangeBackGround)
    btn_setting.grid(row=2, columnspan=2, pady=20)
    btn_profile = Button(mm, text="Profile Page", font=('arial', 18), width=35, fg='purple', command=#Toprofile)
    btn_profile.grid(row=4, columnspan=2, pady=20)
    btn_search = Button(mm, text="Search", font=('arial', 18), width=35, fg='purple', command=#Tosearch)
    btn_search.grid(row=6, columnspan=2, pady=20)
    btn_savedp = Button(mm, text="saved picture", font=('arial', 18), width=35, fg='purple', command=#tosave)
    btn_savedp.grid(row=8, columnspan=2, pady=20)
    btn_help = Button(mm, text="help", font=('arial', 18), width=35, fg='purple', command=#gohelp)
    btn_help.grid(row=10, columnspan=2, pady=20)
    btn_sound = Button(mm, text="Sound on/off", font=('arial', 18), width=35, fg='purple', command=#stop_)
    btn_sound.grid(row=12, columnspan=2, pady=20)
    btn_exit = Button(mm, text="Exit", font=('arial', 18), width=35, fg='purple', command=Exit)
    btn_exit.grid(row=14, columnspan=2, pady=20)
