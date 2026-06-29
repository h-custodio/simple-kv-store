from kv_store import KVStore
import commands as c

# Issues to address: parser logic is still fragile
# YOU ARE WORKING IN THE PERSISTENCE BRANCH RN #

# Consider adding this later on
# from pathlib import Path

# log_file = Path(__file__).parent / "log.txt"

# with open(log_file, "a") as f:
#     f.write("log entry\n")

def repl(store):
    while True:
        print("$ ", end="")

        input_string = input("input: ")
        input_string = c.parse(input_string)

        if input_string is None:
            print("input cannot be empty")
            continue

        command = input_string[0].upper()
        args = input_string[1:]

        result = c.execute(store, command, args)
        if result is not None:
            print(result)


def main():
    store = KVStore()

    print(
        "COMMANDS: SET, GET, DEL, SHOW, or QUIT to exit\n" \
        "EXAMPLE: SET age 20\n" \
        "EXAMPLE: GET name\n" \
        "EXAMPLE: DEL age\n")
    repl(store)

if __name__ == "__main__":
    main()