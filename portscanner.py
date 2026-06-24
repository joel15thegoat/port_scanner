import socket 
import concurrent. futures 
def scan_port (port) : 
  try: 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    sock. settimeout (3)
    result = sock. connect_ex(("127.0.0.1", port)) 
    if result == 0: 
      print (f"Port {port} is open") 
      sock. close () 
  except Exception as e: 
    print (f"Error: {e}") 
def mass_scan (ports) : 
  with concurrent. futures. ThreadPoolExecutor() as executor: 
    executor.map(scan_port, ports) 
# Usage 
ports = range(1, 1025) 
mass_scan (ports)
