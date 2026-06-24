# port_scanner
A lightweight, multi-threaded port scanner written in Python. It scans ports 1–1024 on local host (127.0.0.1) using a thread pool, identyfying open ports

## Features
- Fast concurrent scanning with `concurrent.futures`
- Adjustable timeout and port range
- Clean, minimal code perfect for learning

## Usage
**1. Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/port-scanner.git
   cd port-scanner
   ``` 
**2. run the script:**
```bash
python scanner.py
```
## Customization
- Change the target IP by replacing `127.0.0.1` 
- Adjust the port range by modifying `ports = range(start, end).`
- Tweak the timeout with `sock.settimeout(seconds).`

## License
- this is published under the MIT [licenece](https://mit-license.org/)
