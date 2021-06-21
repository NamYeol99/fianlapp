import pymysql

def dbcon():
    return pymysql.connect(host='namyeol.mysql.pythonanywhere-services.com',
                   user='namyeol', password='1234',
                   db='namyeol$ddb', charset='utf8')

def insert_member(email, pw, name):
    try:
        db = dbcon()
        c = db.cursor()
        setdata = (email, pw, name)
        c.execute("INSERT INTO member VALUES (%s, %s, %s)", setdata)
        db.commit()
    except Exception as e:
        print('db error:', e)
    finally:
        db.close()

def select_all():
    ret = list()
    try:
        db = dbcon()
        c = db.cursor()
        c.execute('SELECT * FROM member')
        ret = c.fetchall()
        # for row in c.execute('SELECT * FROM student'):
        #     ret.append(row)
    except Exception as e:
        print('db error:', e)
    finally:
        db.close()
        return ret

def select_member(email, pw):
    ret = ()
    try:
        db = dbcon()
        c = db.cursor()
        setdata = (email, pw)
        c.execute('SELECT * FROM member WHERE email = %s AND pw = %s', setdata)
        ret = c.fetchone()
    except Exception as e:
        print('db error:', e)
    finally:
        db.close()
        return ret
##insert_member('b@b.com', '1234', '비비비')
ret = select_member('b@b.com', '1234')
print(ret)