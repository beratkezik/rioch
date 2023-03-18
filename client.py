# -*- coding: utf-8 -*-

import subprocess, sys, os, ctypes

try:
    import requests, uuid
except ImportError:
    print("Gerekli modüller indiriliyor...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'requests==2.28.1', 'uuid==1.30'])
finally:
    import requests


class client():

    clear = lambda: os.system("cls")
    clear()

    def checkFile():
        if os.path.exists("main.py"):
            os.system("main.py")
        else:
            client.getSerial()


    def getSerial():
        while True:
            serial = input("Ürün anahtarını girin." + "\n" + "[?] : ")

            if len(serial) == 33:
                client.checkSerial(serial=serial)
                break
            else:
                client.clear()
                print("Lütfen geçerli bir ürün anahtarı girin!")
                ctypes.windll.user32.MessageBoxW(0, "Lütfen geçerli bir ürün anahtarı girin!", "SMS Tool", 0)


    def checkSerial(serial):
        try:
            url = "https://drive.google.com/u/0/uc?id=" + serial + "&export=download"

            r = requests.get(url=url)

            if r.status_code == 200 and r.text[0:95] == "I1NNUyBUb29sIGJ5IFdpcGVyCiNnaXRodWI6IGh0dHBzOi8vZ2l0aHViLmNvbS93aXBlcmRldgojZGM6IFdpcGVyIzA1NjU":
                client.updateFile(serial=serial)
                os.system("main.py")
            else:
                client.clear()
                print("Yanlış ürün anahtarı!")
                ctypes.windll.user32.MessageBoxW(0, "Yanlış ürün anahtarı!", "SMS Tool", 0)
                client.getSerial()
        except:
            client.clear()
            print("Bilinmeyen bir hata oluştu. Lütfen geliştirici ile iletişim kurun.")
            ctypes.windll.user32.MessageBoxW(0, "Bilinmeyen bir hata oluştu. Lütfen geliştirici ile iletişim kurun.", "SMS Tool", 0)
            client.getSerial()


    def updateFile(serial):
        if os.path.exists("main.py"):
            os.remove("main.py")
        with open("main.py", "w", encoding="UTF-8") as file:
            file.write("# -*- coding: utf-8 -*-" + "\n")
            file.write("\n")
            file.write("import requests, base64, os, ctypes" + "\n")
            file.write("\n")
            file.write("code = None" + "\n")
            file.write("\n")
            file.write('print("Ürün anahtarı kontrol ediliyor...")' + "\n")
            file.write("\n")
            file.write("while True:" + "\n")
            file.write("\t" + "try:" + "\n")
            file.write("\t" + "\t" + 'url = "https://drive.google.com/u/0/uc?id=' + serial + '&export=download"' + "\n")
            file.write("\t" + "\n")
            file.write("\t" + "\t" + "r = requests.get(url=url)" + "\n")
            file.write("\t" + "\n")
            file.write("\t" + "\t" + 'if r.status_code == 200 and r.text[0:95] == "I1NNUyBUb29sIGJ5IFdpcGVyCiNnaXRodWI6IGh0dHBzOi8vZ2l0aHViLmNvbS93aXBlcmRldgojZGM6IFdpcGVyIzA1NjU":' + "\n")
            file.write("\t" + "\t" + "\t" + "code = r.text" + "\n")
            file.write("\t" + "\t" + "\t" + "break" + "\n")
            file.write("\t" + "\t" + "else:" + "\n")
            file.write("\t" + "\t" + "\t" + 'ctypes.windll.user32.MessageBoxW(0, "Ürün anahtarınız geçersiz!", "SMS Tool", 0)' + "\n")
            file.write("\t" + "\t" + "\t" + "try:" + "\n")
            file.write("\t" + "\t" + "\t" + "\t" + 'os.remove("main.py")' + "\n")
            file.write("\t" + "\t" + "\t" + "except:" + "\n")
            file.write("\t" + "\t" + "\t" + "\t" + "pass" + "\n")
            file.write("\t" + "\t" + "\t" + 'os.system("client.py")' + "\n")
            file.write("\t" + "except:" + "\n")
            file.write("\t" + "\t" + 'ctypes.windll.user32.MessageBoxW(0, "Bilinmeyen bir problem oluştu.", "SMS Tool", 0)' + "\n")
            file.write("\t" + "\t" + "try:" + "\n")
            file.write("\t" + "\t" + "\t" + 'os.remove("main.py")' + "\n")
            file.write("\t" + "\t" + "except:" + "\n")
            file.write("\t" + "\t" + "\t" + "pass" + "\n")
            file.write("\t" + "\t" + 'os.system("client.py")' + "\n")
            file.write("\n")
            file.write("exec(base64.b64decode(code))")
            file.close()


client.checkFile()