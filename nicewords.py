import sys
sys.path.append("/home/rakaut/containers/webbuilder/modules")
import base64
import dbConn as db
import urllib.request


page = urllib.request.urlopen('https://www.affirmations.dev/')
btext=page.read()


text = btext.decode('utf-8')
text=text.replace("{","").replace("b'","").replace("}","").replace('"','')
print(str(text))
sp_Text=text.split(":")
strQ=f"insert into nicewords(type,line)values('{sp_Text[0]}','{sp_Text[1]}')"
print(strQ)
#decodedstring=base64.b64decode(text).decode('utf-8')
#print(decodedstring) 
