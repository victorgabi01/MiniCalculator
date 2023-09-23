class MiniCalculator:
    def __init__(self, zero = 0.0):
        self.zero = zero #valoarea de start a calculatorului
    def operatii_mini_calcualtor(self):
        print(self.zero) # printam valoarea de start
        comanda = input('> ') #dam de la tastatura operatii urmate de numere
        while comanda != 'x': #cat timp comanda este diferita de x calculatorul va face operatii succesive

            if '+' in comanda:
                numar  = float(comanda.split('+')[1]) #eliminam semnul  de calcul cu split, apoi convertim string-ul in float
                self.zero = self.zero + numar         #[0] index semn, [1] index numar
            elif '-' in comanda:
                numar = float(comanda.split('-')[1])
                self.zero = self.zero - numar
            elif '*' in comanda:
                numar = float(comanda.split('*')[1])
                self.zero = self.zero * numar
            elif'/' in comanda:
                numar = float(comanda.split('/')[1])
                self.zero = self.zero / numar
            elif '=' in comanda:
                numar = float(comanda.split('=')[1])
                self.zero =  numar
            else:
                print(f'Invalid operation {self.zero}')

            print(self.zero) #ne afiseaza rezultatul
            comanda = input('>')# ne pune iar sa folosim o operatie si un numar



