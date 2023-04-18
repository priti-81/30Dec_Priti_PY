import string
 
test_str = 'Gfg, is best: for ! Geeks ;'

test1 = test_str.translate(str.maketrans('', '', string.punctuation))
print(test1)
