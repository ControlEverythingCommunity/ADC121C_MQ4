[![MQ4](ADC121C_I2CGAS_MQ4.png)](https://www.controleverything.com/content/Gas?sku=ADC121C_I2CGAS_MQ4)
# MQ4
MQ4 Gas Sensor.

The MQ4 is capable of sensing methane or natural gas air concentration levels.

This Device is available from ControlEverything.com [SKU: ADC121C_I2CGAS_MQ4]

https://www.controleverything.com/content/Gas?sku=ADC121C_I2CGAS_MQ4

This Sample code can be used with Raspberry pi, Arduino and Particle.

## Java
Download and install pi4j library on Raspberry pi. Steps to install pi4j are provided at:

http://pi4j.com/install.html

Download (or git pull) the code in pi.

Compile the java program.
```cpp
$> pi4j MQ4.java
```

Run the java program.
```cpp
$> pi4j MQ4
```

## Python
Download and install smbus library on Raspberry pi. Steps to install smbus are provided at:

https://pypi.python.org/pypi/smbus-cffi/0.5.1

Download (or git pull) the code in pi. Run the program.

```cpp
$> python MQ4.py
```

## Arduino
Download and install Arduino Software (IDE) on your machine. Steps to install Arduino are provided at:

https://www.arduino.cc/en/Main/Software

Download (or git pull) the code and double click the file to run the program.

Compile and upload the code on Arduino IDE and see the output on Serial Monitor.

#####The code output is the methane concentration in ppm.