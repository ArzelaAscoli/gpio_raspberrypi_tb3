# gpio_raspberrypi_tb3_ws
a working space for controlling gpio in tb3
<br>
<br>
step1: [install rpi gpio](https://www.raspberrypi-spy.co.uk/2012/05/install-rpi-gpio-python-library/)

    sudo apt-get update
    sudo apt-get install rpi.gpio
<br>
step2: remove /devel and /build folder
<br>
step3: catkin_make your working space

    catkin_make
<br>
step4: don't forget source your .bash or .zsh

    source gpio_raspberrypi_tb3_ws/devel/setup.bash
    source gpio_raspberrypi_tb3_ws/devel/setup.zsh
<br>
