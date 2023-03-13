#! /bin/bash

TARGET=/Users/$USER/loaner_reminder/

if [ -d "$TARGET" ]; then
    echo "Looks like you're already set up!"
    echo "Make sure all the files are still in /Users/$USER/loaner_reminder/ if it doesn't work"
else
    echo 'Setting up...'
    chmod u+x $HOME/Downloads/loaner_reminder/*
    mkdir /Users/$USER/loaner_reminder/
    cp $HOME/Downloads/loaner_reminder/* /Users/$USER/loaner_reminder/
    echo 'Setup complete!'
fi

echo 'Starting the program...'
python3 /Users/$USER/loaner_reminder/setup.py $1
echo 'Setup complete!'
