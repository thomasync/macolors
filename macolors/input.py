import json
import os
import re
from pathlib import Path

import yaml

from macolors.format import Format

HOME = str(Path.home())


class Input:
    def __init__(self, line=None, line_number=0, scheme=None):
        self.line = line
        self.line_number = line_number
        self.scheme = scheme
        self.force_auto = False

    def format(self, line):
        self.define_input(line)

        _format = Format(self.scheme)
        if self.scheme:
            return _format.format(self.line, self.line_number)
        else:
            return _format.format_default(self.line)

    def define_input(self, line):
        self.line = line.rstrip()
        self.line_number += 1

        if not self.scheme and not self.force_auto:
            self.scheme = self.get_scheme()

    def get_scheme(self, name=None):
        _scheme = None
        for scheme in self.get_schemes():
            if name and scheme["name"] == name:
                _scheme = scheme

            elif (
                not name and "match" in scheme and re.search(scheme["match"], self.line)
            ):
                return scheme

        return _scheme

    def set_scheme(self, name):
        self.scheme = self.get_scheme(name)

    def set_json_scheme(self, json_scheme):
        try:
            scheme = json.loads(json_scheme)

            if "schemes" not in scheme:
                key = list(scheme.keys())[0]
                scheme = scheme[key]

            scheme["name"] = "custom_json"
            self.scheme = scheme
        except Exception as e:
            raise Exception("Bad json format", e)

    def get_schemes(self):
        schemes = self.__get_default_scheme()

        custom_schemes = self.__get_custom_scheme()
        if custom_schemes:
            self.__add_scheme(schemes, custom_schemes, True)

        return schemes

    def __add_scheme(self, schemes, yaml_file, custom=False):
        try:
            schemes_keys = list(yaml_file.keys())
            for scheme_key in schemes_keys:
                self.__is_already_scheme(schemes, scheme_key, custom)

                scheme = yaml_file[scheme_key]
                scheme["name"] = scheme_key
                schemes.append(scheme)
        except Exception as e:
            raise Exception("Yaml file are not in correct format", e)

    def __is_already_scheme(self, schemes, scheme_key, custom):
        schemes_names = [scheme["name"] for scheme in schemes]

        if scheme_key in schemes_names and not custom:
            raise Exception(f"Scheme {scheme_key} already exists")
        elif scheme_key in schemes_names and custom:
            schemes.remove(
                next(
                    (scheme for scheme in schemes if scheme["name"] == scheme_key),
                    None,
                )
            )

    def __get_default_scheme(self):
        schemes = []
        for file in os.listdir(f"{os.path.dirname(__file__)}/schemes"):
            yaml_file = self.__open_yaml_file(
                f"{os.path.dirname(__file__)}/schemes/{file}"
            )
            if yaml_file:
                self.__add_scheme(schemes, yaml_file)

        return schemes

    def __get_custom_scheme(self):
        schemes = None
        if os.path.isfile(f"{HOME}/.macolors.yml"):
            schemes = self.__open_yaml_file(f"{HOME}/.macolors.yml")

        elif os.path.isfile(f"{HOME}/.macolors.yaml"):
            schemes = self.__open_yaml_file(f"{HOME}/.macolors.yaml")

        return schemes

    def __open_yaml_file(self, file):
        if file.endswith(".yml") or file.endswith(".yaml"):
            with open(file, "r") as stream:
                try:
                    yaml_file = yaml.safe_load(stream)
                    if yaml_file:
                        return yaml_file
                except yaml.YAMLError as exc:
                    print(exc)
                    exit(1)

        return None
