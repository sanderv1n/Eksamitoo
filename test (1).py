from sys import exit
from math import sqrt

class Kalkulaator:
    def liida(self, a, b): # liitmine
        return a + b
    def lahuta(self, a, b): # lahutamine
        return a - b
    def korruta(self, a, b): # korrutamine
        return a * b
    def jaga(self, a, b): # jagamine
        if b == 0:
            return "Nulliga jagada ei saa"
        return a / b
    def jääk(self, a, b): # jääk
        return a % b
    def astenda(self, a, b): # astendamine
        return a ** b

    def keskmine(self, a, b): # keskmine
        return sum([a, b]) / 2
    def suurem(self, a, b): # suurem
        return a > b # True, kui a on suurem kui b
    def väiksem(self, a, b): # väiksem
        return a < b # True, kui a on väiksem kui b
    def ruutjuur(self, a): # ruutjuur
        return sqrt(a)


    def alusta(self): # Alustamise meetod
        while True: # while True, et programm jookseks kuni kasutaja lõpetab
            while True: # while True, et küsida
                op = input("Sisestage tehe:\n"
                           "Liitmine - [+]\n"
                           "Lahutamine - [-]\n"
                           "Korrutamine - [*]\n"
                           "Jagamine - [/]\n"
                           "Astendamine - [**]\n"
                           "Ruutjuur - [sqrt]\n"
                           "Jääk - [%]\n"
                           "Keskmine - [avg]\n"
                           "Suurem - [>]\n"
                           "Väiksem - [<]\n"
                           "(Sulge - [x]): ")
                if op == "x":
                    exit() # exit suleb programmi
                elif op in ["+", "-", "*", "/", "**", "%", ">", "<", "sqrt", "avg"]: # kui saime valiidse operaatori, lõpetame küsimise
                    self.op = op
                    break
                else: # kui ei saanud soovitud operaatorit, küsime uuesti
                    print(str(op) + " ei ole valiidne tehe")

            if self.op == "sqrt": # ruutjuurega on ainult ühte arvu vaja
                num1 = input("Sisestage arv (Sulge [x]): ")
                if num1 == "x":
                    exit()
                elif num1.isdigit(): # kontrollime, et oleks number
                    self.num1 = float(num1) # teeme ujukomaarvuks
                    print(self.ruutjuur(self.num1)) # väljastame ruutjuure
                else: # kui ei olnud x ega number, küsime uuesti
                    print(str(num1) + " ei ole valiidne arv")
            else: # kõigi teisega on kaks arvu
                while True:
                    num1 = input("Sisestage esimene arv (Sulge [x]): ")
                    if num1 == "x":
                        exit()
                    elif num1.isdigit():
                        self.num1 = float(num1)
                        break
                    else:
                        print(str(num1) + " ei ole valiidne arv")

                while True:
                    num2 = input("Sisestage teine arv (Sulge [x]): ")
                    if num2 == "x":
                        exit()
                    elif num2.isdigit():
                        self.num2 = float(num2)
                        break
                    else:
                        print(str(num2) + " ei ole valiidne arv")

                if self.op == "+":
                    print(self.liida(self.num1, self.num2))
                elif self.op == "-":
                    print(self.lahuta(self.num1, self.num2))
                elif self.op == "*":
                    print(self.korruta(self.num1, self.num2))
                elif self.op == "/":
                    print(self.jaga(self.num1, self.num2))
                elif self.op == "**":
                    print(self.astenda(self.num1, self.num2))
                elif self.op == "%":
                    print(self.jääk(self.num1, self.num2))
                elif self.op == ">":
                    print(self.suurem(self.num1, self.num2))
                elif self.op == "<":
                    print(self.väiksem(self.num1, self.num2))
                elif self.op == "avg":
                    print(self.keskmine(self.num1, self.num2))


k = Kalkulaator()
k.alusta() # käivitame kalkulaatori

