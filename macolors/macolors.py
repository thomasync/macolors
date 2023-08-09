import argparse
import subprocess
from io import StringIO

from macolors.input import Input


class Macolors:
    def __init__(self):
        self.input = Input()
        self.__parser = self.__get_parser()

        self.arguments = None

    def get_from_stdin(self, stdin):
        if not stdin or stdin.isatty():
            self.__parser.print_help()
            return

        for line in stdin:
            self.input.format(line)

    def get_from_command(self, command=None):
        command = self.__verify_command(command)

        process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            stdin=subprocess.DEVNULL,
            encoding="utf-8",
            errors="replace",
        )

        while True:
            output = process.stdout.readline()

            if output == "" and process.poll() is not None:
                break

            if output:
                self.input.format(output)

    def get_arguments(self, arguments, define_arguments=True):
        args, unknown = self.__parser.parse_known_args(arguments[1:])
        args.command = args.command + unknown
        self.arguments = args

        if define_arguments:
            self.define_arguments()

        return self.arguments

    def define_arguments(self):
        if self.arguments.scheme:
            self.input.set_scheme(self.arguments.scheme)
        elif self.arguments.json:
            self.input.set_json_scheme(self.arguments.json)

    def __get_parser(self):
        parser = argparse.ArgumentParser()

        schemes = [scheme["name"] for scheme in self.input.get_schemes()]
        parser.add_argument(
            "command",
            nargs="*",
            help="command to colorize",
        )

        group = parser.add_mutually_exclusive_group()
        group.add_argument(
            "-s",
            "--scheme",
            choices=schemes,
            help="Force schema to use. Allowed values are " + ", ".join(schemes),
            metavar="",
        )

        group.add_argument(
            "-a",
            "--force-auto",
            help="Force auto detection without using schemes",
            action="store_true",
            default=False,
        )

        group.add_argument(
            "--json",
            help="Allow to use json format to define scheme",
        )

        stream = StringIO()
        parser.print_usage(stream)
        usage = stream.getvalue().replace("usage: ", "")

        parser.usage = (
            f"{usage}or\nusage: [command ...] | {usage.replace('[command ...]', '')}"
        ).replace("  ", " ")

        return parser

    def __verify_command(self, command):
        if not command and not self.arguments.command:
            raise Exception("Command is required")

        if not command:
            command = self.arguments.command

        if len(command) == 1:
            command = command[0].split(" ")

        # TODO: SHOULD BE GENERIC TO BLOCK ALL INTERACTIVE COMMANDS
        blacklist = [
            "nano",
            "vim",
            "vi",
            "emacs",
        ]
        if any(element in " ".join(command) for element in blacklist):
            raise Exception("Command not allowed.")

        return command