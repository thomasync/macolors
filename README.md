# Macolors - Colorize Command Outputs

![Python Version](https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8%20%7C%203.9-blue)
![License](https://img.shields.io/badge/license-MIT-blue)

Macolors is a Python utility that enhances the output of command-line programs by adding color to their outputs. It utilizes the "rich" library to provide advanced text formatting and colorization, resulting in a more visually appealing and user-friendly experience.

⚠️ **Note**: Macolors is in 0.0.x version, so breaking changes may occur between releases. And it may never be maintained in the future. I created this tool, just to help me on a very specific case of another project.

## TODO's

-   [x] Add support for custom color schemes
-   [x] Add support for custom color schemes in json format
-   [ ] Find a way to colorize the output of commands that are not piped to Macolors (`less`, `more`, `netstat`, etc.)
-   [ ] Add more (mooore) color schemes
-   [ ] Add tests
-   [ ] Publish on PyPI and Homebrew (when the version 1.0.0 will be released)

## Features

-   Colorizes the standard output of command-line programs.
-   Utilizes the "rich" library for advanced formatting and theming.
-   Supports various formatting options, including colors, bold, underline, etc.
-   Easily configurable to match your preferred color scheme.
-   Designed to work seamlessly in pipelines.
-   Compatible with Python 3.6 and above.

## Installation

**Note**: Macolors is still in development, so it is not yet available on PyPI or Homebrew. You can install it manually by cloning the repository and running the setup script.

~~`$ pip install macolors`~~

~~`$ brew install macolors`~~

<br>

```
$ git clone https://github.com/thomasync/macolors
```

```
$ pip install -r requirements.txt
```

```
$ python setup.py install
```

<!-- `pip install macolors` -->

## Usage

To colorize the output of a command, simply pipe the command's output to `macolors`:

```bash
usage: macolors [-h] [-s | -a | --json JSON] [command ...]
or
usage: [command ...] | macolors [-h] [-s | -a | --json JSON]

positional arguments:
  command           command to colorize

options:
  -h, --help        show this help message and exit
  -s , --scheme     Force schema to use. Allowed values are logs, logs2, logs3, extra, crontab
  -a, --force-auto  Force auto detection without using schemes
  --json JSON       Allow to use json format to define scheme
```

```bash
$ ping google.fr | macolors -s extra
```

```bash
$ macolors -s logs tail -f /opt/project/logs/app.log
```

## Customization

Macolors comes with a set of predefined color schemes. You can use the `--scheme` option to select a scheme. If you don't specify a scheme, Macolors will try to automatically detect the colors to use based on the command's output.

### YAML

Create a `.macolors.yml` file in your home directory to add your own color schemes. The file should contain a list of color schemes in YAML format. Each scheme should have a name and a list of color rules. Each rule should have a regular expression to match, a style to apply, and different options to customize the rule.

Style are based on the [rich](https://rich.readthedocs.io/en/latest/index.html) library: [colors](https://rich.readthedocs.io/en/stable/appendix/colors.html#color-names) and [styles](https://rich.readthedocs.io/en/latest/reference/style.html?highlight=italic#rich.style.Style).

```yaml
name_of_scheme:
    match: REGEX [OPTIONAL]
    style: STYLE [OPTIONAL]
    min: INTEGER [OPTIONAL]
    max: INTEGER [OPTIONAL]
    line: INTEGER [OPTIONAL]
    schemes:
        - {
              match: REGEX,
              style: STYLE,
              odd: 'BOOLEAN [OPTIONAL]',
              min: 'INTEGER [OPTIONAL]',
              max: 'INTEGER [OPTIONAL]',
              description: 'STRING [OPTIONAL]',
          }

        - {
              match: REGEX,
              style: STYLE,
              odd: 'BOOLEAN [OPTIONAL]',
              min: 'INTEGER [OPTIONAL]',
              max: 'INTEGER [OPTIONAL]',
              description: 'STRING [OPTIONAL]',
          }
```

Examples of color schemes can be found in the [schemes](macolors/schemes) directory.

### JSON

You can also create your own color scheme by specifying a json object with the `--json` option.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.

---

**Note**: Macolors is designed to work with various command-line utilities. However, some commands may not play well with colorization or may require additional configuration.

Feel free to contribute, report issues, or suggest improvements by opening an [issue](https://github.com/thomasync/macolors/issues) or creating a [pull request](https://github.com/thomasync/macolors/pulls).
