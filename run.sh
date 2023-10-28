#!/bin/bash

# Start Mininet with a custom Python script
sudo mn --custom custom_topology.py --topo mytopo

# You can also add additional commands to run inside Mininet, for example:
# sudo mn --custom custom_topology.py --topo mytopo --command "python /path/to/myscript.py"

# Additional commands can be added as needed
