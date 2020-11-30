def HelpForm():
    global HelpFrame
    HelpFrame = Frame(app)
    HelpFrame.configure(bg='red')
    T=Text(HelpFrame, height=15, width=80, font=('arial', 14))
    T.pack()
    quote="""""
    :THIS APP WILL LET YOU (AS A SELLER) ADDVERTISE
    :IN IT, BESIDE AS A CUSTOMWER YOU CAN SEE THE OTHER PRODUCTS
    :AND YOU CAN ALSO CONNTACT WITH SELLER ACCORDING TO THEIR CONNECTION DATA
    :IN THEIR PERSONAL PAGE
         """""
    T.insert(END, quote)
    T.config(state=DISABLED)
    HelpFrame.pack()
    
