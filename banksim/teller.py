#
# `teller.py`
# A bank teller class used to serve users from a queue.
# 
# Written by Joshua Paul A. Chan


from employee import Employee

class Teller(Employee):
    """
    `Teller`
    A Teller class used to serve customers. Inherits from Employee
    
    # inherited from Employee
    @attr   : employeed_id  : str
    @attr   : name          : str
    @attr   : salary        : str
    @attr   : available     : bool
    
    @method : is_available  : bool
    @method : set_available : none
    @method : serve         : bool
    
    # overrided/defined in-class
    @method : __str__       : str   : returns a string representation of the
    Teller instance
    @method : __repr__      : str   : returns a string representation of the
    Teller instance (wraps __str__)
    """
    
    def __init__(self, name, salary=None):
        """
        `Teller(name, salary)`
        Constructs a new Teller instance from the Teller class. Inherits
        directly from Employee's constructor
        
        @param  : self      : the Employee object to operate upon
        @param  : name      : the name to give the employee
        @param  : salary    : the salary of the employee [default '9600.00']
        @return : none 
        """
        super().__init__(name, salary)
    
    def __str__(self):
        """
        `__str__`
        Represent a teller as a string
        
        @pre    : the given Teller must be initialized
        @post   : the Teller's is_available attribute will be changed to av
        
        @param  : self  : the Teller object to operate upon
        @return : str   : a string representation of the teller, including
        employee id and name
        """
        return "<Teller id='{}' name='{}' />".format(self.employee_id, self.name)
    
    def __repr__(self):
        """
        `__repr__`
        Represent a teller as a string (wraps self.__str__)
        
        @pre    : the given Teller must be initialized
        @post   : the Teller's is_available attribute will be changed to av
        
        @param  : self  : the Teller object to operate upon
        @return : str   : a string representation of the teller, including
        teller id and name
        """
        return str(self)
        
def main():
    # Quick Unit test
    t = Teller('John Jacob')
    
    # 1. Inheritance
    # case: 
    # it should inherit is_available(), set_available() and serve()
    assert callable(t.is_available) == True
    assert callable(t.set_available) == True
    assert callable(t.serve) == True
    
    # 2. Definitions
    assert type(str(t)) == str

if __name__ == '__main__':
    main()
