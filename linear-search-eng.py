#English version Added

class List:
    
    def __init__(self): 
        # Open the file 'names.txt' in read mode
        with open('nomes.txt', 'r') as self.name_file:
            # Read all lines, strip newlines and store in the list 'names'
            self.names = [n.strip() for n in self.name_file]
        print(self.names)

class Search(List):
    
    def search(self):
        # Prompt the user to input the name they are looking for
        self.value = input('Enter the name to be found: ')
        List.__init__(self)  # Initialize the parent class (List)
        
        # Iterate through the list of names and check if the input value matches
        for self.current_name in self.names:
            if self.value == self.current_name:
                return 'Value found'
        
        return 'Value not found'

# Create an instance of the Search class and invoke the search method
system = Search()
print(system.search())
