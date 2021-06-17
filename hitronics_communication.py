# imports
from serial import Serial

# global variables
BAUDRATE = 115200
DATA_BITS = 8
PARITY = None
STOP_BITS = 1
FLOW_CONTROL = None
BUFFER = 1024


# TODO: com port lookup
COMPORT = 'COM6'





# Checksum = hex length + message

# convert to dec
# convert add
# convert back to hex?

#%%
number, pad, rjust, size, kind = 0xABC123EFFF, '0', '>', 42, 'b'
print(f'{number:{pad}{rjust}{size}{kind}}')
# '001010101111000001001000111110111111111111'
# %%
number = 0xAA5500048084
pad = '0'
rjust = '>'
size = 8*6
kind = 'b'

MESSAGE = f'{number:{pad}{rjust}{size}{kind}}'

#%%
# open serial port
ser = Serial(COMPORT)
print(ser.name)

# send command
ser.write(MESSAGE)

# listen for response
print(ser.read(BUFFER))