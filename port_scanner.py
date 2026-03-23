import socket
import time

target = input("Enter IP address: ")

start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))

print(f"\nScanning target: {target}")
print(f"Scanning ports from {start_port} to {end_port}...\n")

start_time = time.time()

open_ports = []

try:
    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.3)  

        result = s.connect_ex((target, port))

        if result == 0:
            print(f"[OPEN] Port {port}")
            open_ports.append(port)

        s.close()

    end_time = time.time()

    print("\nScanning completed.")
    print(f"Time taken: {end_time - start_time:.2f} seconds")

    print(f"\nTotal open ports: {len(open_ports)}")
    print(f"Open ports: {open_ports}")

except:
    print("Error: Invalid input or network issue")
