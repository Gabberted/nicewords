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
strQ=f"select count(*) from  nicewords where type='{sp_Text[0]}' and values='{sp_Text[1]}'"
print(strQ)
strCount=db.returnFetchall(strQ)[0]
print("strCount: {strCount}")
if strCount == "0":
    print("Entry not found, storing")
    strQ=f"insert into nicewords(type,line)values('{sp_Text[0]}','{sp_Text[1]}')"
    db.NoReturnQuery(strQ)
else:
    print(f"{sp_Text[1]} already stored, skipping")

#decodedstring=base64.b64decode(text).decode('utf-8')
#print(decodedstring) 
