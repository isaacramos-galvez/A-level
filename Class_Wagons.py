class Wagon:
    def __init__(self, name, contents):
        self.name = name
        self.contents = contents

    def __str__(self):
        return f"The wagon has details {self.name}, {self.contents}"

class OpenWagon(Wagon):
    def __init__(self):
        super().__init__(self, name, contents)

class ClosedWagon(Wagon):
    def __init__(self):
        super().__init__(self, name, contents)
    
class siding:
    def __init__(self):
        self._top_of_stack_pointer = -1
        self._wagon_array = [none] * 30

    def push_wagon(self, wagon):
        self._top_of_stack_pointer += 1
        self._wagon_array[self._top_of_stack_pointer] = wagon

    def pop_wagon(self):
        wagon_to_remove = self._wagon_array[self._top_of_stack]
        self._top_of_stack_pointer -= 1
        return wagon_to_remove

    def get_siding_details(self):
        return self._wagon_array
        return self._top_of_stack_pointer

class Yard: 
    def __init__(self, number_of_sidings):
        self.number_of_sidings = number_of_sidings
        self.sidings = []
        for i in range(number_of_sidings):
            self.sidings.append(siding())
    



