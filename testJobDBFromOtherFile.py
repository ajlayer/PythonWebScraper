# Testing connectivity between file and database
# 2/15/2018 Connection to database works correctly

import sqlite3
import sys

# Connect to database
print("Connecting to database...")
try:
    conn = sqlite3.connect('jobDB.db')
    print("Connected to database.")
except sqlite3.Error as e:
    print("Unable to connect to database")
    print(e)
    sys.exit()

# Creates cursor
c = conn.cursor()

# Adds test data
#joblist = [(8,'Python Database Guy', 'www.website.com', 'Lebanon, PA', 'amazon', 5),
#             (3, 'HTML Developer', 'www.imgay.com', 'Lebanon, PA', 'heeeeee', 6),
#             (2, 'Full stack developer', 'www.CS320.com', 'Lebanon, PA', 'Suggestions', 7),
#             (6,'marketing guy', 'www.what.com', 'Lebanon, PA', 'computer', 11),
#             (7,'Game developer', 'www.this is fun.com', 'Lebanon, PA', 'company', 5),
#             (4,'Web scraper', 'www.yorkcawledge.com', 'Lebanon, PA', 'what', 3),
#             (5,'big man on campus', 'www.mike federline.com', 'Lebanon, PA', 'what', 1),
#            ]
#c.executemany('INSERT INTO jobs VALUES (?,?,?,?,?,?)', joblist)



# Print contents of Database in a for loop
for row in c.execute('SELECT * FROM jobs ORDER BY job_number'):
    print(row)

# Closes connection to database
conn.close()

# Test is finished
print("Test Finished")