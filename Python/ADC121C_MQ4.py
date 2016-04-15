# Distributed with a free-will license.
# Use it any way you want, profit or free, provided it fits in the licenses of its associated works.
# ADC121C_MQ4
# This code is designed to work with the ADC121C_I2CGAS_MQ4 I2C Mini Module available from ControlEverything.com.
# https://www.controleverything.com/content/Gas?sku=ADC121C_I2CGAS_MQ4#tabs-0-product_tabset-2

import smbus
import time

# Get I2C bus
bus = smbus.SMBus(1)

# ADC121C_MQ4 address, 0x50(80)
# Read data back from 0x00(00), 2 bytes
# raw_adc MSB, raw_adc LSB
data = bus.read_i2c_block_data(0x50, 0x00, 2)

# Convert the data to 12-bits
raw_adc = (data[0] & 0x0F) * 256 + data[1]
ppm = (10000.0 / 4095.0) * raw_adc + 200

# Output data to screen
print "Methane concentration : %.2f ppm" %ppm
