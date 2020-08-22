import socket as s

hostname= s.gethostname()
ip_addr= s.gethostbyname(hostname)

print(f'Your Computer Name is {hostname} and Your IP Addr is {ip_addr}')

input()