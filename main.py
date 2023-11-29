import serial
import time
import datetime
import csv

total_number_of_runs = 14
idle_times = [600, 300, 120, 60, 60, 30, 30, 10, 10, 10, 10, 10, 10, 10]

dev = serial.Serial(baudrate=19200,
                    parity=serial.PARITY_EVEN, 
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS,
                    timeout=1.0)
dev.port = '/dev/tty.usbserial-A10LJ0ED'

def write_temperatures(run, rows):
    with open(str(run) + '.csv', 'w', newline='') as csvfile:
        fieldnames = ['temperature']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        for i in range(len(rows)):
            writer.writerow(rows[i])

start_time = datetime.datetime.now().timestamp()
def get_temp(dev):
    dev.flushInput()
    dev.flushOutput()
    command = bytes('#0A0000NA2\r\n', 'ascii')
    dev.write(command)
    
    t = datetime.datetime.now().timestamp() - start_time
    
    data = dev.read(16)
    if len(data) == 16 and int(data[0])==62 and int(data[1])==15:
        s1 = (int(data[5])*256.0 + int(data[6]))/10
    else:
        s1 = None
    return {'temperature': s1}

def read_for_thirty_seconds(run):
    start_time = datetime.datetime.now().timestamp()
    rows = []
    for i in range(30):
        temp = get_temp(dev)
        print(temp)
        rows.append(temp)
        time.sleep(0.5)
    print(rows)
    write_temperatures(run, rows)

def wait_for_seconds(seconds):
    minutes = int(seconds/60)
    if minutes < 1:
        print(seconds, " seconds to go")
        time.sleep(seconds - 10)
    else:
        for i in range(minutes):
            print(minutes - i," minutes to go")
            if i == minutes-1:
                time.sleep(50)
            else:
                time.sleep(60)

def main():
    dev.open()
    for i in range(total_number_of_runs):
        print("Starting with cycle ", i)
        print("Waiting for seconds", idle_times[i])
        wait_for_seconds(idle_times[i])
        count_for_10_seconds()
        print("Get ready for temperature reading")
        input("Press key to start reading temperature")
        print("Now reading temperature")
        read_for_thirty_seconds(i)
    dev.close()

def count_for_10_seconds():
    for i in range(10):
        print(int(10-i), " seconds left")
        time.sleep(1)

main()