def insert_save(nam, pict):

    try:
        cursor.execute("INSERT INTO `saved_pictures` (username, namephoto, dataphoto) VALUES(?, ?, ?)",
                       (USERNAME.get(), nam, pict))
        conn.commit()
    except ValueError:
        print(ValueError)
