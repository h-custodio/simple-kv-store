
def execute(store, command, args):
    if command == "SET" and len(args) == 2:
        store.set(args[0], args[1])
        return "OK"

    elif command == "GET" and len(args) == 1:
        exist = store.show()

        if args[0] not in exist:
            return "this key does not exist"
        else:
            return store.get(args[0])

    elif command == "DEL" and len(args) == 1:
        exist = store.show()

        if args[0] not in exist:
            return "this key does not exist"
        else:
            store.delete(args[0])
            return args[0] + " has been deleted"

    elif command == "QUIT":
        raise SystemExit("Stopping program")
    
    elif command == "SHOW":
            return store.show()

    elif command == "PING":
        print("PONG")
        
    else:
        return "command unknown" 

def parse(string):
    if string == "":
        return
    else:
        return string.split()