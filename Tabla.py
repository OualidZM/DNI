class TablaAsignacion:
    def __init__(self):
        self.tabla = [ 'T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', 'J', 
						'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E' ]
                        
        self.no_in_tabla = [ 'I', 'Ñ', 'O', 'U']


    def getleng(self):
        return len(self.tabla)
        


    def letra_no_in_tabla(self):
        try:
            if self.no_in_tabla != self.tabla:
                return True
        except:
                return False

    def letra(self):
        for letra in self.tabla:
            self.tabla.index(letra)

    def obtener_letra(self,dni_number_list):

        if Tabla_cc.letra_no_in_tabla() == True and Tabla_cc.getleng() == 23:
            
            int(dni_number_list)
            resultado = dni_number_list % Tabla_cc.getleng()
            result = Tabla_cc.obtener_letra(resultado)
            
            return result






        if (0 < getleng() <= 22) and leters_no == True:
            leter = int(DNi) % getleng()

            if leter + letter_number == 9:
                return leter + letter_number
            else:
                return "something went wrong"


Tabla_cc  = TablaAsignacion()

# Aún no está terminada