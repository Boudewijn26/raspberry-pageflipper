# Raspberry Pi powered page flipper

Requires a Raspberry Pi zero or zero w, setup from [pi-as-keyboard](https://github.com/c4software/pi-as-keyboard)

Connect page down to pin 18 and ground, page up to pin 23 and ground and LED to pin 
24 and ground.

I recommend optimizing your Pi for boot time and then running this from `/etc/rc.local`. LED will turn on as soon as switches should work.
