from Tabla import TablaAsignacion
import inquirer
class DNi:
    
    
    def __init__(self):
        self.tabla = TablaAsignacion
        # self.dni = False
        # self.nif = False
        # self.nie = False


    def ask(self):


        question = inquirer.list_input(message="Encontrar: ", choices=['DNI','NIE','NIF'])

        if question == 'DNI': #si 
            dni_number_list = []#agrega llista buida

            question_dni = inquirer.text(message="escribe 8 numeros")#demanam per numeros
            to_int =  int(question_dni)
            dni_number_list.append(to_int)

            # dni_number_list.append(numbers_split)#afegim aquets numeros a una lista

            if dni_number_list == ['']:  #comprobar que no esta buida
                error = inquirer.list_input(message="Something went wrong: ", choices=['Try Again', 'Break'])#si esta buida donar dos opcions
                if error == 'Try Again':
                    return ii.ask()
                else:
                    if error == 'Break':
                        return
            else:
                if len(dni_number_list) == 8:
                    print(self.tabla.obtener_letra(self,dni_number_list),sep="")

                else:
                    if len(dni_number_list) !=8:
                        ask_if_repit = inquirer.list_input(message="something went wrong, Do yo want to repeat Again?",choices=['No','Yes'])
                        if ask_if_repit == 'Yes':
                            return ii.ask()
                        else:
                            if ask_if_repit == 'No':
                                return
                        




        elif question == 'NIE':

            nie_number_list = []
            select_first_leter_nie = inquirer.list_input(message="select first leter for NIE: ", choices=['X','Y','Z'])
            if select_first_leter_nie == 'X':
                X_inpt_numb = inquirer.text(message="input max 7 numbers")
                nie_number_list.append(X_inpt_numb)
            elif select_first_leter_nie == 'Y':
                Y_inpt_numb = inquirer.text(message="input max 7 numbers")
                nie_number_list.append(Y_inpt_numb)
            
            else:
                if select_first_leter_nie == 'Z':
                    Z_inpt_numb = inquirer.text(message="input max 7 numbers")
                    nie_number_list.append(Z_inpt_numb)


        else:
            if question == 'NIF':

                select_first_leter_nif = inquirer.list_input(message="select first leter for NIE: ", choices=['K','L','M'])

                nif_number_list = []
                if select_first_leter_nif == 'K':
                    K_nif_number = inquirer.text(message="Insert a max of 7 numbers: ")
                    nif_number_list.append(K_nif_number)
                    
                elif select_first_leter_nif == 'L':
                    L_nif_number = inquirer.text(message="insert a max of 7 numbers: ")
                    nif_number_list.append(L_nif_number)
                else:
                    if nif_number_list == 'M':
                        M_nif_number = inquirer.text(message="insert a max of 7 numbers: ")
                        nif_number_list.append(M_nif_number)






    # def Dni_i(self):

    #     # if

    #     if input(len(self.number)) == 8 and self.number[:-1] == self.tabla:    
    #         return self.dni == True
    #     else:
    #         return False
        
    # def Nif(self):

    #     if input(self.number) == 8 and self.number[:-1] == self.tabla:    
    #         return self.dni == True
    #     else:
    #         return False

    # def Nie(self):

    #     if input(self.number) == 8 and self.number[:-1] == self.tabla:    
    #         return self.dni == True
    #     else:
    #         return False

    #     self.tabla
    #     if 'X' or 'Y':
    #         return self.nie == True
    #     else:
    #         False


if __name__ == "__main__":
    ii =  DNi()
    ii.ask()
