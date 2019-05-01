import speech_recognition as sr
import time
import socket
import os
import winsound

r = sr.Recognizer()

#Algoritmo de Speech Recognition
with sr.Microphone() as source:
	print "Iniciando protocolo de conexao..."
	time.sleep(1)
	print "[+]Caitlyn Online[+]"

	while True:

		audio = r.listen(source)

		try:

			print "Eu --> {}".format(r.recognize_google(audio, language = "pt"))
			request = str(r.recognize_google(audio, language = "pt"))
			request = request.lower()
			if request == "ip":
				request = request.upper()
			conect = request[0:8]
			tempo = time.ctime()
			site = "www.{}".format(request[9:])
			site_ip = request[0:7]
			# Specs [+]Caitlyn[+]
			if request == "protocolo de reconhecimento":
				print "\nCaitlyn --> ID: Caitlyn | Versao: 0.0.3 \n"
			if request == "toca":
				winsound.PlaySound("teste", winsound.SND_FILENAME)
			# Funcionalidades de Rede
			elif conect == "conectar":
				s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				s.connect((site, 21))
				data_recv = s.recv(1024)
				print data_recv
			elif site_ip == "ip site":
				full_site_ip = request[8:]
				ip_site_socket = socket.gethostbyname("{}".format(full_site_ip))
				print ip_site_socket
			# Horario 
			elif request == "horas":
				print tempo[11:19]
			elif request == "data":
				print tempo[0:10], tempo[20:24]
			# Funcionalidades do Sistema
			elif request == "IP":
				print os.system("ipconfig")
			elif request == "desconectar":
				break
		except:
			print "Audio Ilegivel"