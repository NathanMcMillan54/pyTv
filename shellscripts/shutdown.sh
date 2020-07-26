#!/usr/bin/env bash

if [[ "$OSTYPE" == "linux-gnu"* ]]; then
	shutdown -P now
elif [[ "$OSTYPE" == "darwin"* ]]; then
	osascript -e 'tell application "System Events" to shut down'
fi
