import socket                   # Import socket module
import sqlite3
port = 60000                
# Reserve a port for your service.
s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
s.bind((host, port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.
x=0
while x<2:
    print ('Server listening....')
    conn, addr = s.accept()     # Establish connection with client.
    print ('Got connection from', addr)
    data=conn.recv(1024)
    print('Server received')
    print('receiving data...')

    filename=str(repr(data)).strip("'")+'.txt'
    f = open(filename,'wb')
    while True:
        data = conn.recv(1024)
        if not data:
            break
        # write data to a file
        f.write(data)
    f.close()
    print('Done receiving')
    
    
    
    conn1 = sqlite3.connect('ListSoft.db')
    cur = conn1.cursor()
    conn1.text_factory = str
    
    cur.execute('''CREATE TABLE IF NOT EXISTS Temp_list 
        (mac TEXT, Software_Name TEXT, 
         id TEXT, Vendor_Name TEXT, Date_of_Install TEXT, Status TEXT)''')
         
    with open(filename, 'r') as f:
    	i=5
    	l=f.readlines()
    	k=len(l)
    	print(k)
    	while(i<k):
    		y='.'
    		z=0
    		s1=""
    		dat=str()
    		DV=str()
    		name=list()
    		vname=list()
    		
    		ss=str(l[i]).split("\x00")
    		#print(ss)
    		#print(s1.join(ss))	
    		a=str(s1.join(ss))
    		b=a.split(" ")
    		#print(b)
    		for j in range(len(b)-1):
    
                     if len(b[j])>0:
                      if b[j].count('.')>=2:
                       DV=str(b[j])
                       z=1
                      else:
                       if z==0:
                        name.append(b[j])
                       elif b[j].isdigit():
                        dat=str(b[j])
                       else:
                        vname.append(b[j])
                i=i+1
                if len(" ".join(name))<1:
                	continue
    		print(DV, " ".join(name), " ".join(vname), dat)
    		cur.execute('''INSERT INTO Temp_list (mac, Software_Name, id, Vendor_Name, Date_of_Install, Status) 
    		VALUES ( ?, ?, ?, ?, ?, ? )''', ( str(filename.split('.')[0]), " ".join(name), DV, " ".join(vname), dat, "INSTALLED"))
    		
    conn1.commit()
    conn.close()
    x=x+1
    cur.close()

conn1 = sqlite3.connect('ListSoft.db')
cur = conn1.cursor()
conn1.text_factory = str

cur.execute('''CREATE TABLE IF NOT EXISTS Policy_Table 
     (id INTEGER UNIQUE, Software_Name TEXT)''') 
cur.execute('''INSERT OR IGNORE INTO Policy_Table (id, Software_name)
        VALUES ( 0, "Python" )''')
cur.execute('''INSERT OR IGNORE INTO Policy_Table (id, Software_name)
        VALUES ( 1, "HP Customer Experience Enhancements" )''')
cur.execute('''INSERT OR IGNORE INTO Policy_Table (id, Software_name)
        VALUES ( 2, "Nullsoft Install System 3.01" )''')
cur.execute('''INSERT OR IGNORE INTO Policy_Table (id, Software_name)
        VALUES ( 3, "HP Support Assistant" )''')
cur.execute('''INSERT OR IGNORE INTO Policy_Table (id, Software_name)
        VALUES ( 4, "Google Update Helper" )''')
cur.execute('''INSERT OR IGNORE INTO Policy_Table (id, Software_name)
        VALUES ( 5, "Intel(R) Processor Graphics" )''')
conn1.commit()
cur.close()

conn1 = sqlite3.connect('ListSoft.db')
cur = conn1.cursor()
conn1.text_factory = str

cur.execute('''CREATE TABLE IF NOT EXISTS TXN_Table 
        (mac TEXT, Software_Name TEXT, 
         id TEXT, Vendor_Name TEXT, Date_of_Install TEXT, Status TEXT)''')

cur.execute('''CREATE TABLE IF NOT EXISTS Exception_Table 
        (mac TEXT, Software_Name TEXT, 
         id TEXT, Vendor_Name TEXT, Date_of_Install TEXT, Status TEXT)''')

cur.execute('''CREATE TABLE IF NOT EXISTS Policy_Table 
     (id INTEGER UNIQUE, Software_Name TEXT)''') 

a=list()
cur.execute('SELECT Software_name FROM Policy_Table')
for row in cur :
   a.append(row)
#print(a)

b=list()
cur.execute('SELECT Software_Name FROM Temp_list')
for row in cur :
   b.append(row)
#print(a)

c=list()
cur.execute('SELECT mac, Software_Name, id, Vendor_Name, Date_of_Install, Status FROM Temp_list')
for row in cur:
  c.append(row)


for i in range(len(b)):
	if b[i] in a:
		cur.execute('''INSERT INTO TXN_Table (mac, Software_Name, id, Vendor_Name, Date_of_Install, Status) 
    		VALUES ( ?, ?, ?, ?, ?, ? )''', ( c[i][0], c[i][1], c[i][2], c[i][3], c[i][4], "P"))
    	else:
    		cur.execute('''INSERT INTO Exception_Table (mac, Software_Name, id, Vendor_Name, Date_of_Install, Status) 
    		VALUES ( ?, ?, ?, ?, ?, ? )''', ( c[i][0], c[i][1], c[i][2], c[i][3], c[i][4], "E"))
conn1.commit()
cur.close()