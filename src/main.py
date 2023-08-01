import argparse


def say_goodbye(name):
    if name is None:
        print("Goodbye!")
        return

    print(f"Goodbye, {name}!")


def say_hello(name):
    if name is None:
        print("Hello!")
        return

    print(f"Hello, {name}!")


def get_likes(name):
    people = [{"name": "Json", "items": ["juul", "flower", "flour"]}]

    for person in people:
        if person["name"] == name:
            print(person["items"])


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command")

    hello_parser = subparsers.add_parser('sayHello')
    hello_parser.add_argument('name', nargs='?', default=None)

    goodbye_parser = subparsers.add_parser('sayGoodbye')
    goodbye_parser.add_argument('name', nargs='?', default=None)

    likes_parser = subparsers.add_parser('getLikes')
    likes_parser.add_argument('name', nargs='?')

    args = parser.parse_args()

    if args.command == "sayHello":
        say_hello(args.name)

    if args.command == "sayGoodbye":
        say_goodbye(args.name)

    if args.command == "getLikes":
        get_likes(args.name)


if __name__ == '__main__':
    main()
