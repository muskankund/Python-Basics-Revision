class fruits:  #making a fruit class
    total=0  #initialise counter
    def __init__(self,fno,fname,fcolor,fincolor,fshape,ftexture,ftaste,forigin,fsoiltype,fsoilph,fseedless,fgrowson):  #Constructor declared with number of arguments
        self.fno=fno  
        self.fname=fname  
        self.fcolor=fcolor  
        self.fincolor=fincolor
        self.fshape=fshape
        self.ftexture=ftexture
        self.ftaste=ftaste
        self.forigin=forigin
        self.fsoiltype=fsoiltype
        self.fsoilph=fsoilph
        self.fseedless=fseedless
        self.fgrowson=fgrowson
        fruits.total+=1  
    def displaytotal(self):  #function to display fruit 1 properties 
        print("No:",self.fno,"Fruite Name:",self.fname,",color:",self.fcolor,",inside color:",self.fincolor,',grows on:',self.fgrowson,',shape:',self.fshape,',texture:',self.ftexture,',taste:',self.ftaste,',origin:',self.forigin,',soil type:',self.fsoiltype,',soil ph:',',seedless variety:',self.fseedless)  
f1=fruits(1,"Apple","Red",'white','round','crunchy','sweet','central Asia','loam','6 to 7','No','Trees') #passing parameters
f2=fruits(2,"Mango","Yellow",'yellow','oval','fleshy','sweet','southern Asia','sandy','4.5 to 7','No','Trees')  #passing parameters
f1.displaytotal()    #calling the function
f2.displaytotal()    #calling the function
print("Total Number of Fruites %d" % fruits.total)  #printing total no. of fruits