# openIPC configurator (python edition)
first try on a configurator for openIPC for any platform

openIPC configurator by default runs on Windows and needs .NET framework. The Windows Version uses a batch file and is english only.

As this is my very first attempt of writing a GUI in python, it is also the first time creating something based on a existing programm.
I hope there are a few people out there, who can help make this configurator work with LiNUX (which i am using), windows (like the existing) and of course MacOS and maybe on mobile devices, which would be awesome for everyone. Who likes to take a laptop to the field, which isn't enough for openIPC.

This software needs a hotspot function as well for mobile devices or something you can use to connect to the openIPC system...

# openIPC configurator written in python3 by KM|fpv

I've used thonny for writing this entire thing, because it's fast and easy and also available for all platforms.

TODO or wanted list:
01) multilanguage - is working
02) device selection - kind of works
03) ping device - is working => enables connect button on successful ping answer
04) connect to pinged device, when ping was successful
05) get/download the configuration files (list needs update: majestic.yaml/vdec/wfb/wifibroadcast/(set)video.sh/and more)
06) upload configuration files to the devices
07) automatic change corresponding configuation based on settings (change cam - automatic change vrx and vice versa)
09) update/backup for sensors/vtx/vrx
10) OSD config - if it's still needed (read about betaflight is implementing this - nice!)
11) presets for sensors (like imx415 and imx335 and image settings)
12) manual/hints system
13) ...
