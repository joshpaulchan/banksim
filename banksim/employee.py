"""
`employee.py`
An abstract employee class that contains the basic rudimentary information a
bank employee requires.

Written by Joshua Paul A. Chan
"""

from uuid import uuid4 as gen_id

class Employee(object):
    """
    `Employee`
    An abstract Employee class.
    
    # defined in-class
    @attr   : employee_id   : str   : the unique id of the employee
    @attr   : name          : str   : the user-friendly name of the employee
    @attr   : salary        : str   : a string of the user's yearly salary
    @attr   : available     : bool  : whether the user is available or not 
    
    @method : is_available  : bool  : checks whether or not the employee is
    free to service a customer
    @method : set_available : none  : sets an employee's availability
    @method : serve         : bool  : serve a customer
    @method : __str__       : str   : returns a string representation of the
    Employee instance
    @method : __repr__      : str   : returns a string representation of the
    Employee instance (wraps __str__)
    """
    
    def __init__(self, name, salary=None):
        """
        `Employee(name)`
        Constructs a new Employee instance from the Employee class.
        
        @pre    : name must be a properly-formatted UTF-8 string
        @pre    : name must be a max of 64 characters long and min of 2 chars
        @post   : a fairly unique (see python's uuid.uuid4) id will be generated
        for the employee
        @post   : instantiates a new Employee object with the given name, randomly
        generated id, and available by default
        
        @param  : self      : the Employee object to operate upon
        @param  : name      : the name to give the employee
        @param  : salary    : the salary of the employee [default '9600.00']
        @return : Employee  :
        """
        assert type(name) == str
        assert len(name) >= 2
        assert type(salary) == str or salary == None
        
        self.employee_id = gen_id()
        self.name = name[:64]
        self.available = True
        self.salary = salary or '9600.00' # roughly $10 hr, 20 hrs/wk, 48 wks/yr
    
    def is_available(self):
        """
        `is_available()`
        Checks whether or not the employee is free to service a customer
        
        @pre    : the given Employee must be initialized
        @post   : the Employee will not be modified in any way
        @post   : a boolean result will be returned, indicating whether or not
        an employee is available
                        
        @param  : self  : the Employee object to operate upon
        @return : bool  : whether or not the employee is available
        """
        return self.available == True
    
    def set_available(self, av):
        """
        `set_available(av)`
        Checks whether or not the employee is free to service a customer
        
        @pre    : the given Employee must be initialized
        @pre    : av must be a bool or bool-like object
        @post   : the Employee's is_available attribute will be changed to av
                        
        @param  : self  : the Employee object to operate upon
        @param  : av    : the availability (True or False) of the Employee
        @return : none
        """
        assert type(av) is bool
        self.available = av
    
    def serve(self, cust):
        """
        `serve(av)`
        "Serve" a customer by attempting to resolve his or her purpose for
        visiting
        
        @pre    : the given Employee must be initialized
        @pre    : cust must be a valid Customer object
        @pre    : the employee must be available to service a customer
        @post   : [success] the Employee will be made unavailable and attempt to
        solve the customer's request.
                        
        @param  : self  : the Employee object to operate upon
        @param  : cust  : the customer to "service"
        @return : bool  : whether an employee was successful in servicing the
        given customer  
        """
        print(str(type(cust)))
        # assert str(type(cust)) is 'Customer'
        if not self.is_available(): raise Error("{} is currently busy.".format(self))
        
        # check customer purpose
        purpose = cust.get_purpose()
        can_help_with_purpose = True
        # if applicable, make busy
        
        if can_help_with_purpose: self.set_available(False)
    
    def __str__(self):
        """
        `__str__`
        Represent an employee as a string
        
        @pre    : the given Employee must be initialized
        @post   : the Employee's is_available attribute will be changed to av
        
        @param  : self  : the Employee object to operate upon
        @return : str   : a string representation of the employee, including
        employee id and name
        
        """
        return "<Employee id='{}' name='{}' />".format(self.employee_id, self.name)
    
    def __repr__(self):
        """
        `__str__`
        Represent an employee as a string (wraps self.__str__)
        
        @pre    : the given Employee must be initialized
        @post   : the Employee's is_available attribute will be changed to av
        
        @param  : self  : the Employee object to operate upon
        @return : str   : a string representation of the employee, including
        employee id and name
        
        """
        return str(self)
        
def main():
    pass

if __name__ == '__main__':
    main()
