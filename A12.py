def Tosearch():
    mm.destroy()
    search()
def search():
    Database()
    global ser, lbl_result2, track
    ser = Frame(app)
    ser.pack()
    btn_re = Button(ser, text="return to menu", font=('arial', 10), width=10, fg='black', command=#returnser)
    btn_re.grid(row=0, columnspan=2, pady=20)

    lbl_result_empty = Label(ser, text="search", font=('arial', 25), fg="purple")
    lbl_result_empty.grid(row=1, columnspan=2)
    lbl_result2 = Label(ser, text="", font=('arial', 18))
    lbl_result2.grid(row=6, columnspan=2)
    username1 = Entry(ser, font=('arial', 20), text=track, width=15)
    username1.grid(row=3, column=1)
    btn_go = Button(ser, text="go", font=('arial', 18), width=35, fg='purple', command=#absar)
    btn_go.grid(row=7, columnspan=2, pady=20)
