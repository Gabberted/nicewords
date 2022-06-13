import sys
sys.path.append("/home/rakaut/containers/webbuilder/modules")
import json
import dbConn as db
import urllib.request


page = urllib.request.urlopen('https://www.affirmations.dev/')
print(page.read())

y = json.dumps(page.read())
 
print(y)
print(type(y))
