
def execute(store, command, args):
    if command == "SET" and len(args) == 2:
        store.set(args[0], args[1])
        return "OK"

    elif command == "GET" and len(args) == 1:
        exist = store.show()

        if args[0] not in exist:
            print("this key does not exist")
            return None
        else:
            return store.get(args[0])

    elif command == "DEL" and len(args) == 1:
        exist = store.show()

        if args[0] not in exist:
            print("this key does not exist")
            return None
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
        print("command unknown")
        return None 

def parse(string):
    if string == "":
        return
    else:
        return string.split()
    

# move into different file as system scales

class Result:
    def __init__(self):
        success: bool
        value: str | None = None
        error: str | None = None
        appendable: bool