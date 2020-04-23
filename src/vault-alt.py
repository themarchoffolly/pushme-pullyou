from diagrams import Cluster, Diagram
from diagrams.onprem.security import Vault
from diagrams.onprem.network import Consul

with Diagram("Clustered Production Vault Service", show=False):

  with Cluster("Vault Production"):
    vault_prod = Vault("node1")
    vault_prod - [Vault("node2"), Vault("node3")]

  with Cluster("Consul Production"):
    c_prod = [Consul("consul_server1"),
              Consul("consul_server2"),
              Consul("consul_server3"),
              Consul("consul_server4"),
              Consul("consul_server5")]

    c_prod >> vault_prod
