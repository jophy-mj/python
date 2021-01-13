from datetime import date;
last_year=int(input("Enter the last year:"))
current_date=date.today()
current_year=current_date.year
print("Leap years from",current_year,"to",last_year,"is:")
for i in range(current_year,last_year+1):
              if((i%400==0)or((i%4==0)and(i%100!=0))):
                      print(i)
              
