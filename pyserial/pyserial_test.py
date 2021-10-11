import serial

tx = serial.Serial('COM1')
rx = serial.Serial('COM2')
tx.write(open("test.txt", 'rb').read())
print(rx.readline())
tx.close()
rx.close()