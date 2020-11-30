def Remove_user(name):
    Database()
    if CheckIsUser(name) == True:
        deleteuser(name)
    else:
        exit()


def CheckIsUser(name):
    cursor.execute("SELECT * FROM `seller` WHERE username=?", (name,))
    if cursor.fetchone() is not None:
        return True
    return False


def deleteuser(name):
    try:
        cursor.execute("delete from 'seller' where username= ?", (name,))
        conn.commit()
    except ValueError:
        print(ValueError)


