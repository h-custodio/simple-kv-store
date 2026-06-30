from kv_store import KVStore
import commands as cmd


def repl(store):
    while True:
        print("$ ", end="")

        input_string = input("input: ")
        input_string = cmd.parse(input_string)

        if input_string is None:
            print("input cannot be empty")
            continue

        command = input_string[0].upper()
        args = input_string[1:]

        result = cmd.execute(store, command, args)
        if not result.success:
            print(result.error)
        else:
            print(result.value)

            if result.appendable:
                cmd.log(command, args)


def main():
    store = KVStore()

    try:
        cmd.reconstruct(store)
    except FileNotFoundError:
        print("No existing log. Starting Fresh\n")

    print(
        "COMMANDS: SET, GET, DEL, SHOW, or QUIT to exit\n" \
        "EXAMPLE: SET age 20\n" \
        "EXAMPLE: GET name\n" \
        "EXAMPLE: DEL age\n")
    repl(store)

if __name__ == "__main__":
    main()
