# Write a Pandas program to create
# a) Date time object for Jan 15 2012.
# b) Specific date and time of 9:20 pm.
# c) Local date and time.
# d) A date without time.
# e) Current date.
# t) Time from a date time.
# g) Current local time.
import pandas as pd
import datetime

dt_a = pd.Timestamp('2006-11-30')
print("a) Date time object for Nov 30 2006:", dt_a)

dt_b = pd.Timestamp('2006-11-30 1:00:00')
print("b) Specific date and time of 1:00 pm:", dt_b)

dt_c = pd.Timestamp.now()
print("c) Local date and time:", dt_c)

dt_d = pd.Timestamp(datetime.date(2006, 11, 30))
print("d) A date without time:", dt_d.date())

dt_e = pd.Timestamp.today().date()
print("e) Current date:", dt_e)

dt_f = pd.Timestamp.now().time()
print("f) Time from a date time:", dt_f)

dt_g = datetime.datetime.now().time()
print("g) Current local time:", dt_g)
