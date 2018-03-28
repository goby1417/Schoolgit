import sqlite3
from PyQT5.QtWidgets import *

#remember to clear all other widgets before adding new ones 
class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init()
        
        lbl_welcome = QLabel("Welcome! Please click the button bellow to login to interact with the database.", self)
        lbl_welcome.move(10, 10)

        btn_Login= QPushButton('Login', self)
        btn_Login.move(30,15)

        self.error = 0
            
        btn_Login.clicked.connect(self.UserandPasswordWindow)

    def UserandPasswordWindow(self):
        lbl_user = QLabel("Username: ", self)
        lbl_user.move(10, 10)
        self.lne_user = QLineEdit(self)
        self.lne_user.move(10, 20)

        lbl_password = QLabel("Password: ", self)
        lbl_password.move(20, 10)
        self.lne_password = QLineEdit(self)
        self.lne_password.move(20, 20)

        btn_check= QPushButton('Go', self)
        btn_check.move(30,15)

        if self.error == 1:
            lbl_error1 = QLabel("INCORRECT USER ENTERED. TRY AGAIN.", self)
            lbl_error1.move(40, 10)
        elif self.error == 2:
            lbl_error2 = QLabel("INCORRECT PASSWORD ENTERED. TRY AGAIN.", self)
            lbl_error2.move(40, 10)
            
        btnLogin.clicked.connect(self.Check1, self.lne_user.text, self.lne_password.text)

    def Check1(self, UsernameGiven, PasswordGiven):
        import csv
        self.UserList = []
        with open("UsersFile.csv") as f:
            reader = csv.DictReader(f, delimiter=',')
            for line in reader:
                for x in line.split(","):
                    x.strip()
                    self.UserList.append(x)
            for i in range (0,len(self.UserList)):                                   #range automatically takes the 1 off the lenght of the list 
                if self.UserList[i] == UsernameGiven:
                    Check2(self, PasswordGiven)
                elif i == len(self.UserList) and not self.UserList[i] == UsernameGiven:
                    self.error = 1
                    UserandPasswordWindow(self, self.error)
                else:
                    i += 1

    def Check2(self, PasswordGiven):
        import csv
        self.PasswordList = []
        with open("PasswordFile.csv") as f:
            reader = csv.DictReader(f, delimiter=',')
            for line in reader:
                for x in line.split(","):
                    x.strip()
                    self.PasswordList.append(x)
            for i in range (0,len(self.PasswordList)):                               #range automatically takes the 1 off the lenght of the list 
                if self.PasswordList[i] == PasswordGiven:
                    self.MainWindow = MainWindow(self)
                    #self.MainWindow.show()
                elif i == len(self.PassordList) and not self.PasswordList[i] == PasswordGiven:
                    self.error = 2
                    UserandPasswordWindow(self, self.error)
                else:
                    i += 1
                    
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        lbl_welcome = QLabel("Read the instruction text document then click a button to procede", self)
        lbl_welcome.move(10, 10)        
        
        btn_addKW = QPushButton('Add a keyword', self)
        btn_addKW.move(15, 10)
        self.lne_addKW = QlineEdit(self)
        self.lne_addKW.move(15, 20)

        btn_viewKWs = QPushButton('View all keywords', self)
        btn_viewKWs.move(20, 10)

        btn_NoT = QPushButton('Number of tweets in the past...', self)
        btn_NoT.move(25, 10)
        self.lne_statsNoT = QlineEdit(self)
        self.lne_statsNoT.move(25, 20)

        btn_SoKW = QPushButton('Stats on a keyword', self)
        btn_SoKW.move(30, 10)
        self.lne_SoKW = QlineEdit(self)
        self.lne_SoKW.move(30, 20)

        btn_SoD = QPushButton('Stats on demographic', self)
        btn_SoD.move(35, 10)
        lbl_age = QLabel("Age : ")
        lbl_age.move(40, 10)
        lbl_gender = QLabel("Gender: ")
        lbl_gender.move(45, 10)
        self.lne_SoDage = QlineEdit(self)
        self.lne_SoDage.move(40, 20)
        self.lne_SoDgender = QlineEdit(self)
        self.lne_SoDgender.move(45, 20)

        btn_addKW.clicked.connect(self.AddKeywords)
        btn_viewKWs.clicked.connect(self.ViewKeywords)
        btn_NoT.clicked.connect(self.NumberofTweets)
        btn_SoKW.clicked.connect(self.StatsOnKeyword)
        btn_SoD.clicked.connect(self.StatsOnDemographic)

    def OpenDB():
        conn = sqlite3.connect('PROJECT[1].db')
        x = conn.cursor()
        return (conn, x)

    def CloseDB(conn):
        con.commit()
        conn.commit()

    def AddKeywords(self):
        conn, x = OpenDB()
        x.execute("INSERT INTO Keywords (%s, 0, 0, 0)" % (self.lne_addKW.text))
        CloseDB(conn)
        #validation

    def ViewKeywords(self):
        conn, x = OpenDB()
        x.execute("SELECT Keyword FROM Keywords")
        CloseDB(conn)
        #validation 

    def NumberofTweets(self):
        print("C")
        #NOT IN MYSQL MAYBE WRITE OUT THE STATS FOR THAT DAY OUT INTO A TEXT FILE THEN READ THEN TO MAKE THE CALCULATION 

    def StatsOnKeyword(self):
        conn, x = OpenDB()
        x.execute("SELECT * FROM Keywords WHERE Keyword = %s" % (self.lne_SoKW.text))
        CloseDB(conn)

    def StatsOnDemographic(self):
        #to avoid any confusion if they dont want to enter an age / gender they enter 'NONE'
        if self.lne_SoDgender == 'NONE' and self.lne_SoDage != 'NONE':
            conn, x = OpenDB()
            x.execute("SELECT Keyword FROM Keywords WHERE Age = %s" % (self.lne_SoDage.text))
            CloseDB(conn)
        elif self.lne_SoDage == 'NONE' and self.lne_SoDgender != 'NONE':
            conn, x = OpenDB()
            x.execute("SELECT Keyword FROM Keywords WHERE Gender = %s" % (self.lne_SoDgender.text))
            CloseDB(conn)


#stuff to do:
    #what format is the information returned in sqlite3?
    #check transistions from each function - .hide() widgets (will need to take into account some widgets are conditional) OR make a new window each time 
    #validation of text line edit 
           













        
        
                
