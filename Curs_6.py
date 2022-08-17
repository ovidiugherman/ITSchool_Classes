                                                        # Exercitii

     # Retrieve from the user using the input() method 5 numbers and print the average

# counter = 0
# sum_total = 0
# while counter < 5:
#     user_number = int(input())
#     sum_total += user_number
#     counter +=1
# print(sum_total)
# print(f'Average {sum_total/5}')
#


    #Printing the items in a tuple using while loop


# cars = ("bmw",'mercedes','mazda','dacia','audi' )
# items = 0
# while items < len(cars):
#     print(cars[items])
#     items += 1
#


     # Write a program that will tell if a dictionary is empty or not

# dict = {}
# if len(dict) == 0:
#     print('GOL')
# else:
#     print('Nu este gol')


      #The user will input 5 numbers (one at a time)  print the min and the max values

# min_num = max_num = float(input("introduceti primul nr: "))
# i = 1
# while i < 5:
#     number = float(input(f"Introduceti nr {i+1}: "))
#     if number < min_num:
#         min_num = number
#     elif number > max_num:
#         max_num = number
#     i += 1
#
# print(f"Max {max_num}")
# print(f"Min {min_num}")
#



      # Finding the sum of numbers in a list using while loop



# my_list = [1,5,2,3,6,7,4]
#
# sum_nunumere = 0
# i = 0
# while i < len(my_list):
#     sum_nunumere = sum_nunumere + my_list[i]
#     i += 1
#
# print(sum_nunumere)
#



 # Number guessing game, we want to create a game where the user needs to guess the number the computer is thinking of.


# import random
#
# start_no = 1
# end_no = 10
# chosen_number = random.randint(start_no, end_no)
#
# print(f'Ghiceste un numar intre {start_no} si {end_no}')
#
# while True:
#
#     my_number = int(input())
#     if my_number > chosen_number:
#         print("Go lower!")
#     elif my_number < chosen_number:
#         print("Go higher!")
#     else:
#         print("You guessed it!")
#         break
#



# import random
#
# start_no = 1
# end_no = 10
# chosen_number = random.randint(start_no, end_no)
# incercari = 3
# counter = 0
#
# print(f'Ghiceste un numar intre {start_no} si {end_no}')
# print(f"Ai {incercari} incercari ")
#
# while counter < incercari:
#
#     my_number = int(input())
#     if my_number > chosen_number:
#         print("Go lower!")
#     elif my_number < chosen_number:
#         print("Go higher!")
#     else:
#         print("You guessed it!")
#
#     counter += 1
#
# print(f"The correct answer {chosen_number}")
#






                                                    # For Loops


# my_dict = {
#     "a": 1,
#     "b": 2,
#     "c": 3,
# }
#
# for item in my_dict.items():
#     print(item)


#my_list = [1,2,3,4,5,6,7,8,9,10]
#
# # for element in my_list:
# #     if element % 2 == 0:
# #         print(element)
#
#
#for i in range(0,len(my_list)):
   #if my_list[i] % 2 == 0:
   #    print(my_list[i])

