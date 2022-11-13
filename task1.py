# TODO решить с помощью list comprehension и распечатать его
import pprint as pp

num_syst = ['bin', 'dec', 'hex', 'oct']
dict_of_numbers = [{"bin": bin(i), "dec": i, "hex": hex(i), "oct": oct(i)} for i in range(0, 16)]
pp.pprint(dict_of_numbers)