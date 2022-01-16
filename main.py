from configparser import ConfigParser
import os
import sys
import configparser
import os.path
from os import path
import requests
from cryptography.fernet import Fernet, MultiFernet
import base64, hashlib
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import zipfile
import atexit
import ctypes

class Functions:

    # ------------------------------------------------------------------
    #                              Gerais
    # ------------------------------------------------------------------

    def ProcuraEmArray(self, array, array_valores_a_achar):
        i = 0
        achado = False
        indexs = []
        for a_achar in array_valores_a_achar:
            for argumento in array:
                if(a_achar == argumento):
                    indexs.append(i)
                    achado = True

            i = i +1
            # antes de pular para o próximo
            if (achado == False):
                indexs.append(None)
            elif(achado == True):
                achado = False
        return indexs

    def VerificaInternet(url='http://www.google.com/', timeout=5):  
        try:
            _ = requests.head(url, timeout=timeout)
            return True
        except requests.ConnectionError:
            print("Voce não está conectado a internet.")
        return False

    def LimparTerminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def ExisteNoArray(self, array, valor_a_procurar):
        for values in array:
            if(valor_a_procurar == values):
                return True
            else:
                return False

    def RecebeParametros(self, array ,valores_a_achar):
        ''' 
            Descricao:
                retorna o index no valor no array a procurar

            Parametros:
                array array: valor onde deve procurar
                array valores_a_achar: valor a procurar
        '''

        #verifica se todos os valores existem
        for valor_a_procurar in valores_a_achar:
            if(self.ExisteNoArray(array, valor_a_procurar) == False):
                return False
        
        array_final = []

        for parametro in array:
            for valor in valores_a_achar:
                if(parametro == valores_a_achar):
                    array_final.append(sys.argv.index(valores_a_achar))
        
        return array_final
    
    def TextoVermelho(self, texto):
        return("\033[1;31;40m"+texto+"\033[0;37;40m")

    def TextoVerde(self, texto):
        return("\033[1;32;40m"+texto+"\033[0;37;40m")
    
    def TextoAzul(self, texto):
        return("\033[1;36;40m"+texto+"\033[0;36;40m")

    def TextoAmarelo(self, texto):
        return("\033[1;33;40m"+texto+"\033[0;36;40m")

    # ------------------------------------------------------------------
    #                              Logs
    # ------------------------------------------------------------------

    def LerLogs(Logs_File: "logs.txt"):
        file1 = open(Logs_File,"r")
        Linhas = file1.readlines()
        file1.close()
        return Linhas

    def EscreverLog(Logs_File: "logs.txt", Array_Escrever):
        file1 = open(Logs_File,"w")
        file1.writelines(Array_Escrever)
        file1.close()

    def AdicionarLog(Logs_File: "logs.txt", Array_Escrever ):
        Linhas = LerLogs(Logs_File)
        Linhas_a_escrver = Linhas + Array_Escrever
        EscreverLog(Logs_File, Linhas_a_escrver)
        
    # ------------------------------------------------------------------
    #                              Ficheiros
    # ------------------------------------------------------------------

    def FicheirosNoDiretorio(diretorio):
        for root, dirs, files in os.walk(diretorio):
            for filename in files:
                print(filename)

    def ZipaPasta(nome_ficheiro_zip: str, pasta: str):

        if ((".zip" in nome_ficheiro_zip) == False):
            nome_ficheiro_zip = nome_ficheiro_zip +".zip" 

        zf = zipfile.ZipFile(nome_ficheiro_zip, "w")
        for dirname, subdirs, files in os.walk(pasta):
            zf.write(dirname)
            for filename in files:
                if(filename != nome_ficheiro_zip):
                    # print("A adicionar o ficheiro: " + filename + " - "+ dirname)
                    zf.write(os.path.join(dirname, filename))
        zf.close()
        if(os.path.isfile(nome_ficheiro_zip) == True):
            print("Ficheiro Zipado com Sucesso!")
        elif(os.path.isfile(nome_ficheiro_zip) == False):
            print("Ocorreu um erro ao Zipar o ficheiro!")
        pass

    # ------------------------------------------------------------------
    #                              Ascii
    # ------------------------------------------------------------------
    def AsciiAviso(self):                                               
                                                                           
        print("\033[1;33;40m")
                                                                                                
        print("                                                                                        ")
        print("                ░░░░                                                                    ")
        print("                                                                                        ")
        print("                                            ██                                          ")
        print("                                          ██░░██                                        ")
        print("  ░░          ░░                        ██░░░░░░██                            ░░░░      ")
        print("                                      ██░░░░░░░░░░██                                    ")
        print("                                      ██░░░░░░░░░░██                                    ")
        print("                                    ██░░░░░░░░░░░░░░██                                  ")
        print("                                  ██░░░░░░██████░░░░░░██                                ")
        print("                                  ██░░░░░░██████░░░░░░██                                ")
        print("                                ██░░░░░░░░██████░░░░░░░░██                              ")
        print("                                ██░░░░░░░░██████░░░░░░░░██                              ")
        print("                              ██░░░░░░░░░░██████░░░░░░░░░░██                            ")
        print("                            ██░░░░░░░░░░░░██████░░░░░░░░░░░░██                          ")
        print("                            ██░░░░░░░░░░░░██████░░░░░░░░░░░░██                          ")
        print("                          ██░░░░░░░░░░░░░░██████░░░░░░░░░░░░░░██                        ")
        print("                          ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██                        ")
        print("                        ██░░░░░░░░░░░░░░░░██████░░░░░░░░░░░░░░░░██                      ")
        print("                        ██░░░░░░░░░░░░░░░░██████░░░░░░░░░░░░░░░░██                      ")
        print("                      ██░░░░░░░░░░░░░░░░░░██████░░░░░░░░░░░░░░░░░░██                    ")
        print("        ░░            ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██                    ")
        print("                        ██████████████████████████████████████████                      ")
        print("                                                                                        ")
        print("                                                                                        ")
        print("                                                                                        ")
        print("                                                                                        ")
        print("                  ░░                                                                    ")

        print("\033[0;37;40m\n")
        
    def AsciiErro(self):
        print("\033[1;31;40m")
        print(",adPPYba, 8b,dPPYba, 8b,dPPYba,  ,adPPYba,  8b,dPPYba,  ")
        print("a8P_____88 88P'   'Y8 88P'   'Y8 a8'     '8a 88P'   'Y8 ") 
        print("8PP''''''' 88         88         8b       d8 88         ") 
        print("'8b,   ,aa 88         88         '8a,   ,a8' 88         ") 
        print(" `'Ybbd8'' 88         88          `'YbbdP''  88         ") 
        print("\033[0;37;40m\n")

