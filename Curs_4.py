
                                              # TUPLES



# my_tuple = (1, 2, 3)
# # my_tuple2 = 1,2                          # si daca nu pui  paranteze il vede ca si tuple
# # print(*my_tuple)                         # steluta iti scoate parantezele cand rulezi (sa arate mai bine)
# # print(type(my_tuple2))

# my_tuple = (1,2,3,4,5,6,7,8,9)
# print(my_tuple[4:8])

# my_tuple  = (1,2,True, False, 1, 2, "sda")    # in tuple putem avea mai multe valori
# print(1 in my_tuple)                         # in = daca e adevarat ca avem 1 in tuple



# unpackinng a tuple
# my_tuple = (1,2, True, False)
# a,b,c,d = my_tuple                          # despachetare
#
# print(a)
# print(b)
# print(c)
# print(d)

# my_tuple = (1,2, True, False, 33,55,66)
# a,b,c,*d = my_tuple
#                                                # Asterixul face ca tot ce mai urmeaza sa fie lista
# print(a)
# print(b)
# print(c)
# print(d)
# a,b,*c,d,f = my_tuple
#                                               # a,b sunt primele doua elemente, c-ul devine lista , d,f ultimele doua.
# print(a)                                       # c-ul devine lista pana in momentul cand vine urmatorul caracter
# print(b)
# print(c)
# print(d)
# print(f)
#


# my_tuple =(1,2,3)
#
# my_list = list(my_tuple)
# my_list[0] = "a"
#
# print(my_list)
# my_tuple = tuple(my_list)
# print(my_tuple)


# my_tuple1 = (1,2,3)
# my_tuple2 = (3,4,5)
# my_tuple3 = my_tuple1 + my_tuple2
# print(my_tuple3)


# my_tuple1 = (1,2,3)
# my_tuple2 = my_tuple1*3
# print(my_tuple2)

                                          # Exercitii
#my_tuple = ("ford","mercedes","bmw","cielo","renault","skoda","vw")

# a,b,*c,d = my_tuple
# print(a)
# print(b)
# print(c)
# print(d)

# one_element_tuple = ("mazda",)                       # tuple merge si fara paranteze DAR trebuie pus VIRGULA ca altfel il oia ca si string
# new_tuple = my_tuple + one_element_tuple
# print(new_tuple)


# my_list = list(my_tuple)
# my_list.append("mazda")
# print(my_list)                      # este LISTA ca e cu paranteze drepte
# my_tuple = tuple(my_list)
# print(my_tuple)                    # este TUPLE ca e cu paranteze rotunde
#
#

# print("renault" in my_tuple)         # functia in ne arata daca avem ce valoare vrem in tuple

# my_tuple = (1,2, True, [15,20], "test")
# print(my_tuple)
# print(my_tuple[3][1])                  # scoate numarul 20 din lista
#






                                               # SETS


# my_set = {1,2,3,4,5,5,5,5}             # in seturi ne scoate duplicatele
# print(my_set)
# my_set.add(32)
# print(my_set)
# my_set.update([44,66,77])
# print(my_set.remove(3))                    # la funnctia remove daca nu gaseste ce vrem sa scoatem ne da erroare
# print(my_set)
#
#









