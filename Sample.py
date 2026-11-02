class Sample:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        if b==0:
            return "Division by zero is not allowed"
        else:
            return a/b
    def remainder(self,a,b):
        return a%b
