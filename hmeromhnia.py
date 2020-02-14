import datetime
day = int(input('Enter a day'))
month = int(input('Enter a month'))
year = int(input('Enter a year'))

date1 = datetime.date(year, month, day)


from datetime import date

d0 = date.today()
delta = date1 - d0


d = datetime.date.today()
type(d.month)
type(d.year)

from datetime import datetime

now = datetime.now().time()
type(now.minute)
type(now.hour)


s=int(11-now.hour*0.1)
s2=int(60-now.minute-1)
s3=60-now.second
print("η ημερομηνία αυτή είναι σε ",delta.days-1, "μερες,",s,"ώρες,",s2,"λεπτά και",s3,"δευτερόλεπτα")
if year%4==0 and d.year%100!=0:
    x=1
        
elif year%400==0:
    x=1
else:
    x=0

if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
  print("Αυτός ο μήνας έχει 31 μέρες")
elif month==2 and x==1:
   print("Αυτός ο μήνας έχει 29 μέρες")
elif month==2 and x==0:
   print("Αυτός ο μήνας έχει 28 μέρες")   
else:
  print("Αυτός ο μήνας έχει 30 μέρες")

