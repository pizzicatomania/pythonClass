import serial
ser = serial.Serial(
    port='COM1',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
        timeout=0 )

print(ser.portstr) #

ser.write( bytes('hello', encoding='ascii') ) #
ser.write(b'hello') #


x = ser.read() # read one byte
s = ser.read(10) # read up to ten bytes (timeout)
line = ser.readline() # read a '\n' terminated line

ser.close()


