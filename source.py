# Scrapes various job websites & stores listings in a database

from urllib import urlopen
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


# Gets jobs from monster.com and adds the information to a database
def getJobsFromMonster(url):
    # Try to connect to website URL
    try:
        html = urlopen(url)
    # If it can not connect
    except AttributeError as e:
        print("Error:")
        print(e)
        return None
    # Try to parse the web page into a beautifulsoup object
    try:
        bsObj = BeautifulSoup(html, "html.parser")
    # If it cant create a beautifulsoup object
    except AttributeError as e:
        print("Error:")
        print(e)
        return None

    # Scrape for specific tags

    # TODO: Get web id from database of websites
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


    for x in range(0, len(titles)):
        tupe = [(x, web_id, titles[x], locations[x], companies[x], dates[x])]
        print(tupe)
        # Add tuple to database
        #c.executemany('INSERT INTO jobs VALUES(?,?,?,?,?,?)', tupe)

# TODO: Location
# Gets jobs from snagajob.com and adds the information to a database
def getJobsFromSnagajob(url):
    web_id = 2
    # Try to connect to website URL
    try:
        html = urlopen(url)
    # If it can not connect
    except AttributeError as e:
        print("Error:")
        print(e)
        return None
    # Try to parse the web page into a beautifulsoup object
    try:
        bsObj = BeautifulSoup(html, "html.parser")
    # If it cant create a beautifulsoup object
    except AttributeError as e:
        print("Error:")
        print(e)
        return None

    web_id = 2
    # <h2 class="result-title">
    titleList2 = bsObj.findAll("h2", {"class": "result-title"})
    # Company name is stored in <div> </div> tags
    # TODO: figure out how to scrape for companies
    #companyList2 = bsObj.findAll("div", {"class": "company"})
    # <span class="location text-muted">
    locationList2 = bsObj.findAll("span", {"class": "location text-muted"})
    # <small class = text-success updated">
    dateList2 = bsObj.findAll("small", {"class": "text-success updated"})
    titles2 = []
    companies2 = []
    locations2 = []
    dates2 = []

    # Titles
    for name in titleList2:
        # Adds title to titles list
        titles2.append(name.get_text().strip())

    # Companies
    #for name in companyList:
        # Adds company name to companies list
    #    companies.append(name.get_text().strip())

    # Locations
    for name in locationList2:
        # Adds location to location list
        locations2.append(name.get_text().strip())

    # Dates
    for name in dateList2:
        # Adds date to date list
        dates2.append(name.get_text().strip())
    x = 0
    # Used to figure out limiting factor for the for loop
    #print(len(titles2))
    #print(len(locations2))
    #print(len(dates2))

    for x in range(0, 14):
        tupe = [(x, web_id, titles2[x], locations2[x], 'Coming Soon!', dates2[x])]
        print(tupe)
        c.executemany('INSERT INTO jobs VALUES(?, ?, ?, ?, ?, ?)', tupe)


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


# Gets results

#print("**********Monster**********")
# Every time this gets run it adds all the data to the database,
# No point in running it more than once because it just adds the same
# Data set every time
#getJobsFromMonster(monster)

#print("**********SnagAJob**********")
#getJobsFromSnagajob(snagajob)

#print("**********Indeed**********")
#getJobsFromIndeed(indeed)
#print("**********ZipRecruiter**********")
#getJobsFromZipRecruiter(ziprecruiter)

# Print database contents
for row in c.execute('SELECT * FROM jobs ORDER BY web_id'):
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