import uuid
from uuid import getnode
import socket
import subprocess

def get_mac():
  mac_num = hex(uuid.getnode()).replace('0x', '').upper()
  mac = ''.join(mac_num[i : i + 2] for i in range(0, 11, 2))
  return mac

a = get_mac()
subprocess.call(["C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe","D:\client\pkgs\ClientF\process.ps1;"])
s = socket.socket()

#host = socket.gethostname()
port = 60000

s.connect(('192.168.173.220', port))
s.send(str(a))


with open('abcd.txt', 'rb') as f:
	print("file opened")
	l=f.read(1024)
	while(1):
		s.send(l)
		print('sent: ', repr(l))
		l=f.read(1024)
		if not l:
		 break
	f.close()
print('file sent')
s.close()
print('connection closed')
