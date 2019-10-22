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
	return xbee.atcmd("AI")  # If the value of AI is non zero, the module is not connected to a network
print("Forming a new 802.15.4 network as a coordinator...")
xbee.atcmd("NI", "Coordinator")
network_settings = {"CE": 1, "A2": 4, "CH": 0x13, "MY": 0xFFFF, "ID": 0x3332, "EE": 0}
for command, value in network_settings.items():
	xbee.atcmd(command, value)
xbee.atcmd("AC")  # Apply changes
time.sleep(1)
while network_status() != 0:
	time.sleep(0.1)
print("Network Established\n")

print("Waiting for a remote node to join...")
node_list = []
while len(node_list) == 0: # Perform a network discovery until the remote joins
	node_list = list(xbee.discover())
print("Remote node found, transmitting data")

for node in node_list:
	dest_addr = node['sender_eui64'] # using 64-bit addressing
	dest_node_id = node['node_id']
	payload_data = "Hello, " + dest_node_id

	xbee.transmit(dest_addr, payload_data)

# Start the receive loop
print("Receiving data...")
print("Hit CTRL+C to cancel")
while True:
	p = xbee.receive()
	if p:
		# Here you recieve the message
        format_packet(p)
	else:
		time.sleep(0.25)









