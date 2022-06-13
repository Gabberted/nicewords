import sys
sys.path.append("/home/rakaut/containers/webbuilder/modules")
import base64
import dbConn as db
import urllib.request


page = urllib.request.urlopen('https://www.affirmations.dev/')
btext=page.read()


text = btext.decode('utf-8')
text=text.replace("{","").replace("b'","").replace("}","")
print(str(text))

#decodedstring=base64.b64decode(text).decode('utf-8')
#print(decodedstring) 
