from calculator import calculator
a = 0
calc = calculator()
class use:
    def main(self):
        uno = input("Действие: ")
        if uno == "+":
            calc.plus()
        elif uno == "-":
            calc.minus()
        elif uno == "/":
            calc.div()
        elif uno == "*":
            calc.mul()
        elif uno.lower() == "exit":
            global a
            a = 10                          
        else:
           print("Error: Нет действия")

while a < 1:
    main = use()
    main.main()     