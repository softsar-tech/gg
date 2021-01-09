def category():
    global cg, lbl_result2, PRICE, NAME, COLOR, TYPE
    cg = Frame(app)
    cg.pack()
    Database()

    lbl_result_empty = Label(cg, text="add a product to cast", font=('arial', 18), fg="blue")
    lbl_result_empty.grid(row=0, columnspan=2)

    lbl_left = Label(cg, text="you have", font=('arial', 18), fg="blue")
    lbl_left.grid(row=1, columnspan=2)
    
    lbl_result2 = Label(cg, text="", font=('arial', 18))
    lbl_result2.grid(row=6, columnspan=2)

    lbl_num = Label(cg, text=NUM, font=('arial', 18), fg="blue")
    lbl_num.grid(row=1, column=1)
