import sqlite3

themes = {
'espemlakv10' : "C:\\Users\\mfurk\\Desktop\\domain_infos\\info.txt"
}
#python domain_create.py "C:\\Users\\mfurk\\Desktop\\deneme.db"
class Create_Site():
    def __init__(self):
        pass
    def save_info(self,id_k,db):
        global infos
        infos = {}

        baglanti = sqlite3.connect(db)
        cursor = baglanti.cursor()

        cursor.execute("Create Table If not exists domains (id	INTEGER PRIMARY KEY AUTOINCREMENT,domain TEXT,username TEXT, password TEXT, theme TEXT)")
        baglanti.commit()

        cursor.execute("SELECT * FROM domains WHERE id={}".format(id_k))
        data = cursor.fetchone()
        try:
            infotxt = themes[str(data[4])]
        except TypeError:
            print("**********\nDB HATASI, DOSYA YOLU HATALI\n**********")

        domain_info=locals()
        f = open(infotxt, "r")
        contents = ""
        for line in f: 
            contents += line.strip()
        exec(contents,globals(),domain_info)

        f.close()
        
        raw_cwd = infotxt.split(chr(92))
        raw_cwd.pop(-1)
        cwd = ""
        for i in range(0,len(raw_cwd)):
            cwd +=  raw_cwd[i] + chr(92) + chr(92)
            
        cursor.execute("SELECT * FROM domains")
        count = cursor.fetchall()
        count = len(count)
        
        infos.update({'domain' : data[1]})
        infos.update({'username' : data[2]})
        infos.update({'password' : data[3]})
        infos.update({'zip_file' : domain_info['domain_info']['zip_file'].format(cwd=cwd)})
        infos.update({'sql_file' : domain_info['domain_info']['sql_file'].format(cwd=cwd)})
        infos.update({'conf_file' : domain_info['domain_info']['conf_file'].format(cwd=cwd)})
        infos.update({'conf_number' : domain_info['domain_info']['conf_number']})
        infos.update({'conf_name' : domain_info['domain_info']['conf_name']})
        infos.update({'row_count' : int(count)})
        
    def read_info(self,sira):
        return infos[str(sira)]
    
