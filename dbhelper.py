import mysql.connector
from mysql.connector import Error


class DBhelper:

    def __init__(self):
        try:
            self.con=mysql.connector.connect(host='localhost',user='root'
                                            ,password='',database='company')
            self.cursor=self.con.cursor()
            print('DataBase Connected...')
        except Error as e:
            print(f'Error Occured {e}')


    def insert(self,name,email,password):

        try:
            self.cursor.execute(f"INSERT INTO `employees` (`name`,`email`,`password`) VALUES ('{name}', '{email}', '{password}');")
            self.con.commit()
            return 1
        except Error as e:
            print(f'An Error occured as {e}')
    def update(self,name,email,password,id):

        try:
            self.cursor.execute(f"UPDATE `employees` SET `name` = '{name}', `email` = '{email}', `password` = '{password}' WHERE id = '{id}';")
            self.con.commit()
            return 1
        except Error as e:
            print(f'An Error occured as {e}')
    def display(self,id):
        try:
            self.cursor.execute(f"SELECT * FROM `employees` WHERE `id`='{id}';")
            return self.cursor.fetchall()
        except Error as e:
            print(f'An Error occured as {e}')

    def delete(self,id):
        try:
            self.cursor.execute(f"DELETE FROM `employees` WHERE `id`='{id}';")
            self.con.commit()
            return 1
        except Error as e:
            print(f'An Error occured as {e}')
