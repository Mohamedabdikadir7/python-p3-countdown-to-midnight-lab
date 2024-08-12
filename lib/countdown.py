# # your code goes here!
# import time
# def countdown(count):
#     while count >= 1:
#         print(f'{count} SECOND(S)!')
#         count -= 1
#     print ("happy new year")
# def countdown_with_sleep(count):
#     while count >= 1:
#         print(f'{count} SECOND(S)!')
#         time.sleep(1)  # Pause for 1 second
#         count -= 1
#     print("HAPPY NEW YEAR!")

import time

def countdown(number):
    while number >= 1:
        print(f'{number} SECOND(S)!')
        number -= 1
    print("HAPPY NEW YEAR!")

def countdown_with_sleep(number):
    while number >= 1:
        print(f'{number} SECOND(S)!')
        time.sleep(1)  # Pause for 1 second
        number -= 1
    print("HAPPY NEW YEAR!")



 