import http.server
import socketserver 
from colorama import Fore, init

init()
#banner
def banner():
	banner = f"""

{Fore.GREEN}███╗░░██╗████████╗████████╗██████╗{Fore.CYAN}░░██████╗███████╗██████╗░██╗░░░██╗███████╗██████╗░
{Fore.GREEN}███║░░██║╚══██╔══╝╚══██╔══╝██╔══██╗{Fore.CYAN}██╔════╝██╔════╝██╔══██╗██║░░░██║██╔════╝██╔══██╗
{Fore.GREEN}████████║░░░██║░░░░░░██║░░░██████╔╝{Fore.CYAN}╚█████╗░█████╗░░██████╔╝╚██╗░██╔╝█████╗░░██████╔╝
{Fore.GREEN}███╔══██║░░░██║░░░░░░██║░░░██╔═══╝{Fore.CYAN}░░╚═══██╗██╔══╝░░██╔══██╗░╚████╔╝░██╔══╝░░██╔══██╗
{Fore.GREEN}███║░░██║░░░██║░░░░░░██║░░░██║{Fore.CYAN}░░░░░██████╔╝███████╗██║░░██║░░╚██╔╝░░███████╗██║░░██║
{Fore.GREEN}█╚═╝░░╚═╝░░░╚═╝░░░░░░╚═╝░░░╚═╝{Fore.CYAN}░░░░░╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝	
	Developed By : shayan-jn5
	
"""
	print(banner)
banner()
#setup http server
class HTTPServer:
	def __init__(self,host,port):
		Handler = http.server.SimpleHTTPRequestHandler

		with socketserver.TCPServer((host, port), Handler) as httpd:
		    print(f"{Fore.GREEN}[+]{Fore.WHITE}http://{host}:", port)
		    httpd.serve_forever()
#start progress of setup	
def start():
	print(f'{Fore.RED}[00]{Fore.WHITE} Setup HTTP Server')
	print()
	print(f'{Fore.YELLOW}'+'-'*30+f'{Fore.WHITE}')
	#choose server mode
	optioninput = input('OPTION : ')
	print(f'{Fore.YELLOW}'+'-'*30+f'{Fore.WHITE}')

	if optioninput == '00':
		print(f'{Fore.RED}[*]{Fore.WHITE} Select Your Host')
		print(f'{Fore.RED}[*]{Fore.WHITE} We Suggest[localhost]')
		print()
		print(f'{Fore.RED}[00]{Fore.WHITE}localhost')
		print(f'{Fore.RED}[01]{Fore.WHITE}Custom host')
		print()
		print(f'{Fore.YELLOW}'+'-'*30+f'{Fore.WHITE}')
		#select host 
		hostinput = str(input('OPTION : '))
		print(f'{Fore.YELLOW}'+'-'*30+f'{Fore.WHITE}')
		if hostinput == '00':
			Host = 'localhost'
		elif hostinput == '01':
			Host = str(input('Host : '))
		else:
			raise TypeError
			exit()
		print(f'{Fore.RED}[*]{Fore.WHITE} Select Your Port ')
		print(f'{Fore.RED}[*]{Fore.WHITE} We Suggest[1024]')
		print()
		print(f'{Fore.YELLOW}'+'-'*30+f'{Fore.WHITE}')
		#typing port
		portinput = int(input('Port : '))
		print(f'{Fore.YELLOW}'+'-'*30+f'{Fore.WHITE}')
		#call httpserver class
		HTTPServer(host = Host, port = portinput)
			

	else:
			raise TypeError
			exit()
		
#call start function		
start()		
		
