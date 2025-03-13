import socket

def scan_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Timeout for the connection attempt
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"Port {port} is open on {host}")
        else:
            print(f"Port {port} is closed on {host}")
        sock.close()
    except Exception as e:
        print(f"Error scanning port {port} on {host}: {e}")

def main():
    host = input("Enter the host to scan: ")
    ports = input("Enter the ports to scan (comma-separated): ")
    ports = [int(port.strip()) for port in ports.split(",")]

    for port in ports:
        scan_port(host, port)

if __name__ == "__main__":
    main()
