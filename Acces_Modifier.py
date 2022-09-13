class Animal:
    def __init__(self, name, age):
        #public data members
        self._name = name
        self._age = age
     # protected method
    def _displayAge(self):
        #accesing protected age attribute
        print("Age: ", self._age)

    def ChangeAge(self, age):
        self.__age = age

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
    #public method
    def printDetails(self):
        #accesing protected attribute from super class
        print("Dog Name: ", self._name)
        super()._displayAge()
    def ChangeDogName(self, name):
        #ok we can change protected attrib child from class
        self._name = name
    def ChangeDogAge(self, newAge):
        self.__age = newAge

obj = Dog("Ghita", 5)

#accesing display age public method
obj.printDetails()
#modify age public attribute
obj.ChangeAge(10)

# _ protected
# __privat poate fi folosit doar in interiorul clasei


