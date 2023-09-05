from tkinter import *

codsoft = Tk()
codsoft.title("TO DO LIST")
codsoft.geometry("400x650")
codsoft.resizable(False,False)

task_list = []
def addTask():
    task = task_entry.get()
    task_entry.delete(0,END)

    if task:
        with open("tasklist.txt","a") as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END,task)
def deleteTask():
    global task_list
    task = str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt","w") as taskfie:
            for task in task_list:
                taskfie.write(task+"\n")
        listbox.delete( ANCHOR)

def openTaskFile():
    try:
        global task_list
        with open("task.txt","r") as taskfile:
            tasks = taskfile.readline()

        for task in tasks:
            if task != "\n":
                task_list.append(task)
                listbox.insert(END,task)
    except:
            file=open("tasklist.txt","w")
            file.close()

#icon
Image_icon = PhotoImage(file="Pic/task.png")
codsoft.iconphoto(False,Image_icon)

#top bar
topimage = PhotoImage(file="Pic/topheader.jpg")
Label(codsoft,image=topimage).pack()

#dockimage
dockimage = PhotoImage(file="Pic/dock.png")
Label(codsoft,image=dockimage,bg="#32405b").place(x=30,y=25)

noteimage = PhotoImage(file="Pic/task.png")
Label(codsoft,image=noteimage,bg="#48a4fc").place(x=30,y=25)

heading = Label(codsoft,text="All TASK",font="Times 20 bold",fg="white",bg="#48a4fc")
heading.place(x=120,y=20)

#main
frame = Frame(codsoft,width=400,height=50,bg="white")
frame.place(x=0,y=180)

task = StringVar()
task_entry = Entry(frame,width=18,font="arial 20",bd=0)
task_entry.place(x=10,y=7)
task_entry.focus()
button = Button(frame,text="ADD",font="arial 20 bold",width=6,bg="#1484f7",fg="#fff",bd=0,command=addTask)
button.place(x=300,y=0)

#listbox
frame1 = Frame(codsoft,bd=3,width=700,height=280,bg="#1484f7")
frame1.pack(pady=(160,0))

listbox = Listbox(frame1,font=("arial",12),width=40,height=16,bg="#1484f7",fg="white",cursor="hand2",selectbackground="red")
listbox.pack(side=LEFT,fill=BOTH,padx=2)

scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT,fill= BOTH)

#listbox
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# openTaskFile()
delete_icon = PhotoImage(file="Pic/delete.png")
Button(codsoft,image=delete_icon,bd=0,command=deleteTask).pack(side=BOTTOM,pady=13)
codsoft.mainloop()
