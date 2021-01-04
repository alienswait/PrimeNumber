# Prime numbers are divisible only by the number 1 or itself

def primenumber(number):
    if number == 1:
        return False

    elif number ==2:
        return True


    else:
        for i in range(2,number):
            if number % 2 ==0:
                return False
            return True

while True:
    number =  input("number: ")

    if number == "q":
        print("signing out...")
        break

    else:
        number= int(number)
        if primenumber(number):
            print(number,"is the prime number..")

        else:
            print(number,"is not prime numbers..")
