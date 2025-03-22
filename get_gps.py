# import serial
# import pynmea2
# import time

# # Serial port config
# SERIAL_PORT = '/dev/ttyACM0' 
# BAUD_RATE = 9600

# def read_gps():
#     last_print_time = 0  
#     try:
#         with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1) as ser:
#             # print("Reading GPS data...")

#             while True:
#                 line = ser.readline().decode('ascii', errors='replace').strip()
#                 if line.startswith('$GPGGA') or line.startswith('$GPRMC'):
                    
#                     try:
#                         msg = pynmea2.parse(line)
#                         if hasattr(msg, 'latitude') and hasattr(msg, 'longitude'):
#                             current_time = time.time()
#                             # print("current_time: ", current_time)

#                             if current_time - last_print_time >= 10:
#                                 return msg.latitude, msg.longitude
                                
#                                 # print(f"Latitude: {msg.latitude}, Longitude: {msg.longitude}")
#                                 last_print_time = current_time

#                     except pynmea2.ParseError:
#                         continue
#     except serial.SerialException as e:
#         print(f"Serial error: {e}")

# if __name__ == "__main__":
#     read_gps()


import serial
import pynmea2

SERIAL_PORT = '/dev/ttyACM0'
BAUD_RATE = 9600

def read_gps_once():
    try:
        with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1) as ser:
            while True:
                line = ser.readline().decode('ascii', errors='replace').strip()
                if line.startswith('$GPGGA') or line.startswith('$GPRMC'):
                    try:
                        msg = pynmea2.parse(line)
                        if hasattr(msg, 'latitude') and hasattr(msg, 'longitude'):
                            return msg.latitude, msg.longitude
                    except pynmea2.ParseError:
                        continue
    except serial.SerialException as e:
        print(f"Serial error: {e}")
        return None, None
