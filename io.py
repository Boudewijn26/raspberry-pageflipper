import RPi.GPIO as GPIO
import time

NULL_CHAR = chr(0)


def write_report(report):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report.encode())


def page_down(channel):
    write_report(NULL_CHAR * 2 + chr(0x4e) + NULL_CHAR * 5)
    write_report(NULL_CHAR * 8)


def page_up(channel):
    write_report(NULL_CHAR * 2 + chr(0x4b) + NULL_CHAR * 5)
    write_report(NULL_CHAR * 8)


GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.OUT)

GPIO.output(24, GPIO.HIGH)
GPIO.add_event_detect(18, GPIO.BOTH, callback=page_down, bouncetime=50)
GPIO.add_event_detect(23, GPIO.BOTH, callback=page_up, bouncetime=50)

while True:
    time.sleep(1)
