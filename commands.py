
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
    
    if command == "QUIT":
        raise SystemExit("Stopping program")
        
    else:
        return Result(success=False, error="command unknown") 
    

def parse(string: str):
    if string == "":
        print("this string cannot be empty")
        return
    
    return string.split()

def log(command, args):
    with open("log.txt", "a") as f:
        f.write(command + " " + " ".join(args) + "\n")

def reconstruct(store):
    with open("log.txt", "r") as file:
        for line in file:
            parsed_line = line.split()

            command = parsed_line[0]
            args = parsed_line[1:]

            execute(store, command, args)










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


