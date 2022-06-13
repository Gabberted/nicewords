import sys
sys.path.append("/home/rakaut/containers/webbuilder/modules")

import dbConn as db
import urllib.request


page = urllib.request.urlopen('https://www.affirmations.dev/')
print(page.read())
