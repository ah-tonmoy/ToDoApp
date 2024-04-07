import sys

def add(item):
    f = open("todo.txt", 'a')
    f.write(item)
    f.write('\n')
    f.close()
    print("Item added successfully")

def ls():
    try:
        updateUtility()
        l = 1
        for key in d:
            item = str(l) + "." + d[key]
            print(item)
            l += 1
    except:
        print("Unable to list items")

def done(no):
    try:
        updateUtility()
        numberOfToDoItems = len(d)
        no = int(no)
        if(no > numberOfToDoItems):
            return    
        
        file = open("done.txt", 'a')
        file.write(d[no])
        file.write("\n")

        with open("todo.txt", "r+") as files:
            toDoItems = files.readlines()
            files.seek(0)
            for item in toDoItems:
                line = item.strip('\n')
                if line != d[no]:
                    files.write(item)
            files.truncate()
        message = "Item " + str(no) + " has been marked as done"
        print(message)
    except:
        print("Unable to mark to do ites as done")


def report():
    try:
        doneItems = open("done.txt", 'r')
        count = 1

        for item in doneItems:
            item = item.strip('\n')
            output = str(count) + "." + item
            print(output)
            count += 1
    except:
        print("No items has been completed yet")

def updateUtility():
    try:
        count = 1
        toDoItems = open("todo.txt", "r")
        for line in toDoItems:
            line = line.strip('\n')
            d.update({count: line})
            count += 1
    except:
        print("Error while reading file")

if(__name__ == '__main__'):
    try:
        d = {}
        args = sys.argv

        if(args[1] == 'add' and len(args[2:]) == 0):
            print("Error: Missing todo string. Nothing added!")
        elif(args[1] == 'done' and len(args[2:]) == 0):
            print("Error: Missing NUMBER for marking todo as done.")
        else:
           globals()[args[1]](*args[2:])
    except:
        print("Please try again")