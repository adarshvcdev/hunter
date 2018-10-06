from bounce.models import Scrip
from bounce.serializers import ScripSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import csv

with open('nifty50.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        scrip = Scrip(ticker = row[2], name = row[0], index = "Nifty")
        scrip.save()
        print(row[0])
        # print(row[0])
        # print(row[2])

# snippet = Snippet(code='foo = "bar"\n')
# snippet.save()

# snippet = Snippet(code='print "hello, world"\n')
# snippet.save()