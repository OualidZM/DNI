class calculatorLetter:
    def __init__(self,numbers):
        self.numbers = numbers

        self.tabla = [ 'T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', 'J', 
						'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E' ]

        self.no_valid = [ 'I', 'Ñ', 'O', 'U']


    def getlength(self):
        return len(self.tabla)


    def getletter(self):
        position = int(self.numbers) % self.getlength()
        letra = self.tabla[position]
        return letra

    def DNI(self):
        return str(self.numbers) + self.getletter()


    def NIF(self,letter):
        return  letter + str(self.numbers) + "-" + self.getletter()
        


    def NIE(self,letter):
        return  letter + str(self.numbers) + "-" + self.getletter()   

    def validate_length(self):
        list_length = []
        while range(len(self.numbers)):
            for i in self.numbers:
                if i == '-':
                    pass
                else:
                    list_length.append(i)
            if len(list_length) == 9:
                return True
            else:
                return False







