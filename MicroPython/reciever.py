import xbee

print("Waiting for data...\n")

while True:
    received_msg = xbee.receive()
    if received_msg:
        sender = received_msg['sender_eui64'] #Xbee sender address
        payload = received_msg['payload']
        print("Data received from %s >> %s" % (''.join('{:02x}'.format(x).upper() for x in sender),
                                               payload.decode()))