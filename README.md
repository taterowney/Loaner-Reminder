Are you a member of an IT department who constantly has to loan out devices to people who don't have/spilled spaghetti on their laptops? Are you annoyed when said individuals "forget" to return these devices on time? If you answered "yes" to any of these questions, this handy script is for you! After a specified number of days, the program will display a message every 20 minutes reminding the user to return the device. **It does not modify or send any of the borrower's data, nor does it exert any control over the borrower's computer besides displaying these notifications.**

This is currently built for MacOS exclusively; it's not gonna work on any other operating systems.

# How to Use

## Setup

To set up this tool, download the .zip file <a href="https://taterowney.github.io/Loaner-Reminder/loaner_reminder.zip" download>here</a> and unzip it, making sure that the expanded folder is in your Downloads folder.

Next, open the "Terminal" application (either with ⌘ + Space or in the Applications > Utilities folder). You should see a prompt which looks like:

`USERNAME @ SERIAL NUMBER ~ % `

where `SERIAL NUMBER` is the serial number of the device (wow) and USERNAME is the username of the account **which will be used by the borrower** (if this is not what you see or you are signed into a different account, see the "Debugging" section below). 

  Type or paste the following command into the prompt and press "Return":

`chmod u+x ~/Downloads/loaner_reminder/setup.sh ; /bin/bash ~/Downloads/loaner_reminder/setup.sh DAYS`

where `DAYS` is the number of days you want to pass until the notifications are displayed. If this is unset, it will default to 20 days before the notifications appear.
You might receive a prompt saying that "'Terminal' would like to administer your computer." Permitting this allows the program to setup [cron programs](https://en.wikipedia.org/wiki/Cron), programs which run after a set amount of time. You may have to sign in as an administrator to allow this. 

EXAMPLE:
`chmod u+x ~/Downloads/loaner_reminder/setup.sh ; /bin/bash ~/Downloads/loaner_reminder/setup.sh 7`

Start reminding the borrower after a week.

Once this is done, you are all good to go! You can also erase the copy of the `loaner_reminder` folder in Downloads if you want.

## Cleanup

To reset the program so that messages are delayed for X days (replacing the old delay), simply run
`/bin/bash ~/loaner_reminder/setup.sh DAYS`

again in the Terminal.

To stop the program altogether, run
`python3 $HOME/loaner_reminder/disable.py`

in the Terminal. You can always start it again in the same way you would reset it (see above).

  If you've disabled the script, it doesn't do anything anymore, but if you really want you can remove the code by erasing `Users > *USERNAME* > loaner_reminder` folder. 


# Debugging

Q: When I open the Terminal, I see a username in the prompt which **isn't** the one that the borrower will be logged in as ("Shared", "tech_department", etc.) What should I do?

A: If you aren't/don't want to be signed in under the borrower's future account, it's totally fine. To get around this, run Terminal commands with the following text **in front** of them:
`sudo -u BORROWER_NAME `

where `BORROWER_NAME` is the username of the future borrower (usernames can be viewed by looking at the contents of the "Users" directory). You may have to input the password to the future borrower's account.
Note that this (obviously) requires the borrower's account to be already set up; this isn't gonna work if they create their own account, etc.

Q: Is this code safe?

A: Yes, this code is completely safe. It does not modify, read, or log any of the user's data besides the date and time. The only thing it does is display (intentionally irksome) messages to the borrower. If you have security concerns, please talk to me (or, you know, just look at the code for yourself; there's not that much of it). 

Q: How do I change the message displayed in the notification?

A: If you want to change the reminder (or if you don't work for my school), navigate to the `Users > BORROWER_NAME > loaner_reminder` directory, open the `toast.py` file with TextEdit (or do it from the Terminal if that's how you roll), and change the value in quotes of the variable called `passive_aggressive_message`. Make sure that the text is encased in a single pair of quotes, and that it's all on one line (or use triple quotes).

Q: Was 99% of this made during Mandarin class?

A: Maybe

Q: Can I use this code?

A: This code is available under an MIT license; feel free to use it however you want as long it complies with that license (viewable in the LICENSE.md file). As with all programs made during a single Mandarin class (maybe), it is built with a certain amount of jank, so my apologies if it breaks.


-- taterowney
