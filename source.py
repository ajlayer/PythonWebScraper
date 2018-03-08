# Scrapes various job websites & stores listings in a database

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import sqlite3
import sys

# Links
testURL = "http://www.pythonscraping.com/pages/warandpeace.html"
monster = "https://www.monster.com/jobs/search/?q=Warehouse&where=17042"
indeed = "https://www.indeed.com/jobs?q=warehouse&l=York%2C+PA"
ziprecruiter = "https://www.ziprecruiter.com/candidate/search?search=warehouse&location=York%2C+PA"
snagajob = "https://www.snagajob.com/job-search?ui=true&q=warehouse&w=17401"

# global job id counter
x = 0
# Connect to database
print("Connecting to database...")
try:
    conn = sqlite3.connect('jobDB.db')
    print(conn)
    c = conn.cursor()
except sqlite3.Error as e:
    print("Unable to connect to database")
    print(e)
    sys.exit()

# TODO: Add arrays to DB
def getJobsFromMonster(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print("Error:")
        print(e)
        return None
    try:
        bsObj = BeautifulSoup(html, "html.parser")
    except AttributeError as e:
        print("Error:")
        print(e)
        return None

    # Scrape for specific tags
    web_id = 1
    titleList = bsObj.findAll("div", {"class":"jobTitle"})
    companyList = bsObj.findAll("div", {"class":"company"})
    locationList = bsObj.findAll("div",{"class":"job-specs job-specs-location"})
    dateList = bsObj.findAll("div",{"class":"job-specs job-specs-date"})
    titles = []
    companies = []
    locations = []
    dates = []

    # Titles
    for name in titleList:
        # Adds title to titles list
        titles.append(name.get_text().strip())

    # Companies
    for name in companyList:
        # Adds company name to companies list
        companies.append(name.get_text().strip())

    # Locations
    for name in locationList:
        # Adds location to location list
        locations.append(name.get_text().strip())

    # Dates
    for name in dateList:
        # Adds date to date list
        dates.append(name.get_text().strip())

    # TODO: add arrays to DB
    for x in range(0, len(titles)):
        tuple = [(x, web_id, titles[x], locations[x], companies[x], dates[x])]
        print(tuple)
        # Add tuple to database
        c.executemany('INSERT INTO jobs VALUES(?,?,?,?,?,?)',tuple)

# TODO: Fix formatting
# TODO: Store info in variables
# TODO: Add info to DB
def getJobsFromSnagajob(url):
    try:
        html = urlopen(url)
    except AttributeError as e:
        print("Error:")
        print(e)
        return None
    try:
        bsObj = BeautifulSoup(html, "html.parser")
    except AttributeError as e:
        print("Error:")
        print(e)
        return None
    # TODO: Scrape for specifics
    tag = "results"
    nameList = bsObj.findAll("div", {"class":tag})
    for name in nameList:
        # TODO: add to database instead of print
        print(name.get_text())

# TODO: Fix formatting
# TODO: Store info in variables
# TODO: Add info to DB
def getJobsFromIndeed(url):
    try:
        html = urlopen(url)
    except AttributeError as e:
        print("Error:")
        print(e)
        return None
    try:
        bsObj = BeautifulSoup(html, "html.parser")
    except AttributeError as e:
        print("Error:")
        print(e)
        return None
    # TODO: Scrape for specifics
    tag = "organicJob"
    nameList = bsObj.findAll("div", {"data-tn-component":tag})
    for name in nameList:
        # TODO: add to database instead of print
        print(name.get_text())

# TODO: Fix formatting
# TODO: Store info in variables
# TODO: Add info to DB
def getJobsFromZipRecruiter(url):
    try:
        html = urlopen(url)
    except AttributeError as e:
        print("Error:")
        print(e)
        return None
    try:
        bsObj = BeautifulSoup(html, "html.parser")
    except AttributeError as e:
        print("Error:")
        print(e)
        return None
    # TODO: Scrape for specifics
    tag = "job_results"
    nameList = bsObj.findAll("div", {"class":tag})
    for name in nameList:
        # TODO: add to database instead of print
        print(name.get_text())

# Prints results
print("**********Monster**********")
getJobsFromMonster(monster)
print("**********SnagAJob**********")
#getJobsFromSnagajob(snagajob)
print("**********Indeed**********")
#getJobsFromIndeed(indeed)
print("**********ZipRecruiter**********")
#getJobsFromZipRecruiter(ziprecruiter)

# Print database contents
for row in c.execute('SELECT * FROM jobs ORDER BY job_number'):
    print(row)

# Commit changes to database
conn.commit()

# Finished, close connection
print("Closing connection...")

try:
    conn.close()
    print("Connection closed.")
except sqlite3.Error as e:
    print("Error closing database")
    print(e)
    sys.exit()