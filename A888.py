def CreaditsForm():
    global CreaditsFrame
    CreaditsFrame = Frame(app)
    CreaditsFrame.configure(bg='red')
    T = Text(CreaditsFrame, height=15, width=80, font=('arial', 14))
    T.pack()
    quote = """
    מפתחי המשחק :
    -naema eldda  naemaal@ac.sce.ac.il 
    -sujood eldda  sujood.eldda@gmail.com 
    -arin alnbary
    -ranin abu jafar
    -rawan afenesh
    
    """
    T.insert(END, quote)
    T.config(state=DISABLED)
    newbtb = Button(CreaditsFrame, text='Return To Menu', font=('arial', 20))
    #, command=CreaditToMenu)
    newbtb.pack()
    CreaditsFrame.pack()
