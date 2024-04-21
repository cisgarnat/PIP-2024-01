
import serial as conn

arduino = conn.Serial(port="COM3",baudrate=900,timeout=1)

print("conexion con arduino exitosa")

while True:
    a = arduino.readline()
    a = a.decode()
    a = a.strip()
    print(a)