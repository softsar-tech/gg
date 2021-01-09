typeproduct=StringVar()
def search_prod():
    Database()
    global prod, lbl_result2, track
    prod = Frame(app)
    prod.pack()
    btn_re = Button(prod, text="return to menu", font=('arial', 10), width=10, fg='black', command=retur)
    btn_re.grid(row=0, columnspan=2, pady=20)
    lbl_result_empty = Label(prod, text="search according to the type of the products (categories) in the seller page:", font=('arial', 25), fg="purple")
    lbl_result_empty.grid(row=1, columnspan=2)
    lbl_result1 = Label(prod, text="the categories he have are:", font=('arial', 25), fg="purple")
    lbl_result1.grid(row=2, columnspan=2)

    qq=0
    global cursor
    cursor.execute("SELECT * FROM 'products' WHERE username=?", (track.get(),))
    row = cursor.fetchall()
    lista = [NONE] * len(row)
    for i in row:
        while qq != len(row):
            a = row[qq][2]
            lista[qq]=a
            qq += 1
    final_new_menu = list(dict.fromkeys(lista))

    lbl_re = Label(prod, text=final_new_menu, font=('arial', 18))
    lbl_re.grid(row=4, columnspan=2)
    lbl_result2 = Label(prod, text="", font=('arial', 18))
    lbl_result2.grid(row=5, columnspan=2)

    username1 = Entry(prod, font=('arial', 20), text=typeproduct, width=15)
    username1.grid(row=6, column=1)
    btn_go = Button(prod, text="go", font=('arial', 18), width=35, fg='purple', command=ffff)
    btn_go.grid(row=7, columnspan=2, pady=20)
