def showproduct():
    global x
    x = Frame(app)
    x.pack()
    Database()
    global cursor
    cursor.execute("SELECT * FROM 'products' WHERE type=?", (typeproduct.get(),))
    row = cursor.fetchall()
    global c, s, n
    for i in row:
        while s != len(row):
            a = row[0][1]
            b = row[0][2]
            c = row[0][3]
            d = row[0][4]
            e = row[0][5]
            f = row[0][6]
            s += 1
            btne_back = Button(x, text="return to menu", fg="purple", width=20, font=('arial', 18),
                               command=re)
            btne_back.grid(row=1, columnspan=2, pady=20)
            lbl_user1 = Label(x, text="details about the product:", font=('arial', 18), width=35, fg='purple')
            lbl_user1.grid(row=2)
            lbl_s = Label(x, text="name of the product:", font=('arial', 18), width=18, fg='black')
            lbl_s.grid(row=3)
            lbl_p = Label(x, text="type of the product:", font=('arial', 18), width=18, fg='black')
            lbl_p.grid(row=4)
            lbl_e = Label(x, text="color of the product:", font=('arial', 18), width=18, fg='black')
            lbl_e.grid(row=5)
            lbl_e = Label(x, text="price of the product:", font=('arial', 18), width=18, fg='black')
            lbl_e.grid(row=6)
            lbl_result21 = Label(x, text="", font=('arial', 18))
            lbl_result2 = Label(x, text=a, font=('arial', 18), fg="black")
            lbl_result2.grid(row=3, column=1)
            lbl_result1 = Label(x, text=b, font=('arial', 18), fg="black")
            lbl_result1.grid(row=4, column=1)
            lbl_result3 = Label(x, text=c, font=('arial', 18), fg="black")
            lbl_result3.grid(row=5, column=1)
            lbl_result4 = Label(x, text=d, font=('arial', 18), fg="black")
            lbl_result4.grid(row=6, column=1)


            def showpic():

                global show, lbl_result2
                show = Frame(app)
                show.pack()
                def rem():
                    show.destroy()
                    MenuForm()
                global ner
                b = open(e, 'wb')
                b.write(f)
                ner = PhotoImage(file=e)
                global fnt
                btne_back1 = Button(show, text="return to menu", fg="purple", width=20, font=('arial', 18),
                                   command=rem)
                btne_back1.grid(row=0, columnspan=2, pady=20)
                lbl_result_empty = Label(show, bg="white", font=fnt, height=200, width=250, image=ner)
                lbl_result_empty.grid(row=2, column=1, padx=300, pady=10)
                btn_dd = Button(show, text="save picture", fg="purple", width=20, font=('arial', 18), command=insert_save(e, f))
                btn_dd.grid(row=3, columnspan=2, pady=20)
            def ss():
                x.destroy()
                showpic()
            btne_b = Button(x, text="see the picture", fg="purple", width=20, font=('arial', 18), command=ss)
            btne_b.grid(row=7, columnspan=2, pady=20)
def insert_save(nam, pict):

    try:
        cursor.execute("INSERT INTO `saved_pictures` (username, namephoto, dataphoto) VALUES(?, ?, ?)",
                       (USERNAME.get(), nam, pict))
        conn.commit()
    except ValueError:
        print(ValueError)
def sss():
    x.destroy()
