dico_data = {}
manufacturers = [1, 2, 3, 4, 5]
manufac_enc = [5, 4, 3, 2, 1]

i = 0
for elt in manufacturers:
    if elt not in dico_data:
        dico_data[elt] = manufac_enc[i]
    i += 1
print(dico_data)
