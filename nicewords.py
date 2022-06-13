import sys
sys.path.append("/home/rakaut/containers/webbuilder/modules")
import base64
import dbConn as db
import urllib.request


page = urllib.request.urlopen('https://www.affirmations.dev/')
text=page.read()


print(str(text))

#decodedstring=base64.b64decode(text).decode('utf-8')
#print(decodedstring) 
