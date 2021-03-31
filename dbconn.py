import mysql.connector
from datetime import datetime
try:

    hostName = 'localhost'
    userName = 'laxman'
    userPassword = 'jaygoga'
    databaseName = 'mydb' 
    mydb = mysql.connector.connect(host=hostName, user=userName, password=userPassword, database=databaseName)
    mycur = mydb.cursor()
except:
    print("Error accured while connecting to database...")

def insertInViolator(id):
    if id < 0:
        print('Error inserting in database: only positive integers allowed')
    else:
        try:
            id = str(id)
            sql = 'select * from violators where datediff(_datetime, now()) = 0 and uid = %s'
            mycur.execute(sql, (id, ))
            violist = mycur.fetchall()
            print(len(violist))
            if len(violist) == 0:
                nowtime = datetime.now()
                formated_date = nowtime.strftime('%Y-%m-%d %H:%M:%S')
                sql = 'insert into violators values(0, %s, %s);'
                mycur.execute(sql, (id, formated_date,))
                mydb.commit()
                print(f'User with ID: {id} has violated rules and data is inserted')
            else:
                print(f'Violation of user {id} is already inserted.')
        except:
            print(f'Error accured while inserting {id} in violations databaset')

def getUserName(id):
    id = str(id)
    try:
        sql = 'select uname from users where id = %s'
        mycur.execute(sql, (id,))
        return mycur.fetchone()
    except:
        print("Error getting user name from database.")

def insertUser(uname, id):
    try:
        uname = str(uname)
        id = str(id)
        sql = 'insert into users values(%s, %s)'
        mycur.execute(sql, (id, uname, ))
        mydb.commit()
        print(f'Insert new user {uname} at id {id}')
    except:
        print("Error inserting new user..")

def getLastId():
    sql = 'select id from users order by id desc limit 1'
    mycur.execute(sql)
    return mycur.fetchone()