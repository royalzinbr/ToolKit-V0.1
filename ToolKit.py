import os

banner = r"""
    ______      __    _      __   _____             __            
   / ____/___ _/ /_  (_)__  / /  / ___/____ _____  / /_____  _____
  / /_  / __ `/ __ \/ / _ \/ /   \__ \/ __ `/ __ \/ __/ __ \/ ___/
 / __/ / /_/ / /_/ / /  __/ /   ___/ / /_/ / / / / /_/ /_/ (__  ) 
/_/    \__,_/_.___/_/\___/_/   /____/\__,_/_/ /_/\__/\____/____/
                                                ToolKit v1.0
"""
print(banner)
print(""" 
Ferramentas Disponíveis:
[0] Sair
[1] Atualizar sistema
[2] Instalar nmap
[3] Instalar wireshark
[4] Instalar hydra
[5] Instalar john the ripper
[6] Instalar sqlmap
[7] Instalar metasploit
[8] Instalar aircrack-ng
[9] Instalar burpsuite
[10] Instalar dirbuster
[11] Instalar todos
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

elif tool == 0:
    print('Saindo...')
    exit()

elif tool == 11:
    print('Instalando todas as ferramentas...')
    os.system('sudo apt update && sudo apt upgrade -y')
    os.system('sudo apt install nmap wireshark hydra john sqlmap metasploit-framework aircrack-ng burpsuite dirb -y')
    print('Todas as ferramentas instaladas com sucesso!')

else:
    print('Opção inválida!')
    exit()
