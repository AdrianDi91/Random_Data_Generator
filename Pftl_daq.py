import serial
from time import sleep

class Device:
    DEFAULTS = {'write_termination': '\n',
    'read_termination': '\n',
    'encoding': 'Ascii',
    'baudrate': 9600,
    'read_timeout': 1,
    'write_timeout': 1,
    }

    def __init__(self, port):
        self.port = port
        self.rsc = None

    def initialize(self):
            self.rsc = serial.Serial(port=self.port,                     #communication with the device
                baudrate=self.DEFAULTS['baudrate'],
                timeout=self.DEFAULTS['read_timeout'],
                write_timeout= self.DEFAULTS['write_timeout'])
            sleep(1)

    def idn(self):                          # die Methode IDN sagt nur aus welcher COMPORT gelesen wird (für serial number)
        return self.query('*IDN?')
    
    def get_analog_input(self, channel):
        message = f'IN:CH{channel}' #.format(channel)           # form message you want to send to device as string IN=Input
        print("Message ",type(message))
        print("Message: ", message)
        ans = self.query(message)
        print(f"Answer is {type(ans)} and {ans}")
        ans = int(ans)
        return ans         
    
    def set_analog_output(self, channel, output_value):
        message = 'OUT:CH{}:{}'.format(channel, output_value)
        self.query(message)

    def query(self, message):                                   # Query = Rückfrage
        message = message + self.DEFAULTS['write_termination']  #hier kommt 'n rein
        print("11111: ", message)
        message = message.encode(self.DEFAULTS['encoding'])     # hier encoding ascii encodes the string to bytes (like b)
        print("22222: ", message)
        self.rsc.write(message)                                 # writes to device
        ans = self.rsc.readline()
        print("ANS: ", ans)
        ans = ans.decode(self.DEFAULTS['encoding']).strip()     # return line with value
        print("ANS: ", ans)
        return ans

    def finalize(self):
        if self.rsc is not None:
            self.rsc.close()

dev = Device('COM12') #<---- Remember to change the port
dev.initialize()
serial_number = dev.idn()
print(f'The device serial number is: {serial_number}')
"""for i in range(10):
    dev.set_analog_output(0, 4000)
    volts = dev.get_analog_input(0)
    print(f'Measured {volts}')
    sleep(.5)
    dev.set_analog_output(0, 0)
    volts = dev.get_analog_input(0)
    print(f'Measured {volts}')
    sleep(.5)"""
volts = dev.get_analog_input(0)         #Analog input and output must have the same number
print(volts)
dev.set_analog_output(0, 1000)
volts = dev.get_analog_input(0)
print(volts)
dev.finalize()          #Close communication"""

#https://github.com/PFTL/py4lab

# 11111:  *IDN?

# 22222:  b'*IDN?\n'
# ANS:  b''
# ANS:  
# The device serial number is: 
# Message  <class 'str'>       
# Message:  IN:CH0
# 11111:  IN:CH0

# 22222:  b'IN:CH0\n'
# ANS:  b''
# ANS:  
# Answer is <class 'str'> and
# Traceback (most recent call last):
#   File "c:\Users\Addi\Documents\.git\Python for the Lab\Pftl_daq.py", line 69, in <module>
#     volts = dev.get_analog_input(0)         #Analog input and output must have the same number
#   File "c:\Users\Addi\Documents\.git\Python for the Lab\Pftl_daq.py", line 33, in get_analog_input
#     ans = int(ans)
# ValueError: invalid literal for int() with base 10: ''