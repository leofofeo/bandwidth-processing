import csv
from models import NetworkBandwidthUtil

def create_network_interfaces(input_path: str) -> dict:
    network_interfaces = {}
    with open(input_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")

        for idx, row in enumerate(csv_reader):
            if idx == 0:
                continue
            server = row[0].lower().strip()
            interface_name = row[1].lower().strip()
            net_bit_rate = float(row[2])
            network_interface = server + "-" + interface_name

            network_interfaces[network_interface] = net_bit_rate
    return network_interfaces

def calculate_network_bandwidth_utilization(input_path:str , network_interfaces: dict) -> list:
    network_bandwidth_utilization = []
    with open(input_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for idx, row in enumerate(csv_reader):
            if idx == 0:
                continue
            timestamp = row[0]
            server = row[1].lower().strip()
            interface_name = row[2].lower().strip()
            net_bit_rate = float(row[3])

            nbu = NetworkBandwidthUtil(timestamp, server, interface_name, net_bit_rate)
            if nbu.network_interface_name in network_interfaces:
                nbr = network_interfaces[nbu.network_interface_name]
                nbu.net_bit_rate = nbu.net_bit_rate / nbr
            network_bandwidth_utilization.append(nbu)

    return network_bandwidth_utilization

def write_output(output_path:str, nbu_list: list):
    with open(output_path, mode='w') as output_file:
        output_writer = csv.writer(output_file, delimiter=",")
        for nbu in nbu_list:
            output_writer.writerow(
                [
                    nbu.timestamp,
                    nbu.server,
                    nbu.interface_name,
                    nbu.net_bit_rate,
                ]
            )
            print(f"{nbu.timestamp}, {nbu.server}, {nbu.interface_name}, {nbu.net_bit_rate}")
    



