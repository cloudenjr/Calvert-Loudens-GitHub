# import pytz
# import pickle
import sqlite3



# db = sqlite3.connect("accounts.sqlite")
db = sqlite3.connect("accounts.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)

# for row in db.execute("SELECT * FROM history"):
for row in db.execute("SELECT strftime('%Y-%m-%d %H:%M:%f', history.time, 'localtime') AS localtime,"
                      "history.account, history.amount FROM history ORDER BY history.time"):
    # utc_time = row[0]
    # picked_zone = row[3]
    # zone = pickle.loads(picked_zone)
    # local_time = pytz.utc.localize(utc_time).astimezone(zone)
    # print("{}\t{}\t{}".format(utc_time, local_time, local_time.tzinfo))
    print(row)
    # utc_time = row[0]
    # local_time = ptyz.utc.localize(utc_time).astimezone()
    # # local_time = row[0]
    # print("{}\t{}".format(utc_time, local_time))

db.close()
