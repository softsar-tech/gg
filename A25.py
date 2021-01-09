def category2():
    global cg, lbl_result2, PRICE, NAME, COLOR, TYPE
    cg = Frame(app)
    cg.pack()
    Database()

    lbl_result_empty = Label(cg, text="add a product to cast", font=('arial', 18), fg="blue")
    lbl_result_empty.grid(row=0, columnspan=2)

     lbl_type = Label(cg, text="type of the product:", font=('arial', 18), bd=18)
    lbl_type.grid(row=3)

    lbl_result2 = Label(cg, text="", font=('arial', 18))
    lbl_result2.grid(row=6, columnspan=2)

    type = Entry(cg, font=('arial', 20), textvariable=TYPE, width=15)
    type.grid(row=3, column=1)

    


    
