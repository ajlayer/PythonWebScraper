# Creates database to store job listings
import sqlite3
import sys

# Connect to database
print("Connecting to database...")

try:
    conn = sqlite3.connect('jobDB.db')
    print("Successfully connected to database at address: ")
    print(conn)
except sqlite3.Error as e:
    print("Unable to connect to database")
    print(e)
    sys.exit()

# Create cursor
c = conn.cursor()

# TODO: Drop old database
# TODO: Create new database with web_id instead of website
# TODO: Create separate database for websites using web_id and website name

############################################

############################################
################Drop Table##################
#c.execute('DROP TABLE jobs')

# Insert test data into both tables
#c.execute('''INSERT INTO jobs VALUES (1, 1, 'im gay', 'lebanon, pa', 'mcdonalds', 'july 4th, 1863')''')
#c.execute('''INSERT INTO websites VALUES (1, 'www.ChicFilA.com')''')


# Save (Commit) changes
conn.commit()

# Print contents of Database in a for loop in order of job number
#for row in c.execute('SELECT * FROM jobs ORDER BY job_number'):
#    print(row)

# Prints everything from jobs
for row in c.execute('SELECT * FROM jobs ORDER BY job_number'):
    print(row)

# Prints everything from websites
for row in c.execute('SELECT * FROM websites ORDER BY web_id'):
    print(row)

# Finished, close connection
print("Closing connection...")

try:
    conn.close()
    print("Connection closed.")
except sqlite3.Error as e:
    print("Error closing database")
    print(e)
    sys.exit()

