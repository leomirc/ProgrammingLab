class Calcolatrice:

    def somma(self, a, b):

        a_new = a
        b_new = b

        assert self.tipo_corretto(a, b), 'Number type not matching or invalid'
        if type(a) is str and type(b) is str:
            a_new = float(a)
            b_new = float(b)

        return a_new + b_new


    def sottrazione(self, a, b):

        a_new = a
        b_new = b

        assert self.tipo_corretto(a, b), 'Number type not matching or invalid'
        if type(a) is str and type(b) is str:
            a_new = float(a)
            b_new = float(b)

        return a_new - b_new


    def moltiplicazione(self, a, b):

        a_new = a
        b_new = b

        assert self.tipo_corretto(a, b), 'Number type not matching or invalid'
        if type(a) is str and type(b) is str:
            a_new = float(a)
            b_new = float(b)

        return a_new * b_new


    def divisione(self, a, b):

        a_new = a
        b_new = b

        assert self.tipo_corretto(a, b), 'Number type not matching or invalid'
        if type(a) is str and type(b) is str:
            a_new = float(a.strip())
            b_new = float(b.strip())

        assert b != 0, 'Cant divide by zero'

        return a_new / b_new


    def potenza(self, a, b):

        a_new = a
        b_new = b

        assert self.tipo_corretto(a, b), 'Number type not matching or invalid'
        if type(a) is str and type(b) is str:
            assert a.isnumeric() and b.isnumeric(), 'Only integers are allowed'
            a_new = int(a.strip())
            b_new = int(b.strip())
        else:
            assert type(a) == type(b) == int, 'Only integers are allowed'

        return pow(a_new, b_new)


    def modulo(self, a, b):

        a_new = a
        b_new = b

        assert self.tipo_corretto(a, b), 'Number type not matching or invalid'
        if type(a) is str and type(b) is str:
            a_new = float(a.strip())
            b_new = float(b.strip())

        assert b != 0, 'Cant divide by zero'

        return a_new % b_new


    def radice(self, a):

        import math

        a_new = a

        assert type(a) in [int, str], 'Invalid type'
        if type(a) is str:
            assert a.isnumeric(), 'Invalid input'
            a_new = float(a.strip())

        assert a_new >= 0, 'Only positive numbers are allowed'

        return math.sqrt(a_new)


    def conversione_base_10_2(self, a):

        a_new = a

        assert type(a) in [int, str], 'Invalid type'
        if type(a) is str:
            assert a.isnumeric(), 'Invalid input'
            a_new = int(a.strip())

        return bin(a_new)[2:]


    def tipo_corretto(self, a, b):
        if type(a) is str and type(b) is str: return True
        elif (type(a), type(b)) not in [int, float]: return True
        else: return False