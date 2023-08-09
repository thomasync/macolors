#!/bin/bash

commands=(
	"ping google.fr -c 2 -i 0.1"
	"cat tests/logs/test.log"
	"crontab -l",
)

# Clear
printf '\e]1337;ClearScrollback\a'
clear
sleep 0.05

# Get command
if [ "$1" != "" ]; then
	command_selected=$(echo "$1" | grep -o '[0-9]\+')
fi

# If error or no command selected
if [ "${commands[$command_selected]}" = "" ] || [ "$command_selected" = "" ]; then
	for ((i=0; i<${#commands[@]}; i++)); do
		echo "[$i]: ${commands[$i]}"
	done
	exit 1
fi

# Run command
if [[ "$1" == "run_command_"* ]]; then
	eval "${commands[$command_selected]} | macolors"
else
	nodemon --watch . --watch .home --ext "*.py, *.sh, *.yml" --exec "sh watch.sh run_command_$command_selected" --quiet
fi