class Car:      # We create a new class with name Car. 

    def __init__(self, brand, model):     # Initialization (__init__ is a constructor): objects will have two atributes: brand and model. 
        self.brand = brand           # "Self" atribute is a default, refers to the object itSELF. 
        self.model = model
    
    def drive(self):      # Parameter "Self" allowes our method refer to the atributes of certain objects in the class. 
        print(f"{self.brand} {self.model} is driving.")
    
    def stop(self):
        print(f"{self.brand} {self.model} stop driving.")

car1 = Car("Audi", "A3")    # We create a new object car1 using Car class with two atributes: brand and model. 
car1.drive()       # This is how we use functions (methods) we defined for the class, on the objects we created, 
car1.stop()