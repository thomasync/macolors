from macolors.macolors import Macolors
import sys


macolors = Macolors()
macolors.get_arguments(sys.argv)

try:
    if macolors.arguments.command:
        macolors.get_from_command()
    else:
        macolors.get_from_stdin(sys.stdin)

except KeyboardInterrupt:
    pass
