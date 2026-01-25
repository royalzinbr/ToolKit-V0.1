import os

banner = r"""
    ______      __    _      __     _____           __            
   / ____/___ _/ /_  (_)__  / /  / ___/____ _____  / /_____  _____
  / /_  / __ `/ __ \/ / _ \/ /   \__ \/ __ `/ __ \/ __/ __ \/ ___/
 / __/ / /_/ / /_/ / /  __/ /   ___/ / /_/ / / / / /_/ /_/ (__  ) 
/_/    \__,_/_.___/_/\___/_/   /____/\__,_/_/ /_/\__/\____/____/
                                                ToolKit v0.1
"""
print(banner)
print(""" 
Ferramentas Disponíveis:
[1] Atualizar sistema
[2] instalar nmap
[3] instalar wireshark
[4] instalar hydra
[5] instalar john the ripper
[6] instalar sqlmap
[7] instalar metasploit
[8] instalar aircrack-ng
[9] instalar burpsuite
[10] instalar dirbuster
[] Atualizar Sair
""")

tool = int(input('Escolha a ferramenta: '))
if tool == 1:
    print('Atualizando sistema...')
    os.system('sudo apt update && sudo apt upgrade -y')
    print('Sistema atualizado com sucesso!')

elif tool == 2:
    print('Instalando nmap...')
    os.system('sudo apt install nmap -y')
    print('nmap instalado com sucesso!')

elif tool == 3:
    print('Instalando wireshark...')
    os.system('sudo apt install wireshark -y')
    print('wireshark instalado com sucesso!')

elif tool == 4:
    print('Instalando hydra...')
    os.system('sudo apt install hydra -y')
    print('hydra instalado com sucesso!')

elif tool == 5:
    print('Instalando john the ripper...')
    os.system('sudo apt install john -y')
    print('john the ripper instalado com sucesso!')

elif tool == 6:
    print('Instalando sqlmap...')
    os.system('sudo apt install sqlmap -y')
    print('sqlmap instalado com sucesso!')

elif tool == 7:
    print('Instalando metasploit...')
    os.system('sudo apt install metasploit-framework -y')
    print('metasploit instalado com sucesso!')  

elif tool == 8: 
    print('Instalando aircrack-ng...')
    os.system('sudo apt install aircrack-ng -y')
    print('aircrack-ng instalado com sucesso!')

elif tool == 9:
    print('Instalando burpsuite...')
    os.system('sudo apt install burpsuite -y')
    print('burpsuite instalado com sucesso!')

elif tool == 10:
    print('Instalando dirb...')
    os.system('sudo apt install dirb -y')
    print('dirb instalado com sucesso!')

elif tool == 11:
    print('Saindo...')
    exit()