class grade :
     def __init__(self,grade):
	self.grade = grade
     def grade_input(self):
	self.student = int(input("enter your grade: ")
     def print_grade(self):
	if self.student >= 90 :
	  print ("you got A grade")
	elif self.student >= 50 :
	  print ("you got C grade")
	elif self.student >= 70 :
	  print ("you got B grade")
	else :
	   print ("you just pass")

student1 = grade("")
student1 = grade_input()
student1 = print_grade()
