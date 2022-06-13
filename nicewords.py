import sys
sys.path.append("/home/rakaut/containers/webbuilder/modules")
import base64
import dbConn as db
import urllib.request


page = urllib.request.urlopen('https://www.affirmations.dev/')
page.read()


print(page.text)

decodedstring=str.decode('base64',page.text)
print(decodedstring) 
