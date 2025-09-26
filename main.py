# main.py
from calculator import add, subtract, multiply, divide
from advanced import sqrt, power, percentage

def main():
    print("Team Calculator (type 'exit' to quit)")
    while True:
        op = input("Operation [add, sub, mul, div, sqrt, pow, pct]: ").strip()
        if op == "exit":
            break
        try:
            if op in ("add","sub","mul","div","pow","pct"):
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
            if op == "add":
                print("=", add(a,b))
            elif op == "sub":
                print("=", subtract(a,b))
            elif op == "mul":
                print("=", multiply(a,b))
            elif op == "div":
                print("=", divide(a,b))
            elif op == "pow":
                print("=", power(a,b))
            elif op == "pct":
                print(f"={percentage(a,b)}%")
            elif op == "sqrt":
                x = float(input("Enter number: "))
                print("=", sqrt(x))
            else:
                print("Unknown op.")
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
