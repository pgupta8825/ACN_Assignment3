from mininet.net import Mininet
from mininet.node import OVSSwitch, Controller
from mininet.topo import Topo

class CustomTopology(Topo):
    def build(self):
        # Add 3 switches to the topology
        switch1 = self.addSwitch('s1')
        switch2 = self.addSwitch('s2')
        switch3 = self.addSwitch('s3')

        # Add 4 hosts to the topology
        host1 = self.addHost('h1')
        host2 = self.addHost('h2')
        host3 = self.addHost('h3')
        host4 = self.addHost('h4')

        # Connect hosts to switches
        self.addLink(host1, switch1)
        self.addLink(host2, switch1)
        self.addLink(host3, switch2)
        self.addLink(host4, switch3)

        # Connect switches together
        self.addLink(switch1, switch2)
        self.addLink(switch2, switch3)

# Create Mininet network with the custom topology
net = Mininet(topo=CustomTopology(), switch=OVSSwitch, controller=Controller)

# Start the network
net.start()

# You can now access and configure the network as needed
# For example, you can open Mininet CLI:
# net.interact()

# Stop the network when you are done
net.stop()
