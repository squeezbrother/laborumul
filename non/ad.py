test_list = ['glacoxia(pre-reincorporation)', 'glaco(xia( test)', 'glacoxia(abbys)', 'glacoxia(abbys-terarosa)']
new_list = [s.replace('(', '').replace(')', '') for s in test_list]
print(new_list)
