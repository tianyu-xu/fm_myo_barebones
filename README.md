# Electromyogaphy-based Mouse Pointer Control with Python

## Abstract

As people become more and more integrated with the personal computers, smartphones, cloud services and various embedded systems, new interfacing options are required to provide faster and more comfortable service than a conventional touchscreen, button or a mouse. One of the possible ways to realize human-machine interface is via electromyographic signals, which are generated by muscles during their contractions and can be analyzed to derive the command to the computer. This technology has applications in prosthetics and rehabilitation as well.<p>

The purpose of the project is to implement a Python-based program that allows the user to control the mouse cursor by contracting the muscles of his hand. A software is designed to acquire EMG signals from the MYO EMG armband using Python. A GUI is established to guide the user through the calibration procedure. The user is asked to reach a specific point and the time he needs to reach is measured. His experience is evaluated if there is a learning curve and how fast the skill grows with training.

## Requirements

### Software packages

* OS: Windows 10 <p>

* Languages: Python 3<p>

* Dependancies: numpy, matplotlib, PyAutoGUI, scipy, myopython

### Hardware

* Components: MYO EMG armband

## Installation and setup

### 0. Install Anaconda
If you are not familiar with Python and virtual environments, I suggest using Anaconda. Download a Python 3.7 Anaconda from the [official site](https://www.anaconda.com/products/individual)
and install it. Use default installation options.

### 1. Install MyoConnect

Install MyoConnect from the provided setup file: [Windows](https://www.dropbox.com/s/2dfv0gpqq0c2qrp/Myo_Connect_Installer.exe?dl=0)
, [MacOS](https://www.dropbox.com/s/ua43z9n2rib4hv3/MyoConnect.dmg?dl=0)
.

To connect and use the armband, please follow the official tutorial within MyoConnect.

Later, to set up MyoConnect for a comfortable work, run it, then right-click on its icon in task bar, select **Preferences**, and uncheck all options in all tabs. Then, right-click on icon again, select **Application Manager** and uncheck all options here too.

### 2. Create a new python 3.8 virtual environment (explained for Anaconda)

On Windows, open **anaconda prompt**. On MacOS, run **Terminal**. Run the following commands and accept the changes:
```
conda create --name myo python=3.8 pip
```
Now activate the environment that we have just created (its name is '*myo*'):
```
conda activate myo
```
Note: please remember that any time you want to run this project from a new command/terminal window, you need to activate this environment again.

### 3. Install *myo-python* package

Install it from from our fork on Github. To do so, in command line, with 'myo' environment activated, run:
```
pip install https://github.com/smetanadvorak/myo-python/tarball/master
```
### 4. Setup the fm_myo_barebones package

[Download](https://github.com/smetanadvorak/fm_myo_barebones/tarball/master)
this project and put it in an appropriate directory on your disk. In command window, navigate to this project's folder and run:
```
pip install -e .
```


## Architecture

### Step 1: MAV
Apply the calculation of MAV (mean absolute value) for all eight channels of the EMG using MYO armband. Plotted the calculated value. Find out which channels may be of use to control a pointer in each of the directions.

### Step 2: Make a Prototype cursor control example
1. Find out which channels help you detect these movements of the wrist (see terms and descriptions [here]( http://www.ergovancouver.net/wrist_movements.htm)).
2. Implement a MAV calculator in these channels, using the same IIR filter approach.
3. Find a python package that lets you control the mouse cursor (probably you will end up using [pyautogui]( https://pypi.org/project/PyAutoGUI/)).
4. Map the MAV in each of the four channels to the speed of cursor in the corresponding direction.
5. Make a video of how it works. Can you freely navigate with this design? Is it stable? How would you implement a mouse click?


##  Examples
### 0. How to Run the Code

#### 1. Set up MyoConnect
This should be done only once at the beginning of your working session:

* Insert MYO's Bluetooth dongle in your USB port.
* Run MyoConnect, right-click on its icon in task bar, select **Armband Manager** ....
* Approach the dongle with your armband. It should automatically get paired with MyoConnect.
* In MyoConnect, press 'Ping' to make sure that it is not connected to some other armband nearby. Your armband should vibrate in response to the ping.

#### 2. Setup the environment and run the code

Open **Anaconda Prompt** (Windows) or **Terminal** (MacOS) and activate the 'myo' environment:
```
conda activate myo
```
Navigate to the folder with this package, then to ./examples/streaming and run a test script:
```
python streaming.py
```
If everything is installed correctly, a matplotlib figure should appear with the EMG signals being traced in real time. This and other examples can be stopped by either pressing **ctrl-c** (MacOS) or **shift-c** (Windows).