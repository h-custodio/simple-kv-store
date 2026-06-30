
# Consider dispatch table later on

def execute(store, command, args) -> Result:

    if command == "SET" and len(args) == 2:
        store.set(args[0], args[1])
        return Result(success=True, value="Success", appendable=True)

    if command == "GET" and len(args) == 1:
        if not store.exists(args[0]):
            return Result(success=False, error="this key does not exist")

        return Result(success=True, value=store.get(args[0]))

    if command == "DEL" and len(args) == 1:
        if not store.exists(args[0]):
            return Result(success=False, error="this key does not exist")
        
        store.delete(args[0])
        return Result(success=True, value=args[0] + " has been deleted", appendable=True)

    if command == "SHOW":
            return Result(success=True, value=store.show())

    if command == "PING":
        return Result(success=True, value="Pong")
    
    if command == "QUIT":
        raise SystemExit("Stopping program")
        
    else:
        return Result(success=False, error="command unknown") 
    

def parse(string: str):
    if string == "":
        print("this string cannot be empty")
        return
    
    return string.split()
    

# move into different file as system scales

class Result:
    def __init__(self, 
        success: bool, 
        value: any | None = None, 
        error: str | None = None, 
        appendable: bool = False):

        self.success = success
        self.value = value
        self.error = error
        self.appendable = appendable


