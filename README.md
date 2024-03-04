# Pawsible
Anything is possible (on your computer) with Pawsible!

## How to run
Works with Python -v 11
Run both main.py and virtualmouse.py

## Inspiration
We were inspired by desktop pets that walked around on your desktop and kept you company while doing work! We also wanted to use this as an opportunity to add accessibility into using the computer. 

## What it does
Pawsible is a desktop pet that also allows you to surf the web with just your hands! You can perform a google search, and control your mouse with just gestures.

## How we built it
We built it in Python, using packages such as Tkinter, MediaPipe, CVZone, and PyAutoGUI. 

## Challenges we ran into
We initially had big aspirations and wanted to translate ASL to text so people could perform a google search. However, we quickly realized that all the online machine learning modules for ASL recognition were not accurate, and also incredibly slow. It would have taken way too much time to train our own model, so we scrapped that idea. We also struggled initially with connecting Widget to the camera. We could not figure out how to add the interaction between the camera and the computer. Because this computer vision is done in real-time, it was a challenge to optimize it so that the human-computer interaction could be as responsive as it could be.

## Accomplishments that we're proud of
We're proud that we managed to get it to work! We also love how we managed to incorporate both the fun, desktop pet, and the accessibility of letting someone use their computer without their keyboard.

## What we learned
We learned a lot about computer vision and gesture recognition! We also learned how to use Tkinter to create animations and an interactive character.

## What's next for Pawsible
We'd love to implement more features to the virtual mouse! Right now it can only automatically do a google search, but it would be great to add more accessibility features such as the ASL translation that we wanted to implement before!
