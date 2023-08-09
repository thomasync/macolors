import sys

from macolors.macolors import Macolors


def main():
    try:
        macolors = Macolors()
        macolors.get_arguments(sys.argv)

        if macolors.arguments.command:
            macolors.get_from_command()
        else:
            macolors.get_from_stdin(sys.stdin)

    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
