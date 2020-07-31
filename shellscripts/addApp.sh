#!/usr/bin/env bash

if [[ "$OSTYPE" == "linux-gnu"* ]]; then
	gnome-terminal --tab --title="Add app" --command="python ../testAddApp.py"
fi
