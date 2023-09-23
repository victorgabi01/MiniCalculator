class MiniCalculator:
    def __init__(self, zero = 0.0):
        self.zero = zero #valoarea de start a calculatorului
    def operatii_mini_calcualtor(self):
        print(self.zero) # printam valoarea de start
        comanda = input('> ') #dam de la tastatura operatii urmate de numere
        while comanda != 'x': #cat timp comanda este diferita de x calculatorul va face operatii succesive
            try:
                numar_ales = float(comanda.split(comanda[0])[1]) #in numar_ales, variabila diferita de numar stocam covertirea in flaot a stringului, eliminand semnul(+,=,-..) de pe poz. [0] cu functia split

                if isinstance(numar_ales , float): #verificam daca numarul este float, daca da , mergem in if-uri de sub el

                    if '+' in comanda: #daca avem + in comanda de la stringul +40 de ex se executa
                        numar = float(comanda.split('+')[1])  # eliminam semnul  de calcul cu split, apoi convertim string-ul in float
                        self.zero = self.zero + numar  # [0] index semn, [1] index numar
                        print(self.zero)  # ne afiseaza rezultatul

                    elif '-' in comanda:
                        numar = float(comanda.split('-')[1])
                        self.zero = self.zero - numar
                        print(self.zero)  # ne afiseaza rezultatul

                    elif '*' in comanda:
                        numar = float(comanda.split('*')[1])
                        self.zero = self.zero * numar
                        print(self.zero)  # ne afiseaza rezultatul

                    elif '/' in comanda:
                        numar = float(comanda.split('/')[1])
                        if numar == 0:  # imparitrea la 0 nu se poate
                            try:  # facem incercare si exceptie
                                rezultat = self.zero / numar
                            except ZeroDivisionError:
                             print(f'Invalid operation {self.zero}')  # exceptam eroarea si in loc de eroare printam mesajul

                        else:
                            self.zero = self.zero / numar
                            print(self.zero)  # ne afiseaza rezultatul

                    elif '=' in comanda:
                        numar = float(comanda.split('=')[1])
                        self.zero = numar
                        print(self.zero)  # ne afiseaza rezultatul


                    else: #daca avem alte input-uri cu operatii gresite afisam invalidarea ex (%6)
                        print(f'Invalid operation {self.zero}')

            except ValueError: #exceptam eroarea daca ceea ce am introdus nu e float (+123faasd) si printam invalidarea
                print(f'Invalid operation {self.zero}')

            comanda = input('>')# ne pune iar sa folosim o operatie si un numar(face parte din while)



