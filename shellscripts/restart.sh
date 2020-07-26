#!/usr/bin/env bash

if [[ "$OSTYPE" == "linux-gnu"* ]]; then
	restart
elif [[ "$OSTYPE" == "darwin"* ]]; then
	osascript -e 'tell application "System Events" to restart'
fi
