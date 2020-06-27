import pymysql.cursors
connection = pymysql.connect(host='egitimplatformu.org',
                             user='root',
                             password='Smfm1980***',
                             db='dbname',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
