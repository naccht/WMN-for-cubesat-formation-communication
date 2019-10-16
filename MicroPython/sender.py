import xbee

TARGET_64BIT_ADDR = b'' # Put target Xbee module adress here
MESSAGE = "Hello World"

print("Sending data to %s >> %s" % (''.join('{:02x}'.format(x).upper() for x in TARGET_64BIT_ADDR),
                                    MESSAGE))

try:
    xbee.transmit(TARGET_64BIT_ADDR, MESSAGE)
    print("Data sent successfully")
except Exception as e:
    print("Transmit failure: %s" % str(e))