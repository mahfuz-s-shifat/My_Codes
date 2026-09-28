# Date & TIme 

# import datetime

# print(datetime.datetime.now())


from datetime import datetime, date, time

this_moment = datetime.now()

print(this_moment)
print(this_moment. second)

birth = datetime(2025, 5, 2, 8, 3, 15)
print(birth)

a = date.today()
print(a)



#Time Delta


from datetime import datetime

ekhon = datetime.now()

print(ekhon.strftime("%B %d,%Y")) # September 28, 2026



