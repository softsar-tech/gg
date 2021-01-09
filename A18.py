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

def insert_save(nam, pict):

    try:
        cursor.execute("INSERT INTO `saved_pictures` (username, namephoto, dataphoto) VALUES(?, ?, ?)",
                       (USERNAME.get(), nam, pict))
        conn.commit()
    except ValueError:
        print(ValueError)
