# Author: Dana Zhang
# Creation Date: 3/14/2015
# How to use: run `python3 ./path/to/script.py path/to/sqlscriptfile.sql path/to/dbfile.sqlite` to execute sql scripts to selected database
# The following are commands used to view tables in the database file db.sqlite3
# sqlite3
# attach "db.sqlite3" as db1;
# .tables
# .exit


import sqlite3 as sqlite
import sys

if __name__ == "__main__":
    if (len(sys.argv) != 3):
        print ("\n\tRequires two arguments:")
        print ("\n\t\tRunSQLiteScript.py {scriptfilename} {databasefilename}\n\n")
        sys.exit()

    scriptfilename = sys.argv[1]
    dbfilename = sys.argv[2]

    try:
        print ("\nOpening DB")
        connection = sqlite.connect(dbfilename)
        cursor = connection.cursor()

        print ("Reading Script...")
        scriptFile = open(scriptfilename, 'r')
        script = scriptFile.read()
        scriptFile.close()

        print ("Running Script...")
        cursor.executescript(script)

        connection.commit()
        print ("Changes successfully committed\n")

    except getopt.GetoptError as e:
        print ("Something went wrong:")
        print (e)
    finally:
        print ("\nClosing DB")
        connection.close()