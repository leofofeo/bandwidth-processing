class NetworkBandwidthUtil:
    def __init__(self, timestamp, server, interface_name, net_bit_rate):
        self.timestamp = timestamp
        self.server = server
        self.interface_name = interface_name
        self.net_bit_rate = net_bit_rate

    @property
    def network_interface_name(self):
        return self.server + "-" + self.interface_name