class Encriptar:
    key = None
    Config_file = None
    ficheiro_da_chave = None

    def __init__(self, config_file = None):
        self.Config_file = config_file
        pass
    
    def carregar_chave(self, ficheiro = 'filekey.key'):
        """
        Carrega a chave
        """
        return open(ficheiro, "rb").read()

    def GerarPass(self):
        # Gera a key 
        key = Fernet.generate_key()
        self.key = key

        # guarda a key no ficheiro 
        with open('filekey.key', 'wb') as filekey:
            filekey.write(key)
        pass

    def CriaPass(self, passw):
        password_do_utilizador = passw
        password = password_do_utilizador.encode() # converte para bytes

        salt = b'\xaes\kff\x80\xe2{{\xfcG\xbdk\xed\xb9\x15n7'
        kdf = PBKDF2HMAC (
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        self.key = base64.urlsafe_b64encode(kdf.derive(password))

        # guarda a key no ficheiro 
        with open('filekey.key', 'wb') as filekey:
            filekey.write(self.key)
        pass

    def Encriptar(self, ficheiro, key_file = None):
        # usa a chave 
        if(key_file == None):
            fernet = Fernet(self.carregar_chave()) 
        else:
            fernet = Fernet(open(key_file, "rb").read()) 
        
        
        # abre o ficheiro e le
        with open(ficheiro, 'rb') as file: 
            original = file.read() 
            
        # encripta
        encrypted = fernet.encrypt(original) 
        
        # abre o ficheiro e escreve
        with open(ficheiro, 'wb') as encrypted_file: 
            encrypted_file.write(encrypted) 
        pass

    def Desencriptar(self, ficheiro, key_file = None):
        # usa a key existente
        if(key_file == None):
            fernet = Fernet(self.carregar_chave()) 
        else :
            fernet = Fernet(open(key_file, "rb").read()) 

        # abre o arquivo encriptado
        with open(ficheiro, 'rb') as enc_file: 
            encrypted = enc_file.read() 
        
        # desencripta o ficheiro 
        decrypted = fernet.decrypt(encrypted) 
        
        # abre o ficheiro e escrve ele desencriptado
        with open(ficheiro, 'wb') as dec_file: 
            dec_file.write(decrypted) 
        pass

class Program:
    __CONFIG_FILE__ = 'Config.ini'

    Ini = ConfigParser() 
    Encriptar = None
    func = None
    Ini.read(__CONFIG_FILE__)

    def __init__(self, EncriptarClass: None, FunctionsClass: None):
        if(EncriptarClass == None or FunctionsClass == None):
            raise Exception("Algum esta None")

        self.Encriptar = EncriptarClass
        self.func = FunctionsClass
        pass

    def Titulo(self): # mostra opcoes apenas do menu e slogan e etc
            print("██╗  ██╗     ███████╗███╗   ██╗ ██████╗██████╗ ██╗   ██╗██████╗ ████████╗██╗ ██████╗ ███╗   ██╗")
            print("╚██╗██╔╝     ██╔════╝████╗  ██║██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║")
            print(" ╚███╔╝█████╗█████╗  ██╔██╗ ██║██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║   ██║██║   ██║██╔██╗ ██║")
            print(" ██╔██╗╚════╝██╔══╝  ██║╚██╗██║██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║   ██║██║   ██║██║╚██╗██║")
            print("██╔╝ ██╗     ███████╗██║ ╚████║╚██████╗██║  ██║   ██║   ██║        ██║   ██║╚██████╔╝██║ ╚████║")
            print("╚═╝  ╚═╝     ╚══════╝╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝")
    
    def Menu(self, menu_a_mostrar: None):
        if(menu_a_mostrar == None):
            return
        if(menu_a_mostrar.upper() == "MP"): # MP = Menu Principal
            print('------------------- Menu -----------------------\n')
            print('1- Gerar key')
            print('2- Encriptar')
            print('3- Desenciptar')
            print('4- Carregar key')
            print('5- Encripta pasta')
            print('0- Sair do programa')
            print ('------------------- Fim Menu -----------------------\n')
            return input("Opção: ")
                                                                                                
    def ValidaParametros(self):
        # kf - Key File | f - file | ks - key String
        
        return True
        if(("-encrypt" in sys.argv or "-e" in sys.argv) and "-kf" in sys.argv and "-f" in sys.argv):
            if(len(sys.argv) == 6):
                key = func.RecebeParametros(sys.argv, ["-kf", "-f"])[0] +1
                ficheiro = func.RecebeParametros(sys.argv, ["-kf", "-f"])[1] +1

                self.Encriptar.Encriptar(ficheiro, key)
                print('Ficheiro encriptado com sucesso!')
                input("Press Enter to continue...")
                return True

        elif(("-decrypt" in sys.argv or "-d" in sys.argv)and "-kf" in sys.argv and "-f" in sys.argv):
            if(len(sys.argv) == 6):
                key = func.RecebeParametros(sys.argv, ["-kf", "-f"])[0] +1
                ficheiro = func.RecebeParametros(sys.argv, ["-kf", "-f"])[1] +1

                self.Encriptar.Desencriptar(ficheiro, key)
                print('Ficheiro Desencriptado com sucesso!')
                input("Press Enter to continue...")
                return True
        
        return False

    def Main(self):

        ctypes.windll.kernel32.SetConsoleTitleW("X-ENCRYPTION")

        # if(self.ValidaParametros() == True):
        #     return
        
        # se nao haver parametros 
        opcao = "99"
        while opcao != "0":
            self.func.LimparTerminal()
            self.Titulo()
            opcao = self.Menu(menu_a_mostrar="MP")
            if (opcao == "1"): # Gera Pass
                self.MP_Opcao_1()
            elif(opcao == "2"): # Encripta Ficheiro
                self.MP_Opcao_2()
            elif(opcao == "3"): # Desencripta
                self.MP_Opcao_3()
            elif(opcao == "4"): # Carrega Chave
                self.MP_Opcao_4()
            elif(opcao == "5"): # Carrega Chave
                self.MP_Opcao_5()
            elif(opcao == "0"): # Sair do Programa
                self.MP_Opcao_0()

        pass

    def MP_Opcao_1(self):
        self.func.LimparTerminal()
        if(path.exists("filekey.key") == False):
            print("------------ Opções ------------------")
            print("1- Criar uma pass personalizada")
            print("2- Gerar uma pass \n")
            x = input("Escolha: ")
            if(x == "2"):
                self.Encriptar.GerarPass()
            elif(x == "1"):
                self.func.LimparTerminal()
                self.Encriptar.CriaPass(input("Password: "))

            self.func.LimparTerminal()
            print('Key gerada com sucesso! \n')
            input("Press Enter to continue...")
        else:
            print('O ficheiro Key ja existe!')
            x = input('Pretende mesmo assim alterar a key (S/N): ')
            if(x.upper() == 'S' or x.upper() == '1'):
                self.func.LimparTerminal()
                print("------------ Opções ------------------")
                print("1- Criar uma pass personalizada")
                print("2- Gerar uma pass \n")
                x = input("Escolha: ")
                if(x == "1"):
                    self.func.LimparTerminal()
                    self.Encriptar.CriaPass(input("Password: "))
                elif(x == "2"):
                    self.Encriptar.GerarPass()
                self.func.LimparTerminal()
                print('Key gerada com sucesso! \n')
                input("Press Enter to continue...")
            else:
                input("Press Enter to continue...")

    def MP_Opcao_2(self):
        self.Encriptar.Encriptar(input('\nFicheiro: '))
        print('Ficheiro encriptado com sucesso!')
        input("Press Enter to continue...")
    
    def MP_Opcao_3(self):
        self.Encriptar.Desencriptar(input('\nFicheiro: '))
        print('Ficheiro Desencriptado com sucesso!')
        input("Press Enter to continue...")

    def MP_Opcao_4(self):
        func.LimparTerminal()

        self.Encriptar.carregar_chave(input('Ficheiro com a chave: '))
        print('Chave Carregada com Sucesso!')

        input("Press Enter to continue...")

    def MP_Opcao_5(self):
        pasta = input('Pasta a Encriptar: ')
        if(os.path.isdir(pasta) == False):
            raise Exception ({'Texto': 'O valor colocado não é uma pasta!', 'Numero': 2})
        nome_ficheiro_zip = input('Nome do ficheiro a exportar: ')

        if ((".zip" in nome_ficheiro_zip) == False):
            nome_ficheiro_zip = nome_ficheiro_zip +".zip" 

        zf = zipfile.ZipFile(nome_ficheiro_zip, "w")
        for dirname, subdirs, files in os.walk(pasta):
            zf.write(dirname)
            for filename in files:
                if(filename != nome_ficheiro_zip):
                    # print("A adicionar o ficheiro: " + filename + " - "+ dirname)
                    zf.write(os.path.join(dirname, filename))
        zf.close()
        self.Encriptar.Encriptar(nome_ficheiro_zip)

    def MP_Opcao_0(self):
        print('A Sair do Programa!')
        input("Press Enter to continue...")
        os.system('cls' if os.name == 'nt' else 'clear')
        exit()

while True:
    try:
        func = Functions()
        enc = Encriptar()
        p = Program(EncriptarClass=enc, FunctionsClass=func)
        p.Main()
    except SystemExit:
        break
    except KeyboardInterrupt:
        func.LimparTerminal()
        x = input("Tem a certeza que quer sair do Programa? (S/N)\nResposta: ")
        if(x.upper() == "S" or x == "1"):
            print("\nA sair do programa")
            input("Clique em qualquer tecla para continuar")
            func.LimparTerminal()
            break
        elif(x.upper() == "N" or x == "0"):
            continue
    except FileNotFoundError:
        func.LimparTerminal()
        func.AsciiAviso()
        print(func.TextoVermelho("Colocaste o nome do ficheiro ou o caminho errado!"))
        input("Clique em qualquer tecla para continuar")
        continue

    except Exception as e:
        func.LimparTerminal()
        func.AsciiErro()
        # print(e)
        # print(sys.exc_info()[0])
        # print("Erro inesperado:", sys.exc_info()[0], "\n")
        print (func.TextoVermelho("Erro inesperado: "+ str(sys.exc_info()[0])+ "\n"))
        input("Clique em qualquer tecla para continuar")
        func.LimparTerminal()
        continue