class Test:
    def __init__(self,arg1,arg2):
        self.arg1 = arg1
        self.arg2 = arg2
    def print_value(self):
        print(self.arg1,self.arg2)

if __name__ == "__main__":
    obj = Test('Manko','Tinpo')
    obj.print_value()
    obj.newarg = 'Sex'
    print(obj.newarg)
