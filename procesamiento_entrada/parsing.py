from typing import List


class Parser:
    def __init__(self, input_string):
        self.input = list(input_string)
        self.current_token = None

    def parse(self) -> List[str]:
        try:
            self.current_token = self.__get_next_token()
            return self.__oracion()
        except ValueError as e:
            print(e)
            raise ValueError('La oración no forma parte de la lengua española')

    def load_input(self, input_string):
        self.input = list(input_string)
        self.current_token = None

    def __get_next_token(self):
        if self.input:
            return self.input.pop(0)
        else:
            return None

    def __match(self, token):
        if self.current_token == token:
            self.current_token = self.__get_next_token()
        else:
            raise ValueError(f"Caracter invalido: se esperaba: '{token}'")

    def __oracion(self):
        if self.__es_letra(self.current_token):
            return [self.__palabra()] + self.__cuerpo()
        else:
            self.__simbolo()
            return self.__cuerpo()

    def __cuerpo(self):
        if self.current_token is None:
            return []
        if self.__es_letra(self.current_token):
            return [self.__palabra()] + self.__cuerpo()
        else:
            self.__simbolo()
            return self.__cuerpo()

    def __palabra(self):
        return self.__letra() + self.__cola()

    def __cola(self):
        if self.current_token is None:
            return ''
        if self.__es_letra(self.current_token):
            return self.__letra() + self.__cola()
        else:
            return self.__simbolo()

    def __letra(self):
        if self.current_token == 'a':
            self.__match('a')
            return 'a'
        if self.current_token == 'b':
            self.__match('b')
            return 'b'
        if self.current_token == 'c':
            self.__match('c')
            return 'c'
        if self.current_token == 'd':
            self.__match('d')
            return 'd'
        if self.current_token == 'e':
            self.__match('e')
            return 'e'
        if self.current_token == 'f':
            self.__match('f')
            return 'f'
        if self.current_token == 'g':
            self.__match('g')
            return 'g'
        if self.current_token == 'h':
            self.__match('h')
            return 'h'
        if self.current_token == 'i':
            self.__match('i')
            return 'i'
        if self.current_token == 'j':
            self.__match('j')
            return 'j'
        if self.current_token == 'k':
            self.__match('k')
            return 'k'
        if self.current_token == 'l':
            self.__match('l')
            return 'l'
        if self.current_token == 'm':
            self.__match('m')
            return 'm'
        if self.current_token == 'n':
            self.__match('n')
            return 'n'
        if self.current_token == 'ñ':
            self.__match('ñ')
            return 'ñ'
        if self.current_token == 'o':
            self.__match('o')
            return 'o'
        if self.current_token == 'p':
            self.__match('p')
            return 'p'
        if self.current_token == 'q':
            self.__match('q')
            return 'q'
        if self.current_token == 'r':
            self.__match('r')
            return 'r'
        if self.current_token == 's':
            self.__match('s')
            return 's'
        if self.current_token == 't':
            self.__match('t')
            return 't'
        if self.current_token == 'u':
            self.__match('u')
            return 'u'
        if self.current_token == 'v':
            self.__match('v')
            return 'v'
        if self.current_token == 'w':
            self.__match('w')
            return 'w'
        if self.current_token == 'x':
            self.__match('x')
            return 'x'
        if self.current_token == 'y':
            self.__match('y')
            return 'y'
        if self.current_token == 'z':
            self.__match('z')
            return 'z'
        if self.current_token == 'A':
            self.__match('A')
            return 'a'
        if self.current_token == 'B':
            self.__match('B')
            return 'b'
        if self.current_token == 'C':
            self.__match('C')
            return 'c'
        if self.current_token == 'D':
            self.__match('D')
            return 'd'
        if self.current_token == 'E':
            self.__match('E')
            return 'e'
        if self.current_token == 'F':
            self.__match('F')
            return 'f'
        if self.current_token == 'G':
            self.__match('G')
            return 'g'
        if self.current_token == 'H':
            self.__match('H')
            return 'h'
        if self.current_token == 'I':
            self.__match('I')
            return 'i'
        if self.current_token == 'J':
            self.__match('J')
            return 'j'
        if self.current_token == 'K':
            self.__match('K')
            return 'k'
        if self.current_token == 'L':
            self.__match('L')
            return 'l'
        if self.current_token == 'M':
            self.__match('M')
            return 'm'
        if self.current_token == 'N':
            self.__match('N')
            return 'n'
        if self.current_token == 'Ñ':
            self.__match('Ñ')
            return 'ñ'
        if self.current_token == 'O':
            self.__match('O')
            return 'o'
        if self.current_token == 'P':
            self.__match('P')
            return 'p'
        if self.current_token == 'Q':
            self.__match('Q')
            return 'q'
        if self.current_token == 'R':
            self.__match('R')
            return 'r'
        if self.current_token == 'S':
            self.__match('S')
            return 's'
        if self.current_token == 'T':
            self.__match('T')
            return 't'
        if self.current_token == 'U':
            self.__match('U')
            return 'u'
        if self.current_token == 'V':
            self.__match('V')
            return 'v'
        if self.current_token == 'W':
            self.__match('W')
            return 'w'
        if self.current_token == 'X':
            self.__match('X')
            return 'x'
        if self.current_token == 'Y':
            self.__match('Y')
            return 'y'
        if self.current_token == 'Z':
            self.__match('Z')
            return 'z'
        if self.current_token == 'á':
            self.__match('á')
            return 'á'
        if self.current_token == 'é':
            self.__match('é')
            return 'é'
        if self.current_token == 'í':
            self.__match('í')
            return 'í'
        if self.current_token == 'ó':
            self.__match('ó')
            return 'ó'
        if self.current_token == 'ú':
            self.__match('ú')
            return 'ú'
        if self.current_token == 'Á':
            self.__match('Á')
            return 'á'
        if self.current_token == 'É':
            self.__match('É')
            return 'é'
        if self.current_token == 'Í':
            self.__match('Í')
            return 'í'
        if self.current_token == 'Ó':
            self.__match('Ó')
            return 'ó'
        if self.current_token == 'Ú':
            self.__match('Ú')
            return 'ú'
        if self.current_token == 'ü':
            self.__match('ü')
            return 'ü'
        else:
            self.__match('Ü')
            return 'ü'

    def __simbolo(self):
        if self.current_token == ' ':
            self.__match(' ')
            return ''
        if self.current_token == ',':
            self.__match(',')
            return ''
        if self.current_token == '.':
            self.__match('.')
            return ''
        if self.current_token == ';':
            self.__match(';')
            return ''
        if self.current_token == ':':
            self.__match(':')
            return ''
        if self.current_token == '¡':
            self.__match('¡')
            return ''
        if self.current_token == '!':
            self.__match('!')
            return ''
        if self.current_token == '¿':
            self.__match('¿')
            return ''
        if self.current_token == '?':
            self.__match('?')
            return ''
        if self.current_token == '(':
            self.__match('(')
            return ''
        if self.current_token == ')':
            self.__match(')')
            return ''
        if self.current_token == '[':
            self.__match('[')
            return ''
        if self.current_token == ']':
            self.__match(']')
            return ''
        if self.current_token == '{':
            self.__match('{')
            return ''
        if self.current_token == '}':
            self.__match('}')
            return ''
        if self.current_token == "'":
            self.__match("'")
            return ''
        if self.current_token == "\"":
            self.__match("\"")
            return ''
        if self.current_token == "\n":
            self.__match("\n")
            return ''
        if self.current_token == "\t":
            self.__match('\t')
            return ''
        if self.current_token == '-':
            self.__match('-')
            return ''
        else:
            self.__match('_')
            return ''

    @staticmethod
    def __es_letra(char):
        return char in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZñÑáéíóúÁÉÍÓÚüÜ"

    @staticmethod
    def __es_simbolo(char):
        return char in " ,.;:¡!¿?'\"()\n\t[]{}-_"


if __name__ == '__main__':
    input = '¡Hola, esto es una frase de prueba! Además, agrego palabras con acento - ¿Y si tiene salto de linea?'
    parser = Parser(input)
    print(parser.parse())
