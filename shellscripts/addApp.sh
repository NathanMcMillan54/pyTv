#!/usr/bin/env bash

if [[ "$OSTYPE" == "linux-gnu"* ]]; then
	gnome-terminal
	python testAddApp.py
fi
