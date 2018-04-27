import csv, sqlite3

con = sqlite3.connect("quran.db")
cur = con.cursor()
cur.execute("CREATE TABLE quran (id integer primary key, DatabaseID integer, SuraID integer, VerseID integer, AyahText text);") # use your column names h    ere

reader = csv.reader(open("indonesian.csv","rb"),delimiter=",")
for row in reader:
  to_db = [unicode(row[0],"utf8"), unicode(row[1],"utf8"), unicode(row[2],"utf8"), unicode(row[3],"utf8")]
  cur.execute("INSERT INTO quran (DatabaseID, SuraID, VerseID, AyahText) VALUES(?, ?, ?, ?);", to_db )

con.commit()
con.close()
