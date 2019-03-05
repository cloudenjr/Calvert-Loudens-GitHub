import pytz
import datetime

# country = 'Europe/Moscow'
#
# tz_to_display = pytz.timezone(country)
# local_time = datetime.datetime.now(tz=tz_to_display)
# print("The time in {} is {}".format(country, local_time))
# print("UTC is {}".format(datetime.datetime.utcnow()))
#
# # for x in pytz.all_timezones:    # IMPORTANT!!!: Very useful code for what you are attempting with your dad's farm
# #     print(x)
# #
# # for x in sorted(pytz.country_names):
# #     print(x + ": " + pytz.country_names[x])
# #
# # for x in sorted(pytz.country_names):
# #     print("{}: {}: {}".format(x, pytz.country_names[x], pytz.country_timezones.get[x]))
#
# for x in sorted(pytz.country_names):
#     print("{}: {}".format(x, pytz.country_names[x]), end=': ')
#     if x in pytz.country_timezones:
#         for zone in sorted(pytz.country_timezones[x]):
#             tz_to_display = pytz.timezone(zone)
#             local_time = datetime.datetime.now(tz=tz_to_display)
#             print("\t\t{}: {}".format(zone, local_time))
#     else:
#         print("\t\tNo time zone defined.")
#
# *********************************************************************************************************************
# converting local time back to UTC... because of the inability to work backwards, its best to convert date/time
# to UTC time, do your arithmetic then conversion, and display the time back to the users in local time
#
import pytz
import datetime

local_time = datetime.datetime.now()
utc_time = datetime.datetime.utcnow()

print("Naive local time {}".format(local_time))
print("Naive UTC {}".format(utc_time))

aware_local_time = pytz.utc.localize(utc_time).astimezone()
aware_utc_time = pytz.utc.localize(utc_time)

print("Aware local time {}, time zone {}".format(aware_local_time, aware_local_time.tzinfo))
print("Aware UTC {}, time zone {}".format(aware_utc_time, aware_utc_time.tzinfo))

gap_time = datetime.datetime(2015, 10, 25, 1, 30, 0, 0)
print(gap_time)
print(gap_time.timestamp())

s = 1445733000
t = s + (60 * 60)

gb = pytz.timezone('GB')
dt1 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(s)).astimezone(gb) # fromtimestamp is for local time
dt2 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(t)).astimezone(gb)

print("{} seconds since the epoch is {}".format(s, dt1))
print("{} seconds since the epoch is {}".format(t, dt2))
