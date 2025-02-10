from time import sleep


def celsius_fahrenheit(celsius:float):
    fahrenheit = celsius * 1.8 + 32
    return fahrenheit

def fahrenheit_celsius(fahrenheit:float):
    celsius = (fahrenheit - 32) / 1.8
    return celsius

while True:
    try:
        decision = int(input("Please, select you option:\n"
                         "[1] if you want to convert Celsius to Fahrenheit\n"
                         "[2] if you want to convert Fahrenheit to Celsius\n"
                         "[3] to turn off the program\n"
                         "Answer: "))

    
        if decision == 1:
            temperature = float(input("What's the temperature in Celsius?: "))
            fahrenheit = celsius_fahrenheit(temperature)
            print("processing...")
            sleep(2)
            print(f'The temperature {temperature}ºC is the same of {fahrenheit}ºF')
        
        elif decision == 2:
            temperature = float(input("What's the temperature in Fahrenheit?: "))
            celsius = fahrenheit_celsius(temperature)
            print("processing...")
            sleep(2)
            print(f'The temperature {temperature}ºF is the same of {celsius}ºC')
            
        elif decision == 3:
            print('Thank you for using our program :)')
            break
        else:
            print("Please, select the correct numbers: 1, 2 ou 3")
            sleep(2)
            continue

    except ValueError:
        print("Please, select the correct numbers: 1, 2 ou 3")
        sleep(2)
        continue

    to_continue = input("Do you want make another convertion? [y] or [n]: ").lower()
    if to_continue != "y":
        print('Thank you for using our program :)')
        break
    else:
        continue



