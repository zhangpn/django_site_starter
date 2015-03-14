import sys,os
import csv
from importData.models import ZipCode

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

# Full path and name to the csv data file
csv_filepathname = os.path.join(BASE_DIR, 'data.csv')

# Full path to django project directory
djangoproject_home = os.path.join(BASE_DIR, '..')

sys.path.append(djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')

for row in dataReader:
    if row[0] != 'ZIPCODE': # Ignore the header row, import everything else
        zipcode = ZipCode()
        zipcode.zipcode = row[0]
        zipcode.city = row[1]
        zipcode.statecode = row[2]
        zipcode.statename = row[3]
        zipcode.save()