from pprint import pprint
l_dict = [{'bin': bin(i), 'dec': i, 'hex': hex(i), 'oct': oct(i)} for i in range(16)]

pprint(l_dict)
