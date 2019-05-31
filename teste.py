class Teste:
    def prnt(self):
        print('ok')

    A = {
        'a': prnt
    }

    def call(self):
        f = Teste.A.get('a')
        f(self)

t = Teste()
t.call()
