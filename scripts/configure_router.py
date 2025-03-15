from netmiko import ConnectHandler

router = {
    "device_type": "cisco_ios",
    "host": "192.168.1.1",
    "username": "admin",
    "password": "password",
}

def configure_router():
    conn = ConnectHandler(**router)
    conn.send_command("configure terminal")
    conn.send_command("hostname AutomatedRouter")
    conn.send_command("end")
    print("Configuration Applied!")

if __name__ == "__main__":
    configure_router()
