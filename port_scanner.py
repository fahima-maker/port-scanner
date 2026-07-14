import socket
from datetime import datetime

print("=" * 50)
print("        PYTHON PORT SCANNER")
print("=" * 50)

target = input("Enter IP address or Website (e.g., scanme.nmap.org): ")

try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("\n[!] Invalid hostname or IP address.")
    exit()

print(f"\nScanning Target : {target}")
print(f"Resolved IP     : {target_ip}")
print(f"Scan Started    : {datetime.now()}")
print("-" * 50)

start_port = int(input("Enter Start Port: "))
end_port = int(input("Enter End Port: "))

open_ports = []

try:
    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)

        result = s.connect_ex((target_ip, port))

        if result == 0:
            print(f"[OPEN ] Port {port}")
            open_ports.append(port)

        s.close()

except KeyboardInterrupt:
    print("\nScan Interrupted by User.")
    exit()

except Exception as e:
    print(f"\nError: {e}")
    exit()

print("\n" + "=" * 50)
print("SCAN COMPLETED")
print("=" * 50)

if open_ports:
    print("Open Ports Found:")
    for port in open_ports:
        print(f"✔ Port {port}")
else:
    print("No Open Ports Found in the selected range.")

print(f"\nTotal Open Ports: {len(open_ports)}")
print(f"Finished At      : {datetime.now()}")
