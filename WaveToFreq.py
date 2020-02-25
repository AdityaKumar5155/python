import sqlite3
import datetime

#Creates a .sqlite file for saving History
conn = sqlite3.connect("History.sqlite")
cur = conn.cursor()
try:
    cur.execute('''CREATE TABLE IF NOT EXISTS "History"(
    	"ID"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    	"Date"	TEXT,
    	"Wavelength"	TEXT,
    	"Frequency"	TEXT
    )''')
except:
    print('Error : 01')
    quit()


while True:
    datetime=datetime.datetime.now() #Refreshes date at every new loop(NOT WORKING)

    print(datetime)

    #converting Wavelength to Frequency

    wl = input("Enter Wavelength: ")

    print(wl+" m")

    try:
        base = wl.split("*")[0]
    except:
        base = 1

    try:
        power = wl.split("^")[1]
    except:
        power = 0

    fq = 299792458/((float(base))*10**(float(power)))

    count = len(str(fq).split(".")[0])

    if count != 1:
        try:
            fq = str(fq/10**(count-1))[:7]+"*10^"+str(count-1)+" Hz"
        except:
            fq = str(fq/10**(count-1))+"*10^"+str(count-1)+" Hz"
    else:
        try:
            fq = str(fq/10**(count-1))[:7]+" Hz"
        except:
            fq = str(fq/10**(count-1))+" Hz"

    print(fq)

    #storing History

    cur.execute('''INSERT OR IGNORE INTO History (Date, Wavelength, Frequency)
    VALUES ( ?, ?, ? )''', (datetime, wl, fq))
    conn.commit()
conn.close()
