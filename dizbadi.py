class Calculator:
    def __init__(self):
        pass

    def add(self, x, y):
        """Adds two numbers"""
        return x + y

    def subtract(self, x, y):
        """Subtracts y from x"""
        return x - y

    def multiply(self, x, y):
        """Multiplies two numbers"""
        return x * y

    def divide(self, x, y):
        """Divides x by y"""
        if y == 0:
            raise ValueError("Division by zero is not allowed")
        return x / y

def main():
    calc = Calculator()

    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        choice = input("Enter choice (1/2/3/4): ")

        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print("Result:", calc.add(num1, num2))
            elif choice == '2':
                print("Result:", calc.subtract(num1, num2))
            elif choice == '3':
                print("Result:", calc.multiply(num1, num2))
            elif choice == '4':
                try:
                    print("Result:", calc.divide(num1, num2))
                except ValueError as e:
                    print(e)
            break
        else:
            print("Invalid input")

if __name__ == "__main__":
    main()
