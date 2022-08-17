
                                                     #  LISTS


# x = 10
# y = 20
# total = x + y
# print(total)
# total2 = x - y
# print(total2)
# total3 = x * y
# print(total3)
# total4 = y/x
# print(total4)

# total5 = x / 0
# print(total5)

#
#
# x = 7
# y = 3
# total6 = x%y
# print(total6)
#
#
# x = 2
# y = 3
# print(x**y)
#


# x = "Mere"
# y = "Pere"


# x = 5
# print(x)
# x = x + 3     # astea doua sunt la fel doar scrise diferit
# x += 3
# print(x)


# x = 10
# y = 10
# print(x == y)
#
# x = 10
# y = 10
# print(x != y)
#
# x = "10"  # aici variabila e de tip string si atunci e fals ca nu sunt egale
# y = 10
# print(x == y)
#
# x = "10a"
# y = "10"
# print(x > y)



# text = "Razvan, salut"
# print("R" in text)
# print("R" not in text)



# total = 3 + 5*2 #prima oara inmultirea apoi adunarea ca in matematica
# print(total)



# Scrie un program care sa returneze aria total si volumuul unei cutii

# latime = float(input("latime: "))
# lungime =float(input("lungime: "))
# inaltime =float(input("inaltime: "))
#
# aria_fata = latime * lungime
# aria_totala = aria_fata * 6
#
# volumul = latime * lungime * inaltime


# BMI = greutate(kg) / inaltime(m2)

# greutate = float(input("Greutate kg: "))
# inaltime = int(input("Inaltime cm: "))
#
# inaltime_m = inaltime / 100
#
# BMI = greutate/inaltime_m**2
# #print(BMI)
#
# print(f"Underweight{BMI < 18.5}")
# print(f"Normalweight{BMI >= 18.5 and BMI <= 24.9}")
# print(f"Overweight{BMI >= 25 and BMI <= 29.9}")
# print(f"Obese{BMI >= 30}")


                      # Liste


# my_list = ["mar", "banana","kiwi"]
# print(my_list)

# my_list = list(("mar", "banana", "kiwi"))
# print(my_list)

# my_list2 = ["mar", True, 2.5]
# my_list2[0] = True
#
# print(my_list2)
#

# my_list = [1,2,3]
# my_list.append(6)                   # append pune valoarea la finalul listei
# print(my_list)
#
# my_list.insert(1, "Salut")         # insert pune ce element vrem noi la indexul mentionat
# print(my_list)                     # am pus la indexul 1 sa adauge elemennul "Salut" si indexul 2 ii face loc se duce in dreapta


# my_list = [1,2,3]
# my_list2 = [4,5,6]
# my_list.extend(my_list2)
# print(my_list)


# my_list = ["apple", "banana", "cherry"]
# my_list.pop(1)                             #pop sterge elementul dupa index
# print(my_list)


# my_list = [1,2,3,4,5,6,7,8]
#
# print(my_list)
# a = my_list.pop(5)
# print(a)
# print(my_list)
# my_list.clear()
# print(my_list)


# a = [1,2,3]
# b = a.copy()         #face o copie si noi ori de cate ori modificam a ,b-ul ramane la fel
# print(a)
# print(b)
# b = list(a)          # copy si list fac acelasi lucru


# fruits = ["apple", "banana", "cherry"]
# # print(fruits[2])
# #fruits.remove("banana")
# #fruits.insert(1, "kiwi")
# fruits[1] = "kiwi"
#
# fruits.remove("kiwi")
# fruits_2 = ["mar", "cireasa"]
# fruits.extend(fruits_2)
# print(fruits)


                                         # Hommework

