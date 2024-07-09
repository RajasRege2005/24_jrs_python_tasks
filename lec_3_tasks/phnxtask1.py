from artphnxtask import logo
is_running=True
Tasks=[]
def add(task):
    if task in Tasks:
        file = open('phnxtask1.txt','a')
        file.write(f"\nCreation of \"{task}\"-unsuccessful")
        file.close()
        file=open('phnxtask1.txt','r')
        print(file.read())
    else:
        Tasks.append(task)
        file = open("phnxtask1.txt","a")
        file.write(f"\nCreation of \"{task}\"-successful")
        file.close()
        file=open("phnxtask1.txt","r")
        print(file.read())
def remove(task):
    if task in Tasks:
        Tasks.remove(task)
        file = open("phnxtask1.txt","a")
        file.write(f"\nRemoval of \"{task}\"-successful")
        file.close()
        file=open("phnxtask1.txt","r")
        print(file.read())
    else:
        file = open("phnxtask1.txt","a")
        file.write(f"\nRemoval of \"{task}\"-unsuccessful")
        file.close()
        file=open("phnxtask1.txt","r")
        print(file.read())
def search(task):
    if task in Tasks:
        file = open("phnxtask1.txt","a")
        file.write(f"\nSearch of \"{task}\"-successful")
        file.close()
        file=open("phnxtask1.txt","r")
        print(file.read())
    else:
        file=open("phnxtask1.txt","a")
        file.write(f"\nSearch of \"{task}\"-unsuccessful")
        file.close()
        file=open('phnxtask1.txt','r')
        print(file.read())
while is_running:
    print(logo)
    print("1.Add\n2.Remove\n3.Search\n4.Show all tasks\n5.Exit\nEnter your choice:")
    choice=input().lower()
    if choice=="add" or choice=="1":
        print("Enter the task to be added:")
        task=input()
        add(task)
        
    elif choice=="remove" or choice=="2":
        print("Enter task to be deleted:")
        task=input()
        remove(task)

    elif choice=="search" or choice=="3":
        print("Enter task to be searched:")
        task=input()
        search(task)

    elif choice=="show" or choice=="4":
        print(Tasks)

    elif choice=="exit" or choice=="5":
        is_running=False
        Tasks.clear()
        file = open("phnxtask1.txt","r+")
        file.seek(0)
        file.truncate()
        file.close()
    else:
        print("Choice entered is invalid, please enter again.")
        