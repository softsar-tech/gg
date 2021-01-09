
def Registerproducts():
    global lbl_result2, NUM
    Database()
    if COLOR.get == "" or PRICE.get() == "" or NAME.get() == "" or TYPE.get() == "":
        lbl_result2.config(text="Empty fields!", fg="purple")
    else:
        cursor.execute("SELECT * FROM `products` WHERE `username` = ?", (USERNAME.get(),))
        insert_pic(str(USERNAME.get()), str(NAME.get()), str(COLOR.get()), str(TYPE.get()), str(PRICE.get()))
        PRICE.set("")
        COLOR.set("")
        NAME.set("")
        TYPE.set("")
        NUM += 1
        lbl_result2.config(text="Successfully Created!", fg="black")
        cursor.close()
        conn.close()

def insert_pic(username, name, color, type, price):
    try:
        cursor.execute("INSERT INTO `products` (username, name, color, type, price, namepicfile, datapicfile ) VALUES(?, ?, ?, ?, ?, ?, ?)",
                       (username, name, color, type, price, nampic, dartpic))
        conn.commit()
    except ValueError:
        print(ValueError)
