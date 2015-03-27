from __future__ import print_function
from collections import OrderedDict, namedtuple
import urllib2
import socket
import platform as pl

def meminfo():
	meminfo = OrderedDict()

	with open('/proc/meminfo') as f:
		for line in f:
			meminfo[line.split(':')[0]] = line.split(':')[1].strip()
		return meminfo
def inet():
	try:
		response = urllib2.urlopen('http://google.com', timeout = 1)
		return True
	except urllib2.URLError as err: pass
	return False

def cpuinfo():
	with open('/proc/cpuinfo') as f:
		for line in f:
			if line.strip():
				if line.rstrip('\n').startswith('model name'):
					model_name = line.rstrip('\n').split(':')[1]
					return model_name

if __name__ == '__main__':
	host = '192.168.0.16'
	port = 5000

	s = socket.socket()
	s.connect((host, port))
	
	meminfo = meminfo()
	inetCon = inet()
	cpu = cpuinfo()

	s.send("\nEstado (Conexion a internet): " + str(inetCon))
	s.send("CPU: " + cpu + " " + pl.processor())
	s.send("\nMemoria: {0}".format(meminfo['MemTotal']))
	s.send("\nSistema Operativo: " + pl.system() + " " + pl.release())
	s.send("\nArquitectura: " + str(pl.architecture())) 

	s.close()
