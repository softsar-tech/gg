COLORH = StringVar()
COLORH.set("light green")
def ChangeBackGround():
    if COLORH.get() == "light green":
        COLORH.set("purple")
        app.configure(bg="purple")
    else:
          COLORH.set("light green")
          app.configure(bg="light green")


