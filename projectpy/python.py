#Python program to find the number of days between two given dates:--
#A date has date 'd', month 'm', year 'y'
class Date:
    def __init__(self,d,m,y):
        self.d=d
        self.m=m
        self.y=y
#To store number of days in all months from January to Dec.
monthDays=[31,28,31,30,31,30,31,31,30,31,30,31]

#This function counts number of leap years before the given date:
def countLeapYears(d):
    years=d.y

    #check if the current year needs to be considered for the count of the leap years or not

    if (d.m<=2):
        years-=1

    #An year is a leap year if it is a multiple of 4,multiple of 400 and not a  multiple of 100

    ans=int(years/4)
    ans-=int(years/100)
    ans+=int(years/400)
    return ans
#This function returns number of days between two given dates

def getDifference(dt1,dt2):
    #count total number of days before first date 'dt1'
    #initialize count using years and dates
    n1=dt1.y*365+dt1.d
    #Add days for months in given date for i in range(0,dt1.m-1):
    for i in range(0,dt1.m-1):
        n1+=monthDays[i]
    #Since every leap year is of 366 days
    #Add a day for every leap year
    n1+=countLeapYears(dt1)
    #similarly count total number of days before dt2
    n2=dt2.y*365+dt2.d
    for i in range(0,dt2.m-1):
        n2+=monthDays[i]
    n2+=countLeapYears(dt2)

    #return difference between two counts
    return(n2-n1)

#Driver code
dob=input("Enter your DOB as DD/MM/YYYY: ")
dob=[int(i) for i in dob.split("/")]
dob=Date(dob[0],dob[1],dob[2])
PD=input("Enter Present Day as DD/MM/YYYY: ")
PD=[int(i) for i in PD.split("/")]
PD=Date(PD[0],PD[1],PD[2])

#Function call
print("The number of days the person is alive: ",getDifference(dob,PD),"days")





