import socket

def is_proxy_reachable(proxy_host, proxy_port):
    try:
        # Create a socket connection to the proxy server
        with socket.create_connection((proxy_host, proxy_port), timeout=10):
            print("Proxy is reachable.")
            return True
    except (socket.timeout, ConnectionError):
        print("Unable to reach the proxy.")
        return False

# Replace these values with your proxy's IP and port
proxy_host = "146.190.35.152"
proxy_port = "8000"

is_proxy_reachable(proxy_host, proxy_port)

#ELITE with https

#PREVIOUS IS REACHABLE
# PROXY = "144.126.141.115:1010"
# PROXY = "195.35.32.249:80"
# PROXY = "162.246.248.214:80"

