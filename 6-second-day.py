class Calculation:
    
    def __init__(self,first_number,second_number): #constructor
        self.first_number = first_number
        self.second_number =second_number
    
    def add(self):
        sum = self.first_number+self.second_number
        print(f"sum of two number is: {sum}")

    def sub(self):
        dif = self.first_number-self.second_number
        print(f"diff of two number is: {dif}")
         
    
    def mul():
        pass
    
    def div():
        pass
    
cal =Calculation(12,15)
cal.add()
cal.sub()