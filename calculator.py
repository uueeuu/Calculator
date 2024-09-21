class calculator:
    def err1(self):
        print("error:Enter number") 
        
    def plus(self):
        try:
            x = int(input("first num: "))
            y = int(input("second num: "))
            print(x + y)
        except ValueError:
            self.err1()
                        
    def minus(self):
        try:
            x = int(input("first num: "))
            y = int(input("second num: "))
            print(x - y)
        except ValueError:
            self.err1()
                           
    def div(self):
        try:
            x = int(input("first num: "))
            y = int(input("second num: "))
            print(x / y)
        except ValueError:
            self.err1()
           
    def mul(self):
        try:
            x = int(input("first num: "))
            y = int(input("second num: "))
            print(x * y)
        except ValueError:
            self.err1()