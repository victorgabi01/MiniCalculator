class MiniCalculator:
    def __init__(self, zero = 0.0):
        self.zero = zero #valoarea de start a calculatorului
    def operatii_mini_calcualtor(self):
        print(self.zero) # printam valoarea de start
        comanda = input('> ') #dam de la tastatura operatii urmate de numere
        while comanda != 'x': #cat timp comanda este diferita de x calculatorul va face operatii succesive
            try:
                operator_matematic = comanda[0] # se va alege mereu operatorul , acesta fiind mereu pe pozitia zero
                numar_ales = float(comanda[1:]) #in numar_ales, variabila diferita de numar stocam covertirea in flaot a stringului, ignorand semnul(+,=,-..) de pe poz. [0]
                # print(f'Numarul ales este {numar_ales}') #daca decomentam vom vedea cum a vem operator si numar ales
                # print(f'Operatorul este {operator_matematic}')
                if operator_matematic in ('+', '-', '*', '/'): #verificam existenta operatorilor

                    if operator_matematic == '+': #daca avem + in comanda de la stringul +40 de ex se executa
                        self.zero = self.zero + numar_ales
                        print(self.zero)  # ne afiseaza rezultatul

                    elif operator_matematic == '-':
                        self.zero = self.zero - numar_ales
                        print(self.zero)  # ne afiseaza rezultatul

                    elif operator_matematic == '*':
                        self.zero = self.zero * numar_ales
                        print(self.zero)  # ne afiseaza rezultatul

                    elif operator_matematic == '/':
                        if numar_ales == 0:  # imparitrea la 0 nu se poate
                            try:  # facem incercare si exceptie
                                rezultat = self.zero / numar_ales
                            except ZeroDivisionError:
                             print(f'Invalid operation {self.zero}')  # exceptam eroarea si in loc de eroare printam mesajul

                        else:
                            self.zero = self.zero / numar_ales
                            print(self.zero)  # ne afiseaza rezultatul

                elif operator_matematic == '=':
                    self.zero = numar_ales
                    print(self.zero)  # ne afiseaza rezultatul


                else: #daca avem alte input-uri cu operatii gresite afisam invalidarea ex (%6)
                    print(f'Invalid operation {self.zero}')

            except ValueError: #exceptam eroarea daca ceea ce am introdus nu e float (+123faasd) si printam invalidarea
                print(f'Invalid operation {self.zero}')

            comanda = input('>')# ne pune iar sa folosim o operatie si un numar(face parte din while)



