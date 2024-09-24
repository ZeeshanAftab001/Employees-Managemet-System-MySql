from dbhelper import DBhelper
import msvcrt
import sys

def getch():   
    return msvcrt.getch().decode()
def get_data(data):
    print('ID : ',data[0][0],'Name : ',data[0][1],'Email : ',data[0][2],'Password : ',data[0][3])
class Employee:

    def __init__(self):
        
        self.db=DBhelper()
        self.menu()

    def menu(self):
        print('1.Create\n2.Show\n3.Delete\n4.Update\n5.Exit\nOption:')
        option=getch()
        match option:
            case '1':
                self.create()
            case '2':
                self.display()
            case '3':
                self.delete()
            case '4':
                self.Update()
            case '5':
                sys.exit(1000)
            case _:
                pass
    def create(self):
        id=input('Id : ')
        name=input('Name : ')
        email=input('Email : ')
        password=input('Password : ')
        flag=self.db.insert(name=name,email=email,password=password)
        if flag:
            print('Record Inserted in the Database')
        self.menu()
    def display(self):
        id=input('ID : ')
        data=self.db.display(id=id)
        if data:
            get_data(data)
        else:
            print('Record Not Found')
        self.menu()
    def delete(self):
        id=input('ID : ')
        flag=self.db.delete(id=id)
        if flag:
            print('Record Deleted')
        else:
            print('Record Not Found')
        self.menu()
    def Update(self):
        id=input('Id : ')
        name=input('Name : ')
        email=input('Email : ')
        password=input('Password : ')
        flag=self.db.update(name=name,email=email,password=password,id=id)
        if flag:
            print('Record Updated in the Database')
        self.menu()
        

obj=Employee()