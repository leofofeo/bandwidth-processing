# Bandwith calculation

The bandwith utilization processing script is made up of three modules:

## models

The `models` module contains the class `NetworkBandwidthUtil`, which captures the expected information from the `netbitrate.csv` and create a self-contained object from which the `network_interface_name` is calculated. This allows for straightforward data association for later output; each object contains the information necessary for each output row.

## process

The `process` module contains three main functions:

### create_network_interfaces

`create_network_interfaces` takes the path of the `bandwidth.csv` file and parses through the file, creating unique keys in a dict that match the network interface name (derived from each parsed row's `server` + `interface_name`). The value associated with each key is the `netbitrate` included in each row. It is assumed that network interfaces are unique, and as such, if a duplicate were to be found in a row, it would override the previous netbit rate. The `dict` of `network_interfaces` is returned

### calculate_network_bandwidth_utilization

`calculate_network_bandwidth_utilization` takes in the path of the `netbitrate.csv` and the `dict` returned from `create_network_interfaces`. It iterates over the csv file and creates a `NetWorkbadnwidthUtil` object for each row, storing the information from each row in the appropriate object property. It uses the object's calculated interface name to check the network interfaces `dict` for that name, and if found, recalculates the object's stored net bit rate using the value from the `dict`. Each object is appendd to a `list`, which is returned at the end of the function

### write_output

`write_output` takes in the `list` of calculated network bandwidth utilization objects as well as the path to the output file. It iterates over each object and writes a new row with the object's information, subsequently printing that object's data out as well

## main

`main.py` is the entry point into the program. It sets the path files and imperatively calls the appropriate functions from `process`