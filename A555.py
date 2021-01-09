def tosave():
    mm.destroy()
    saved()
def saved():
    global savedd
    savedd = Frame(app)
    savedd.pack()
    btn_r1e = Button(savedd, text="return to menu", font=('arial', 10), width=20, fg='purple', command=men)
    btn_r1e.grid(row=0, columnspan=1, pady=20)

    lbl_result_empty1 = Label(savedd, bg="white", font=fnt, height=200, width=250, image=convp1())
    lbl_result_empty1.grid(row=1, column=1, padx=300, pady=10)
