import sys
sys.path.append("/home/rakaut/containers/webbuilder/modules")
import base64
import dbConn as db
import urllib.request


page = urllib.request.urlopen('https://www.affirmations.dev/')
btext=page.read()


text = btext.decode('utf-8')
text=text.replace("{","").replace("b'","").replace("}","").replace('"','').replace("'","''")
print(str(text))
sp_Text=text.split(":")
#strQ=f"select count(*) from  nicewords where type='%s' and line='%s'"
strQ=f"select count(*) from  nicewords where type='{sp_Text[0]}' and line='{sp_Text[1]}'"
print(str(db.returnFetchall(strQ)[0]))
strCount=str(db.returnFetchall(strQ)[0]).replace("(","").replace(")","").split(",")[0]
print(f"strCount: {strCount}")
if strCount == "0":
    print("Entry not found, storing")
    strQ=f"insert into nicewords(type,line)values('{sp_Text[0]}','{sp_Text[1]}')"
    print(strQ)
    try:
        conn=db.getConn()
        cursor = conn.cursor()
        print("Cursor fetched")
        cursor.execute(strQ)
        print("Execute  !")
        cursor.close()
        conn.commit()
        conn.close()
        print("Close")
        print("Entry stored")
    except Exception as ex:
        print(f"Error: {ex}")
else:
    print(f"{sp_Text[1]} already stored, skipping")

#decodedstring=base64.b64decode(text).decode('utf-8')
#print(decodedstring) 
