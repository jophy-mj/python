class time:
    def __init__(self,hr,min,sec):
        self.hr=hr
        self.min=min
        self.sec=sec
    def __add__(self, other):
        return self.hr+other.hr,self.min+other.min,self.sec+other.sec
time1=time(2,30,45)
time2=time(3,45,50)
time3=time1+time2
print(time3)