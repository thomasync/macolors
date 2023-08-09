import re

from rich.console import Console
from rich.style import Style
from rich.text import Text
from rich.theme import Theme


class Format:
    def __init__(self, scheme):
        self.scheme = scheme
        self.styles = []

    def format(self, line, line_number):
        theme = Theme(inherit=False)
        console = Console(theme=theme)
        text = self.get_text(line, line_number)

        console.print(text)

    def format_default(self, line):
        console = Console()
        console.print(line)

    def get_text(self, line, line_number):
        text = Text(line)

        if not self.__verify_scheme_contraints(self.scheme, line_number):
            return text

        if "style" in self.scheme:
            text.style = Style.parse(self.scheme["style"])

        if "schemes" in self.scheme:
            for scheme in self.scheme["schemes"]:
                if not "style" in scheme:
                    continue

                if not self.__verify_scheme_contraints(scheme, line_number, True):
                    continue

                if re.search(scheme["match"], line, flags=re.MULTILINE):
                    self.stylize(scheme, text)

        return text

    def stylize(self, scheme, text):
        matchs = re.search(scheme["match"], text.plain)
        if matchs:
            index = len(matchs.groups())
            index_start = matchs.start(index)
            index_end = matchs.end(index)
            text.stylize(scheme["style"], index_start, index_end)
            self.styles.append([scheme["style"], index_start, index_end])

    def __verify_scheme_contraints(self, scheme, line_number, specific=False):
        verification = True
        if "min" in scheme and scheme["min"] > line_number:
            verification = False

        if "max" in scheme and scheme["max"] < line_number:
            verification = False

        if "line" in scheme and scheme["line"] != line_number:
            verification = False

        if specific:
            if "odd" in scheme and scheme["odd"] and line_number % 2 == 0:
                verification = False

            if "odd" in scheme and not scheme["odd"] and line_number % 2 != 0:
                verification = False

        return verification
