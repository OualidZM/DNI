from DNI import calculatorLetter



def test_get_letter_dni():

    assert calculatorLetter(87691254).getletter() == 'M'
    assert calculatorLetter(99999999).getletter() == 'R'
    assert calculatorLetter(87162536).getletter() == 'B'
    assert calculatorLetter(12345678).getletter() == 'Z'
    assert calculatorLetter(33333333).getletter() == 'P'
    assert calculatorLetter(11111111).getletter() == 'H'
    assert calculatorLetter(65473829).getletter() == 'M'
    assert calculatorLetter(87679812).getletter() == 'V'
    assert calculatorLetter(34563213).getletter() == 'D'
    assert calculatorLetter(87691254).getletter() == 'M'
    assert calculatorLetter(56743289).getletter() == 'N'
    assert calculatorLetter(11226654).getletter() == 'D'
    assert calculatorLetter(73298765).getletter() == 'L'
    assert calculatorLetter(88888888).getletter() == 'Y'

def test_DNI_letter():

    assert calculatorLetter(87162536).DNI() == '87162536B'
    assert calculatorLetter(99999999).DNI() == '99999999R'
    assert calculatorLetter(12345678).DNI() == '12345678Z'
    assert calculatorLetter(33333333).DNI() == '33333333P'
    assert calculatorLetter(11111111).DNI() == '11111111H'
    assert calculatorLetter(65473829).DNI() == '65473829M'
    assert calculatorLetter(87679812).DNI() == '87679812V'
    assert calculatorLetter(34563213).DNI() == '34563213D'
    assert calculatorLetter(87691254).DNI() == '87691254M'
    assert calculatorLetter(56743289).DNI() == '56743289N'
    assert calculatorLetter(11226654).DNI() == '11226654D'
    assert calculatorLetter(73298765).DNI() == '73298765L'
    assert calculatorLetter(88888888).DNI() == '88888888Y'

def test_get_letter_NIF():

    assert calculatorLetter(6543782).getletter() == 'Y'
    assert calculatorLetter(1234567).getletter() == 'L'
    assert calculatorLetter(7678239).getletter() == 'B'
    assert calculatorLetter(9999999).getletter() == 'J'
    assert calculatorLetter(8765432).getletter() == 'V'
    assert calculatorLetter(8765123).getletter() == 'F'
    assert calculatorLetter(7777234).getletter() == 'Z'
    assert calculatorLetter(6965432).getletter() == 'C'
    assert calculatorLetter(1233356).getletter() == 'G'
    assert calculatorLetter(9976215).getletter() == 'B'
    assert calculatorLetter(1453782).getletter() == 'K'
    assert calculatorLetter(6548721).getletter() == 'T'
    assert calculatorLetter(1592473).getletter() == 'E'
    assert calculatorLetter(1298653).getletter() == 'G'
    assert calculatorLetter(4376982).getletter() == 'J'
    assert calculatorLetter(1234987).getletter() == 'W'

def test_NIF_letter():

    assert calculatorLetter(6543782).NIF('L') == 'L6543782-Y'
    assert calculatorLetter(1234567).NIF('K') == 'K1234567-L'
    assert calculatorLetter(7678239).NIF('M') == 'M7678239-B'
    assert calculatorLetter(9999999).NIF('K') == 'K9999999-J'
    assert calculatorLetter(8765432).NIF('L') == 'L8765432-V'
    assert calculatorLetter(8765123).NIF('M') == 'M8765123-F'
    assert calculatorLetter(7777234).NIF('L') == 'L7777234-Z'
    assert calculatorLetter(6965432).NIF('M') == 'M6965432-C'
    assert calculatorLetter(1233356).NIF('L') == 'L1233356-G'
    assert calculatorLetter(9976215).NIF('L') == 'L9976215-B'
    assert calculatorLetter(1453782).NIF('M') == 'M1453782-K'
    assert calculatorLetter(6548721).NIF('K') == 'K6548721-T'
    assert calculatorLetter(1592473).NIF('K') == 'K1592473-E'
    assert calculatorLetter(1298653).NIF('M') == 'M1298653-G'
    assert calculatorLetter(4376982).NIF('L') == 'L4376982-J'
    assert calculatorLetter(1234987).NIF('K') == 'K1234987-W'

def test_get_letter_NIE():

    assert calculatorLetter(3332256).getletter() == 'Q'
    assert calculatorLetter(5555555).getletter() == 'C'
    assert calculatorLetter(2718345).getletter() == 'K'
    assert calculatorLetter(9985541).getletter() == 'E'
    assert calculatorLetter(1928374).getletter() == 'P'
    assert calculatorLetter(9876548).getletter() == 'A'
    assert calculatorLetter(1278435).getletter() == 'A'
    assert calculatorLetter(8866446).getletter() == 'S'
    assert calculatorLetter(6669714).getletter() == 'J'
    assert calculatorLetter(4433221).getletter() == 'V'
    assert calculatorLetter(7654921).getletter() == 'S'
    assert calculatorLetter(9898989).getletter() == 'L'
    assert calculatorLetter(2222222).getletter() == 'P'
    assert calculatorLetter(4445567).getletter() == 'N'
    assert calculatorLetter(8799123).getletter() == 'J'

def test_NIE_letter():

    assert calculatorLetter(3332256).NIE('X') == 'X3332256-Q'
    assert calculatorLetter(5555555).NIE('Z') == 'Z5555555-C'
    assert calculatorLetter(2718345).NIE('Y') == 'Y2718345-K'
    assert calculatorLetter(9985541).NIE('X') == 'X9985541-E'
    assert calculatorLetter(1928374).NIE('X') == 'X1928374-P'
    assert calculatorLetter(9876548).NIE('Z') == 'Z9876548-A'
    assert calculatorLetter(1278435).NIE('X') == 'X1278435-A'
    assert calculatorLetter(8866446).NIE('X') == 'X8866446-S'
    assert calculatorLetter(6669714).NIE('Y') == 'Y6669714-J'
    assert calculatorLetter(4433221).NIE('Z') == 'Z4433221-V'
    assert calculatorLetter(7654921).NIE('X') == 'X7654921-S'
    assert calculatorLetter(9898989).NIE('X') == 'X9898989-L'
    assert calculatorLetter(2222222).NIE('Z') == 'Z2222222-P'
    assert calculatorLetter(4445567).NIE('X') == 'X4445567-N'
    assert calculatorLetter(8799123).NIE('Y') == 'Y8799123-J'

def test_check_lenght():

    assert calculatorLetter('87162536B').validate_length() == True
    assert calculatorLetter('99999999R').validate_length() == True
    assert calculatorLetter('Y2718345-K').validate_length() == True
    assert calculatorLetter('12345678912').validate_length() == False
    assert calculatorLetter('99999999').validate_length() == False
    assert calculatorLetter('Y8799123-J').validate_length() == True
    assert calculatorLetter('763548212216273').validate_length() == False
    assert calculatorLetter('34563213').validate_length() == False
    assert calculatorLetter('73298765').validate_length() == False
    assert calculatorLetter('K1234987-W').validate_length() == True
    assert calculatorLetter('L6543782-Y').validate_length() == True

