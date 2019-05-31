import json

data = '''a ponto traço b traço ponto ponto ponto c traço ponto traço ponto d traço ponto ponto e ponto f ponto ponto traço ponto g traço traço ponto h ponto ponto ponto ponto i ponto ponto j ponto traço traço traço k traço ponto traço l ponto traço ponto ponto m traço traço n traço ponto o traço traço traço p ponto traço traço ponto q traço traço ponto traço r ponto traço ponto s ponto ponto ponto t traço u ponto ponto traço v ponto ponto ponto traço w ponto traço traço x traço ponto ponto traço y traço ponto traço traço z traço traço ponto ponto 1 ponto traço traço traço traço 2 ponto ponto traço traço traço 3 ponto ponto ponto traço traço 4 ponto ponto ponto ponto traço 5 ponto ponto ponto ponto ponto 6 traço ponto ponto ponto ponto 7 traço traço ponto ponto ponto 8 traço traço traço ponto ponto 9 traço traço traço traço ponto 0 traço traço traço traço traço'''


def fn(x):
    if x == 'traço':
        return True, '111'
    if x == 'ponto':
        return True, '1'
    return False, x

d = {}
key = None
for w in data.split(' '):
    r, x = fn(w)
    if not r:
        key = x
        d[key] = ''
    else:
        if not d[key] == '':
            d[key] += '0'
        d[key] = d[key] + x

print(json.dumps(d))