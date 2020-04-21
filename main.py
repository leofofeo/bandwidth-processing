from process import (
    create_network_interfaces, 
    calculate_network_bandwidth_utilization, 
    write_output,
)

bandwidth_path = './input/bandwidth.csv'
netbitrate_path = './input/netbitrate.csv'
output_path = './output/results.csv'

network_interfaces = create_network_interfaces(bandwidth_path)
network_bandwidth_utils = calculate_network_bandwidth_utilization(
    netbitrate_path, 
    network_interfaces,
)
write_output(output_path, network_bandwidth_utils)