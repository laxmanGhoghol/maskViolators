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
    if not id:
        print('Error inserting in database: only positive integers allowed')
    else:
        try:
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

def getUserId(uname):
    try:
        sql = 'select id from users where uname = %s'
        mycur.execute(sql, (uname,))
        return mycur.fetchone()
    except:
        print("Error getting user id from database.")
