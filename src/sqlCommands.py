import pymysql.cursors

    def write(database, stamp, temp, humidity, pressure):
        cur = db.cursor()
        cur.execute('INSERT INTO table_name (stamp, temp, humidity, pressure)')
        db.close()
