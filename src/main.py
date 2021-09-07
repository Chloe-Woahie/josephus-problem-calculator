import calculator

def main():
    while True:
        soldiers = int(input("Enter amount of soldiers: "))
        survivingPosition = calculator.find_surviving_position(soldiers)
        print("The surviving position is: " + str(survivingPosition))

main()

 
