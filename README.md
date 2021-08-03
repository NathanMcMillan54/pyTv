# About
This is a python GUI made with Tkinter, it's just for showing a list of streaming services like a smart TV would do.

You can add your own apps to pyTv, Netflix and YouTube are already on pyTv.

You can now play Snake on pyTv v1.1, you can use it to make your own game or just play it all the time instead of actually 
watching TV.

You can find the code for Snake here:
```shell script
apps/snake.py
```

#
# Setup 

Make a virtual environment
```shell script
python3 -m venv env
source env/bin/activate
```

Install requirements
```shell script
pip install -r requirements.txt
```

Start the app
```shell script
python main.py
```

If you want to run pyTv on startup

Recommend that you use a RaspberryPi running some version of Linux 
```shell script
cd /etc/profile.d/
sudo touch strtPyTv.sh
sudo nano strtPyTv.sh
```

In ``strtPyTv.sh`` write:
```shell script
#!/usr/bin/env bash
cd home/$USER/Desktop/pyTv/
sh runPytv.sh
```
