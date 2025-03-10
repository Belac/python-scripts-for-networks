import socket
from colorama import init, Fore


def is_port_open(host, port):
    """determine whether `host` has the `port` open"""
    # creates a new socket
    s = socket.socket()
    try:
        # tries to connect to host using that port
        s.connect((host, port))
        # make timeout if you want it a little faster ( less accuracy )
        s.settimeout(0.2)
    except:
        # cannot connect, port is closed
        return False
    else:
        # the connection was established, port is open!
        return True


init()
GREEN, RESET, GRAY = Fore.GREEN, Fore.RESET, Fore.LIGHTBLACK_EX
host = input("Enter the host: ")
for port in range(79, 1025):
    if is_port_open(host, port):
        print(f"{GREEN}[+] {host}:{port} is open        {RESET}")
    else:
        print(f"{GRAY}[!] {host}:{port} is closed        {RESET}", end="\r")
