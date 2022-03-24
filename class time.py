class Time():  #making a class as time
	def __init__(self, hours, mins): #using init function
		self.hours=hours
		self.mins=mins
	def addTime(t1, t2): #defining add time function to add two times
		t3=Time(0,0)
		if t1.mins+t2.mins > 60:
			t3.hours = (t1.mins+t2.mins)//60 #calculating hours condition
		t3.hours = t3.hours+t1.hours+t2.hours
		t3.mins = (t1.mins+t2.mins)-(((t1.mins+t2.mins)//60)*60) #calculating minutes condition
		return t3
	def displayTime(self): #display time function to print time on screen
		print ("Time is",self.hours,"hours and",self.mins,"minutes.")
	def displayMinute(self): #display minute function 
		print ((self.hours*60)+self.mins)

a = Time(int(input('enter t1 hours:')),int(input('enter t1 minutes:'))) #function calling , a is first time
b = Time(int(input('enter t2 hours:')),int(input('enter t2 minutes:'))) #function calling , b is second time
c = Time.addTime(a,b) #calling add time function
c.displayTime() #calling display time function
c.displayMinute() #calling displau minute function