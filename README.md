# Celsius/Fahrenheit Temperature Converter

This Python program allows you to convert temperatures between Celsius and Fahrenheit. The user interacts through the terminal, choosing the conversion direction and providing the temperature to be converted.

## Features

*   Converts temperatures from Celsius to Fahrenheit.
*   Converts temperatures from Fahrenheit to Celsius.
*   Handles errors for invalid (non-numeric) inputs.
*   Allows the user to perform multiple conversions until they choose to exit.

## How to use

1.  **Clone the repository (optional):** If this code is in a repository (e.g., GitHub), you can clone it to your local machine.

2.  **Save the code:** Save the Python code in a file with the `.py` extension, for example, `temperature_converter.py`.

3.  **Run the program:** Open a terminal or command prompt, navigate to the directory where you saved the file, and run the program using the command:

    ```bash
    python temperature_converter.py
    ```

4.  **Follow the instructions:** The program will display a menu with conversion options. Enter the number corresponding to the desired option and follow the instructions to enter the temperature.

## Example usage
Please, select you option:
[1] if you want to convert Celsius to Fahrenheit
[2] if you want to convert Fahrenheit to Celsius
[3] to turn off the program
Answer: 1
What's the temperature in Celsius?: 25
processing...
The temperature 25.0ºC is the same of 77.0ºF
Do you want make another convertion? [y] or [n]: y
Please, select you option:
[1] if you want to convert Celsius to Fahrenheit
[2] if you want to convert Fahrenheit to Celsius
[3] to turn off the program
Answer: 2
What's the temperature in Fahrenheit?: 68
processing...
The temperature 68.0ºF is the same of 20.0ºC
Do you want make another convertion? [y] or [n]: n
Thank you for using our program :)

## Functions

*   `celsius_fahrenheit(celsius: float)`: Converts a temperature from Celsius to Fahrenheit.
*   `fahrenheit_celsius(fahrenheit: float)`: Converts a temperature from Fahrenheit to Celsius.

## Error handling

The program includes error handling to ensure that the user enters valid numeric values. If a non-numeric input is provided, an error message will be displayed, and the program will prompt the user to enter a correct value.

## Notes

*   The program uses the `sleep(2)` function to simulate processing, adding a 2-second pause before displaying the result.
*   The program continues to run until the user chooses the exit option (3) or answers "n" to the question of whether they want to continue converting.

## Author

Bruno Prates