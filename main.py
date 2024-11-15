import tkinter as tk
#Homescreen creation
homescreen = tk.Tk()
homescreen.geometry("600x500")
homescreen.title("home")
homescreen.withdraw()
#Work screen
work=tk.Tk()
work.geometry("600x500")
work.title("work")
work.withdraw()
#Streak Screen
streakscreen = tk.Tk()
streakscreen.geometry("600x500")
streakscreen.title("streak")
streakscreen.withdraw()

#setting up the app
app = tk.Tk()
app.geometry("640x640")
app.title("FutureEdApp")





# Change the label text 
def show(): 
  global drop,button
  if chosenscreen.get() == "list":
    homescreen.deiconify()
    streakscreen.withdraw()
    work.withdraw()
  elif chosenscreen.get() == "streak":
    work.withdraw()
    homescreen.withdraw()
    
    streakscreen.deiconify()
    
  elif chosenscreen.get() == "work":
    streakscreen.withdraw()
    homescreen.withdraw()
    work.deiconify()
    
    

  
    
    
  
# Dropdown menu options 
options = [ 
  "list",
  "streak",
  "work"
] 

# datatype of menu text 
chosenscreen = tk.StringVar() 

# initial menu text 
chosenscreen.set( "Menu" ) 



# Create Dropdown menu 
drop = tk.OptionMenu( homescreen , chosenscreen , *options ).pack() 
drop1 = tk.OptionMenu( streakscreen , chosenscreen , *options ).pack() 
drop2 = tk.OptionMenu( work , chosenscreen , *options ).pack()

# Create button, it will change label text 
button = tk.Button( homescreen, text = "Go" , command = show ).pack() 
button1 = tk.Button( streakscreen, text = "Go" , command = show ).pack() 
button2 = tk.Button( work, text = "Go" , command = show ).pack() 


#MENU BUTTON



#Main Label
mainarr=["I","g","l","o","o", " ", "P","r","i","o","r","i","t","i","e","s"]
main_label = tk.Label(master=app, compound="center", anchor="center")
main_label.configure(text="".join(mainarr) , font=("Roboto", 50))

mainlabeltext=""
x=0
#typewritter animation
def typewriter():
  global mainarr,mainlabeltext,x
  if x < len(mainarr):
    mainlabeltext+=mainarr[x]
    main_label.configure(text=mainlabeltext)
    main_label.place(relx=0.5, rely=0.5, anchor="center")
    x+=1
    app.after(200,typewriter)
    
typewriter()
#First Screen 


#start button code
def startscreen(): 
  homescreen.deiconify()
  app.destroy()
 
startbutton=tk.Button(master=app, text="Start", command=startscreen)
startbutton.place(relx=0.5, rely=0.6, anchor="center")
#Priority list
#priority Label


prioritylab = tk.Label(master=homescreen, compound="center", anchor="center",text="Igloo's Priority List", font=("Roboto", 20))
prioritylab.place(relx=0.5,rely=0.3,anchor="center")
#Text input

priorityList=tk.Entry(master=homescreen)
priorityList.place(relx=0.5, rely=0.7, anchor="center")

#Priority list function
priorityInstructions = tk.Label(master=homescreen, compound="center", anchor="center",text="", font=("Roboto", 10))
priorityInstruct = tk.Label(master=homescreen, compound="center", anchor="center",text="Your Priorities in order are:", font=("Roboto", 10))

priority=[]

arrtxt=""

def prioritylist():
  global arrtxt
  priority.append(priorityList.get())#e
  for i in range(0,len(priority)):
      arrtxt=arrtxt + " " +priority[i]
      priority.remove(priority[i])
  priorityInstructions.configure(text="Your tasks are: " + beans)
  priorityInstructions.place(relx=0.5,rely=0.4, anchor="center" )
  deletebutton.place(relx=0.5,rely=0.84, anchor ="center")



def clear():
  global priorityInstructions,arrtxt
  arrtxt=""
  priorityInstructions.configure(text="")
  priorityInstructions.place(relx=0.5,rely=0.4, anchor="center" )


deletebutton=tk.Button(master=homescreen, text="Clear Tasks",command=clear)



#priority button
prioritybutton=tk.Button(master=homescreen, text="add your tasks on the list based on their priority, add your number one priority first and so on", command=prioritylist)

prioritybutton.place(relx=0.5, rely=0.78, anchor="center")



#WORK SCREEN

time=0
workTimeLabel=tk.Label(master=work, compound="center", anchor="center",text="", font=("Roboto", 20))
btime=0

def worktime():
  
  global workTimeLabel,time,rtime,seconds,btime,brtime,second
  if time<15:
    work.after(1000,worktime)
    time+=1
    rtime=15-time
    seconds=rtime%60
    workTimeLabel.configure(text="25 minute work period "+str(int(ting/60))+" Minutes " + str(seconds)+" seconds")
    workTimeLabel.place(relx=0.5,rely=0.5, anchor="center")
    btime=0
  else:
    if btime<3:
      work.after(1000,worktime)
      btime+=1
      brtime=3-btime
      second=brtime%60
      workTimeLabel.configure(text="5 minute break "+str(int(brtime/60))+" Minutes "+str(second) +" Seconds")
      workTimeLabel.place(relx=0.5,rely=0.5, anchor="center")
    elif brtime==0 and second==0:
      time=0
  
  
    
workbutton=tk.Button(work,command=worktime,text="start timer").pack()
#StreaksCreent
streaklabel = tk.Label(master=streakscreen, compound="center", anchor="center",text=
                       "Congrats you've worked for 68 days in a row!", font="Roboto")
streaklabel.place(relx = 0.5, rely = 0.5, anchor="center")



app.mainloop()