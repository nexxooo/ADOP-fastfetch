#!/bin/bash

while ! ping -c 1 -W 1 8.8.8.8 &>/dev/null; do
    echo "En attente d'internet..."
    sleep 2
done

python3 ~/.config/sway/main.py

