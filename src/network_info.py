import psutil
import socket

def get_network_info():
    """
    Retrieve detailed network information.
    
    Returns:
        dict: A dictionary containing various network details.
    """
    network_info = {}
    
    # Get network interfaces
    interfaces = psutil.net_if_addrs()
    network_info['interfaces'] = {}
    
    for interface, addrs in interfaces.items():
        network_info['interfaces'][interface] = []
        for addr in addrs:
            addr_info = {
                'family': str(addr.family),
                'address': addr.address,
                'netmask': addr.netmask,
                'broadcast': addr.broadcast
            }
            network_info['interfaces'][interface].append(addr_info)
    
    # Get network I/O statistics
    io_counters = psutil.net_io_counters(pernic=True)
    network_info['io_stats'] = {}
    
    for interface, stats in io_counters.items():
        network_info['io_stats'][interface] = {
            'bytes_sent': f"{stats.bytes_sent / (1024**2):.2f} MB",
            'bytes_recv': f"{stats.bytes_recv / (1024**2):.2f} MB",
            'packets_sent': stats.packets_sent,
            'packets_recv': stats.packets_recv,
            'errin': stats.errin,
            'errout': stats.errout,
            'dropin': stats.dropin,
            'dropout': stats.dropout
        }
    
    # Get connection information
    connections = psutil.net_connections()
    network_info['connections'] = {
        'total': len(connections),
        'established': len([conn for conn in connections if conn.status == 'ESTABLISHED']),
        'listening': len([conn for conn in connections if conn.status == 'LISTEN'])
    }
    
    # Get hostname and IP address
    network_info['hostname'] = socket.gethostname()
    network_info['ip_address'] = socket.gethostbyname(socket.gethostname())
    
    return network_info

def print_network_info():
    """
    Print the network information in a formatted manner.
    """
    network_info = get_network_info()
    
    print("Network Information:")
    print(f"\nHostname: {network_info['hostname']}")
    print(f"IP Address: {network_info['ip_address']}")
    
    print("\nNetwork Interfaces:")
    for interface, addrs in network_info['interfaces'].items():
        print(f"\n  {interface}:")
        for addr in addrs:
            print(f"    Family: {addr['family']}")
            print(f"    Address: {addr['address']}")
            print(f"    Netmask: {addr['netmask']}")
            print(f"    Broadcast: {addr['broadcast']}")
    
    print("\nNetwork I/O Statistics:")
    for interface, stats in network_info['io_stats'].items():
        print(f"\n  {interface}:")
        print(f"    Bytes Sent: {stats['bytes_sent']}")
        print(f"    Bytes Received: {stats['bytes_recv']}")
        print(f"    Packets Sent: {stats['packets_sent']}")
        print(f"    Packets Received: {stats['packets_recv']}")
        print(f"    Errors In: {stats['errin']}")
        print(f"    Errors Out: {stats['errout']}")
        print(f"    Drops In: {stats['dropin']}")
        print(f"    Drops Out: {stats['dropout']}")
    
    print("\nNetwork Connections:")
    print(f"  Total: {network_info['connections']['total']}")
    print(f"  Established: {network_info['connections']['established']}")
    print(f"  Listening: {network_info['connections']['listening']}")

if __name__ == "__main__":
    print_network_info()
