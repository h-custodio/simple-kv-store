from kv_store import KVStore
import commands as c

# TO REFACTOR
# Argument parsing logic is a bit fragile (it assumes fixed positions without validating command-specific requirements). 
# ^ think about option brancing (like inputting command first and having a custom response for each).

# NEXT STEP: Add persistance

def repl(store):
    while True:
        print("$ ", end="")

        input_string = input("input: ")

        if input_string == "":
            print("input cannot be empty")
            continue

        input_string = input_string.split()

        command = input_string[0].upper()
        args = input_string[1:]

        result = c.execute(store, command, args)
        if result is not None:
            print(result)        



def main():
    store = KVStore()

    print(
        "COMMANDS: SET, GET, DEL, PRINT, or QUIT to exit\n" \
        "EXAMPLE: SET age 20\n" \
        "EXAMPLE: GET name\n" \
        "EXAMPLE: DEL age\n")
    repl(store)

if __name__ == "__main__":
    main()