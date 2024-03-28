

# Name: Kizzie Trinh
# File Name: M02CaseStudy
# Description: This python code will ask a user to input their first and last name and ask for their GPA.
# based on their GPA will determine if they made it to Dean's List or Honor Roll.


## Welcoming Phase
print ("Welcome, please put in your last and first name and your current GPA")

## Asking user to input their first and last name
lastname = input ("What is your last name?: ") 
STOP = "zzz" or "ZZZ"
firstname = input ("What is your first name?: ")
currentgpa = float(input("What is your current GPA?: "))
studentcount = 5

## These If/Else functions checks to see if the gpa entered above is dean's list or honor roll for the above input
if currentgpa >= 3.50:
        print ("You made the Dean's List")  
        
elif currentgpa >= 3.25:
        print ("You  made the Honor Roll!")
    
else:
        print ("You did not make Honors Roll or Dean's List.")
        
# While loop keeps the code running till it breaks by a user entering "zzz or ZZZ" as the last name or till you're finish entering the students names
while lastname!= STOP:  
       
# Adding a break to the loop if lastname == STOP which is equal to "zzz or ZZZ" 
    if lastname == STOP:
        break

    if lastname != STOP:
        print ("Your Name:",lastname,",", firstname, ":" , "Current GPA:", currentgpa)
        
    lastname = input ("What is your last name?: ") 
    firstname = input ("What is your first name?: ")
    currentgpa = float(input("What is your current GPA?: "))
    
## These If/Else functions checks to see if the gpa entered above is dean's list or honor roll in the while loop
    if currentgpa >= 3.50:
        print ("You made the Dean's List")  
        
    elif currentgpa >= 3.25:
        print ("You  made the Honor Roll!")
    
    else:
        print ("You did not make Honors Roll or Dean's List.")
    


