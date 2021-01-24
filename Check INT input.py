# A function that checks if input is an integer. If not, asks again
def ask_for_int():
    while True:
        try:
            result = int(input("Please provide number: \n"))
        except:
            print("Whoops! That is not a number")
            continue
        else:
            print("Yes thank you")
            break
        finally:
            print("I am going to ask you again! \n")

ask_for_int()