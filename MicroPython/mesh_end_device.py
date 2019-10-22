import xbee, time

def format_eui64(addr):
	return ':'.join('%02x' % b for b in addr)

def format_packet(p):
	type = 'Broadcast' if p['broadcast'] else 'Unicast'
	print("%s message from EUI-64 %s (network 0x%04X)" % 
		(type, format_eui64(p['sender_eui64']), p['sender_nwk']))
	print("from EP 0x%02X to EP 0x%02X, Cluster 0x%04X, Profile 0x%04X:" %
		(p['source_ep'], p['dest_ep'], p['cluster'], p['profile']))
	print(p['payload'],"\n")

def network_status():
	return xbee.atcmd("AI") # If the value of AI is non zero, the module is not connected to a network
print("Joining network as an end device...")
xbee.atcmd("NI", "End Device")
network_settings = {"CE": 0, "A1": 4, "CH": 0x13, "ID": 0x3332, "EE": 0}
for command, value in network_settings.items():
	xbee.atcmd(command, value)
xbee.atcmd("AC")  # Apply changes
time.sleep(1)

while network_status() != 0:
	time.sleep(0.1)
print("Connected to Network\n")

# Start the transmit/receive loop
while True:
	p = xbee.receive()
	if p:
		format_packet(p)
	else:
		# Here you send the message
        try:
			xbee.transmit(xbee.ADDR_COORDINATOR, message)
		except Exception as err:
			print(err)
		time.sleep(0.25)






