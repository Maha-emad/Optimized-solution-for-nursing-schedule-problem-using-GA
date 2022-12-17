# Optimized solution for nursing schedule problem using GA  

Scheduling the right nursing staff will improve the performance and quality of the nursing unit. 
Proper scheduling will help recruitment, nurse preferences, and maintain an overtime budget for a logical nurse.
The most important thing in scheduling is increasing the nurse's spirit and ensuring patient safety. 
NSP can be solved by using several methods, one of them is using a genetic algorithm (GA), GA is an effective and optimal method in solving nurse scheduling problems. The
results obtained is an optimal schedule that is the schedule does not violate the rules that have been determined by the hospital and the constraints of nurses as well( ex, nurses cant have a night shift followed by a morning shift) , we run it on a simple model of 20 nurses.  

The main functionality : 

 a) From user perspective:  
  
   A schedule will be displayed to the user and he can observe the
   nurse scheduling table in the GUI.
   
  b) From Programmer prospective :
   
   
  Function initialize (class schedule)
  For loop to loop on nurses
  If (pref=1)
  Start list of shift with the preferred one

 Self.day= list [shift, number of patients, skill]
 else
countskill = countskill+1
if countskill =5
call getskill function
 countskill=1
nurse_data = []
For loop to loop on days
Days=[]
Append shift
If shift =4
Shift=0
4
Append skill
If day = dayoff
Append skill = 0
number of patients
if self.day[0]=off
self.day.append(0)
else
self.day.append(random (1- max number of patients/nurse)
self.nurse_data[j][0] = ‘e’
Schedule.append(self.nurse_data)
Return
Self.schedule 

Personal contribution : 
I was responsible for developing the fittenes function as well as the genatic algorithm class  

Used tools : 
IDEs: Pycharm and Jupyter.
Libraries: Prettytable and tkinter
Programming language: python 

Advantages:

Printable table of the best population and utilization of genetic algorithm is
met successfully. 

Disadvantages:

There are no many features in the GUI. The algorithm works only for
small-scaling and medium-scaling data.
Future modifications:
Introducing more features to the GUI such as deleting user and using more
advanced approaches for large scaling data 


![Screenshot (180)](https://user-images.githubusercontent.com/71048834/208254841-adf14e37-8909-421d-9b62-78ca1d1ea5ff.png)





