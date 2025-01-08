import random

'''
---Version Two Notes---
Made it possible to reach the solution to the problem before using all the numbers.
-----------------------
'''


def calculate_equation(num_array, opp_array, result_num):
    renew_array = num_array.copy() 
    curr_num = 0
    correct_answer = False
    equation = ""
    while correct_answer == False:
        # Make sure two random numbers are not the same
        num_1_index = 0
        num_2_index = 0
        number_check = False
        if len(num_array) > 1 and curr_num != result_num:
            while number_check == False or num_1_index == num_2_index:
                
                num_1_index = random.randint(0, (len(num_array) - 1))
                num_2_index = random.randint(0, (len(num_array) - 1))
                num_1 = num_array[num_1_index]
                num_2 = num_array[num_2_index]

                #Perform mathematical operations
                ran_opp = random.choice(opp_array)
                match ran_opp:
                    case "+":
                        number_check = True
                        curr_num = num_1 + num_2
                    case "-":
                        if (num_1 - num_2) < 0:
                            number_check = False
                        else:
                            number_check = True
                            curr_num = num_1 - num_2
                    case "*":
                        number_check = True
                        curr_num = num_1 * num_2
                    case "/":
                        if num_2 == 0:
                            number_check = False
                        elif (num_1 % num_2) > 0:
                            number_check = False
                        else:
                            number_check = True
                            curr_num = num_1 / num_2


            num_array.remove(num_1)
            num_array.remove(num_2)
            num_array.append(curr_num)

            equation = equation + f"({num_1} {ran_opp} {num_2} = {curr_num})"
        
        else:
            equation = equation + f"(Answer = {curr_num})"
            if curr_num == result_num:
                equation = equation + "(Solution Found)"
                correct_answer = True
            else:
                equation = equation + "(No Solution)"
                num_array = renew_array.copy()
                equation = ""
                correct_answer = False

    return equation 

def main(): 
    
    # Testing
    # result_num = 321
    # num_1 = 3
    # num_2 = 9
    # num_3 = 11
    # num_4 = 20
    # num_5 = 22
    # num_6 = 25

    # Retrieving the Data
    result_num = int(input("Result Num: "))
    num_1 = int(input("Num 1: "))
    num_2 = int(input("Num 2: "))
    num_3 = int(input("Num 3: "))
    num_4 = int(input("Num 4: "))
    num_5 = int(input("Num 5: "))
    num_6 = int(input("Num 6: "))

    # Numbers and Operations we will use
    opp_array = ["+", "-", "*", "/"]
    num_array = [num_1, num_2, num_3, num_4, num_5, num_6]
   
    for i in range(50):
        equation = calculate_equation(num_array.copy(), opp_array, result_num)
        print(equation)
        print("\n")

if __name__ == "__main__":
    main()
