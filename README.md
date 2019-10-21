# security-cam-raspberry-pi-
making a sucurity cam by using a raspberry pi and a usb camera
## Supply list

1. Raspberry Pi


<img src="https://www.mouser.com/images/riotboard/lrg/6010602_SPL.jpg" width="200">


2. USB Webcam


<img src="https://snpi.dell.com/snp/images/products/large/21_A5485971.jpg" width="200">

3. A router(which you probably already have one).

## Software Requirement
1. [Numpy](https://pypi.org/project/numpy/)
<img src="https://extraimage.net/images/2019/09/23/5ac6e9d90002903efacacdcb8182b8ed.png" width="100">

2. [Opencv](https://pypi.org/project/opencv-python/)
<img src="https://opencv.org/wp-content/uploads/2019/02/opencv-logo-1.png" width="100">

And other dependencies of these two packages
You will need to install these packages on both your raspberry pi and the client(any device that can connect to the LAN)
## Setup the project on raspberry pi
1. Setup your raspberry pi

if you have already setup your raspberry pi, please skip this step

[Follow instructions on this webpage to setup](https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up)

2. open terminal, run `hostname -I` to check the raspberry pi's ip and record it(we will use it later)

3. install python3 on raspberry pi

if you have already installed python\]opl., please skip this step

open terminal and run `sudo apt-get install python3`

4. connect your USB webcam to your raspberry pi

<img src="https://www.teachmemicro.com/wp-content/uploads/2018/02/raspberry-pi-webcam.jpg" width="375">

5. copy the python file in `on_raspberrypi` folder to raspberry pi(in the `home` directory)

6. open terminal and run command `sudo python3 server.py`

you can change the default port by adding `--port (your port)`

now the program is pending for the client to receive the data

## Setup the project on client device
1. install python3 on your client device

[Please follow the instructions on this website](https://realpython.com/installing-python/)

2.download the python file in `on_client` to where your default terminal/DOS path is.

3. open DOS/terminal/console and run cammand `sudo python3 client.py --ip (the ip recorded) --port (the port used)`

4. if successful, it should appear like this

## further more

1. if we wan't raspberry pi to be a security camera, we shouldn't need to run command when booting it. we can 
