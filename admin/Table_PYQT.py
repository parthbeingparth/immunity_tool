# coding: utf-8

# ## Libraries 

# In[7]:

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.Qt import *
import sqlite3



# ### Initializing Elements

# In[3]:

class NewWindow(QMainWindow):
    def __init__(self):
        super(NewWindow, self).__init__()
        self._new_window = None
        self.win = QWidget() 
        self.table = QTableWidget()
        self.tableItem = QTableWidgetItem()
        font = QFont()
        font.setBold(True)
        self.setWindowTitle("Team jarvis")
        
        generate1=QPushButton("Exception_table",self.win)
        generate1.move(85,50)
        generate1.resize(120,30)
        generate1.clicked.connect(self.show_Exception_table)
        
        generate2=QPushButton("Policy_Table",self.win)
        generate2.move(85,90)
        generate2.resize(120,30)
        generate2.clicked.connect(self.show_Policy_table)
        
        generate3=QPushButton("Temp_Table",self.win)
        generate3.move(85,130)
        generate3.resize(120,30)
        generate3.clicked.connect(self.show_temp_table)
        
        generate4=QPushButton("TXN Table",self.win)
        generate4.move(85,170)
        generate4.resize(120,30)
        generate4.clicked.connect(self.show_TXn_table)
        
        self.win.setFixedHeight(250)
        self.win.setFixedWidth(300)
        self.win.setWindowTitle("Summarize IT")
        self.setCentralWidget(self.win)
        
    def show_Exception_table(self):
        self.table.setWindowTitle("Exception_Table")
        self.table.resize(800, 800)
        self.table.setColumnCount(6)
        conn = sqlite3.connect('ListSoft.db')
        cursor=conn.execute("SELECT COUNT(*) from Exception_Table")
        result=cursor.fetchone()
        self.table.setRowCount(result[0])
        #table.setHorizontalHeaderLabels(QString("ip;Software_name;id;Vendor_name;Date;Status;").split(";"))
        self.table.setHorizontalHeaderLabels(["ip","Software_name","id","Vendor_name","Date","Status"])
        cursor = conn.execute("SELECT *  from Exception_Table")
        i=0
        for row in cursor:
            self.table.setItem(i,0, QTableWidgetItem(row[0]))
            self.table.setItem(i,1, QTableWidgetItem(row[1]))
            self.table.setItem(i,2, QTableWidgetItem(row[2]))
            self.table.setItem(i,3, QTableWidgetItem(row[3]))
            self.table.setItem(i,4, QTableWidgetItem(row[4]))
            self.table.setItem(i,5, QTableWidgetItem(row[5]))
            i=i+1
        self.table.show()

    def show_Policy_table(self):
        self.table.setWindowTitle("Policy_Table")
        self.table.resize(400, 800)
        self.table.setColumnCount(2)
        conn = sqlite3.connect('ListSoft.db')
        cursor=conn.execute("SELECT COUNT(*) from Policy_Table")
        result=cursor.fetchone()
        self.table.setRowCount(result[0])
        self.table.setHorizontalHeaderLabels(["id","Software_name"])
        cursor = conn.execute("SELECT *  from Policy_Table")
        i=0
        for row in cursor:
            self.table.setItem(i,0, QTableWidgetItem(row[0]))
            self.table.setItem(i,1, QTableWidgetItem(row[1]))
            i=i+1
        self.table.show()
        
    def show_TXn_table(self):
        self.table.setWindowTitle("TXN_Table")
        self.table.resize(800, 800)
        self.table.setColumnCount(6)
        conn = sqlite3.connect('ListSoft.db')
        cursor=conn.execute("SELECT COUNT(*) from TXN_Table")
        result=cursor.fetchone()
        self.table.setRowCount(result[0])
        self.table.setHorizontalHeaderLabels(["ip","Software_name","id","Vendor_name","Date","Status"])
        cursor = conn.execute("SELECT *  from TXN_Table")
        i=0
        for row in cursor:
            self.table.setItem(i,0, QTableWidgetItem(row[0]))
            self.table.setItem(i,1, QTableWidgetItem(row[1]))
            self.table.setItem(i,2, QTableWidgetItem(row[2]))
            self.table.setItem(i,3, QTableWidgetItem(row[3]))
            self.table.setItem(i,4, QTableWidgetItem(row[4]))
            self.table.setItem(i,5, QTableWidgetItem(row[5]))
            i=i+1
        self.table.show()
        
    def show_temp_table(self):
        self.table.setWindowTitle("Temp_list")
        self.table.resize(800, 800)
        self.table.setColumnCount(6)
        conn = sqlite3.connect('ListSoft.db')
        cursor=conn.execute("SELECT COUNT(*) from Temp_list")
        result=cursor.fetchone()
        self.table.setRowCount(result[0])
        self.table.setHorizontalHeaderLabels(["ip","Software_name","id","Vendor_name","Date","Status"])
        cursor = conn.execute("SELECT *  from Temp_list")
        i=0
        for row in cursor:
            self.table.setItem(i,0, QTableWidgetItem(row[0]))
            self.table.setItem(i,1, QTableWidgetItem(row[1]))
            self.table.setItem(i,2, QTableWidgetItem(row[2]))
            self.table.setItem(i,3, QTableWidgetItem(row[3]))
            self.table.setItem(i,4, QTableWidgetItem(row[4]))
            self.table.setItem(i,5, QTableWidgetItem(row[5]))
            i=i+1
        self.table.show()

if __name__ == '__main__':
    app = QApplication([])
    gui = NewWindow()
    gui.show()
    app.exec_()



# In[25]:


# In[ ]: