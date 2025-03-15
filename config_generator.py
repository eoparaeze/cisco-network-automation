def generate_config(hostname, interface, ip):
    config = f"""
    hostname {hostname}
    interface {interface}
    ip address {ip} 255.255.255.0
    no shutdown
    """
    return config

if __name__ == "__main__":
    print(generate_config("Router1", "GigabitEthernet0/1", "192.168.1.1"))
