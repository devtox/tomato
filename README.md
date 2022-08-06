# Tomato timer
 
This is a tomato timer for Linux. Run to start countdown timer.

Required:
* Python3
* Gtk3

```bash
Use "python3 tomato.py seconds
For example: python3 tomato.py 120
```

### Click to play

[![Tomato timer Linux](https://img.youtube.com/vi/fNsG9uubY0E/0.jpg)](https://www.youtube.com/watch?v=fNsG9uubY0E "Linux TOMATO timer")

### Why?

Parkinson's law: "work expands so as to fill the time available for its completion."

To increase productivity, avoid the "attention economy", "social media" and other malicious industries that waste your time.

By default the timer hides after time completes. You can change behavior by changing code.

### Unity

If you use [Ubuntu Unity](https://ubuntuunity.org/) and want a desktop shortcut (change path to script and 10 to whatever seconds)

```
#!/usr/bin/env xdg-open
[Desktop Entry]
Version=1.0
Name=Tomato
Comment=Tomato
Exec=python3 /home/frank/tomato.py 10
Path=/home/frank/
Icon=/usr/share/icons/Humanity/actions/32/media-record.svg
Terminal=false
Type=Application
Categories=Utility;Development;
```
