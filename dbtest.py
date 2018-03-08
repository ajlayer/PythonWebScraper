import sqlite3
import sys

# Try to connect to example.db
try:
    # con connects to example db
    con = sqlite3.connect('example.db')
    print("Connected!")
    # Prints address of database
    # <sqlite3.Connection object at 0x058070A0>
    print(con)
# If it cant connect
except sqlite3.Error as e:
    print("cant connect")
    print(e)
    sys.exit()

c = con.cursor()

# Creates a table called stocks
# With columns date, trans, symbol, qty, price
#c.execute('''CREATE TABLE stocks
 #            (date text, trans text, symbol text, qty real, price real)''')

# Insert a row of test data
#c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
#c.execute("INSERT INTO stocks VALUES ('2006-01-05','high','A',100,75.14)")
#c.execute("INSERT INTO stocks VALUES ('2007-01-05','frY','B',100,35.14)")
#c.execute("INSERT INTO stocks VALUES ('2008-01-05','shY','gay',100,65.14)")
#c.execute("INSERT INTO stocks VALUES ('2009-01-05','gUY','RT',100,35.64)")
#c.execute("INSERT INTO stocks VALUES ('2010-01-05','hi','AT',100,35.4)")
#c.execute("INSERT INTO stocks VALUES ('2011-01-05','Bi','HAT',100,35.24)")
#c.execute("INSERT INTO stocks VALUES ('2012-01-05','BY','RAT',100,35.44)")
# Save (commit) the changes

# Larger example that inserts many records at a time
#purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
#             ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
#             ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
#            ]
#c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)

#            (date text, trans text, symbol text, qty real, price real)''')

# Insert into database using tuple and variables
#date = '2018-03-99'
#trans = 'BUY'
#symbol = 'GOOG'
#qty = 15
#price = 67.99

#tupe = [(date, trans, symbol, qty, price)]
#c.executemany('INSERT INTO stocks VALUES(?,?,?,?,?)', tupe)


#con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
#con.close()

# Get stuff from DB
# t = target value
#t = ('RHAT',)
#c.execute('SELECT * FROM stocks WHERE symbol=?', t)
#print(c.fetchone())

for row in c.execute('SELECT * FROM stocks'):
    print(row)

con.close()

##############################
#OUTPUT
#Connected!
#<sqlite3.Connection object at 0x02E7BF20>
#('2006-01-05', 'BUY', 'RHAT', 100.0, 35.14)
#('2006-01-05', 'high', 'A', 100.0, 75.14)
#('2007-01-05', 'frY', 'B', 100.0, 35.14)
#('2008-01-05', 'shY', 'gay', 100.0, 65.14)
#('2009-01-05', 'gUY', 'RT', 100.0, 35.64)
#('2010-01-05', 'hi', 'AT', 100.0, 35.4)
#('2011-01-05', 'Bi', 'HAT', 100.0, 35.24)
#('2012-01-05', 'BY', 'RAT', 100.0, 35.44)
##############################