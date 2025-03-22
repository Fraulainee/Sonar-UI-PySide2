import serial
import pynmea2

# Change this to the correct serial port (e.g., 'COM3' on Windows or '/dev/ttyUSB0' on Linux)
SERIAL_PORT = '/dev/ttyACM0'
BAUD_RATE = 9600  # Gmouse typically uses 9600 baud

def read_gps():
    try:
        with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1) as ser:
            # print("Reading GPS data...")
            while True:
                line = ser.readline().decode('ascii', errors='replace').strip()
                if line.startswith('$GPGGA') or line.startswith('$GPRMC'):
                    try:
                        msg = pynmea2.parse(line)
                        if hasattr(msg, 'latitude') and hasattr(msg, 'longitude'):
                            # print(f"Latitude: {msg.latitude}, Longitude: {msg.longitude}")
                            return msg.latitude, msg.longitude
                    except pynmea2.ParseError:
                        continue
    except serial.SerialException as e:
        print(f"Serial error: {e}")

if __name__ == "__main__":
    read_gps()
