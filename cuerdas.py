#   -----  Clase -----
class Proyecto:
    def __init__(self, p_con, p_gen):
        self.p_con = p_con
        self.p_gen = p_gen
      
    def p_red(self):
        print(f'Lo que consume ve la red en P es: {self.p_con - self.p_gen}')
        return self.p_con - self.p_gen


if __name__ == '__main__':
proyecto = Proyecto(10, 5)
proyecto.p_red()
