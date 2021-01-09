def category5():
    global cg, lbl_result2, PRICE, NAME, COLOR, TYPE
    cg = Frame(app)
    cg.pack()
    Database()

    lbl_result_empty = Label(cg, text="add a product to cast", font=('arial', 18), fg="blue")
    lbl_result_empty.grid(row=0, columnspan=2)

    lbl_colors = Label(cg, text="available colors:", font=('arial', 18), bd=18)
    lbl_colors.grid(row=5)

    lbl_result2 = Label(cg, text="", font=('arial', 18))
    lbl_result2.grid(row=6, columnspan=2)

    color = Entry(cg, font=('arial', 20), textvariable=COLOR, width=15)
    color.grid(row=5, column=1)

    btn_add = Button(cg, text="add picture", font=('arial', 10), width=8, fg='black',
                     command=lambda: save_pic(filedialog.askopenfilename(filetypes=[("Image File", '.png')])))
    btn_add.grid(row=7, columnspan=1, pady=20)

    btn_add = Button(cg, text="add", font=('arial', 18), width=35, command=Registerproducts, fg='red')
    btn_add.grid(row=8, columnspan=2, pady=20)

    btne_back = Button(cg, text="back", fg="red", width=35, font=('arial', 18),
                        command=mx)
    btne_back.grid(row=9, columnspan=2, pady=20)
