from datetime import datetime,date

myDate = datetime(2022,8,9,19,59,24)
print(myDate)

myDate = myDate.replace(month=11)
print(myDate)

birth = date(1995,3,5)
death = date(2078,6,11)

life = death - birth

print(life.days)

awake = datetime(2022,10,5,7,30)
sleep = datetime(2022,10,5,23,45)

wake = sleep - awake

print(wake.seconds)