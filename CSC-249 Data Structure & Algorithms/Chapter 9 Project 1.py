# Creates a dictionary with course & room numbers
roomNumbers={'CS101':'3004', 'CS102':'4501', 'CS103':'6755', 'NT110':'1244', 'CM241':'1411'}

# Creates a dictionary containing course numbers and names of the instructors
instructorCourse={'CS101':'Haynes', 'CS102':'Alvarado', 'CS103':'Rich', 'NT110':'Burke', 'CM241':'Lee'}

# Dictionary containing course numbers and the meeting times
meetingtime={'CS101':'8:00am', 'CS102':'9:00am', 'CS103':'10:00am', 'NT110':'11:00am', 'CM241':'1:00pm'}

#Prompt the user to enter the course number.
courseNumber=input("Enter a class name:")

#prints the class number
print("Class:",courseNumber)

#prints the Course Room Number
print("Room:",roomNumbers[courseNumber])

#prints the instructor and course
print("Instructor:",instructorCourse[courseNumber])

#prints meeting time
print("Time:",meetingtime[courseNumber])