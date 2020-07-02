#create a Health manage ment project for 3 clients, create files for their diet & exercise
#write a fn which takes input as client name when executed, one more fn to retieve diet or food
#use also current time of diet
#means data ko log krna h
#log mtlb data ko enter krna h timestamp pr

client_list = {1:"Sarthak", 2:"Mausam", 3:"John"}
log_list = {1:"Exercise", 2:"Diet"}

def getdate():
    import datetime
    return datetime.datetime.now()


try:
    print("Welcome Select Client Name: ")
    for key, value in client_list.items():
        print("Press", key, "for", value,"\n", end="")
    client_name = int(input())
    print("Selected Client : ", client_list[client_name], "\n", end="")

    print("Press 1 for Log")
    print("Press 2 for Retrieve")
    op = int(input())

    if op is 1:
        for key, value in log_list.items():
            print("Press", key, "to lock", value,"\n", end="")
        log_name =  int(input())
        print("Selected Job : ", log_list[log_name])

        f = open(client_list[client_name] + "_" + log_list[log_name] + ".txt", "a")
        k = 'y'
        while(k is not "n"):
            print("Enter", log_list[log_name], "\n", end="")
            mytext = input()
            f.write("[ " + str(getdate()) + " ] : " + mytext + "\n")
            k = input("ADD MORE ? y/n:")
            continue
        f.close()

    elif op is 2:
        for key, value in log_list.items():
            print("Press", key, "to retrieve", value,"\n", end="")
        lock_name =  int(input())
        print(client_list[client_name], "-", log_list[log_name], "Report :","\n", end="")

        f = open(client_list[client_name] + "_" + log_list[log_name] + ".txt", "rt")
        contents = f.readlines()
        for line in contents:
            print(line, end="")
        f.close() 

    else:
        print("Invalid Input !!!")

except Exception as e:
    print("Wrong Input !!!")