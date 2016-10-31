#
# `teller.py`
# A bank teller class used to serve users from a queue.
# 
# Written by Joshua Paul A. Chan

from uuid import uuid4 as gen_id

class Customer(object):
    """
    `Customer`
    A Customer class used to serve customers. Inherits from Customer
    
    # overrided/defined in-class
    @attr   : customer_id   : str   : the unique customer id 
    @attr   : name          : str   : the user-friendly name of the Customer
    object
    @attr   : visit_purpose : str   : indicates the user's purpose for visiting
    @attr   : served        : bool  : indicates whether the user was served or
    not
    
    @method : was_served    : bool  : checks whether this Customer has been served or not
    @method : serve         : None  : marks this Customer as having been served
    
    @method : __str__       : str   : returns a string representation of the
    Customer instance
    @method : __repr__      : str   : returns a string representation of the
    Customer instance (wraps __str__)
    """
    
    def __init__(self, name, visit_purpose='other'):
        """
        `Customer(name, salary)`
        Constructs a new Customer instance from the Customer class. Inherits
        directly from Customer's constructor
        
        @pre    : the name must be between 3-64 UTF-8 encoded characters
        
        @param  : self          : Customer  : the Customer object to operate
        upon
        @param  : name          : str       : the name to give the customer
        @param  : visit_purpose : str       : the customer's purpose for visiting [default 'other']
        @return : none 
        """
        assert len(name) >= 3
        
        self.customer_id = gen_id()
        self.name = name[:64]
        self.visit_purpose = visit_purpose
        self.served = False
        self.has_waited = 0
    
    def was_served(self):
        """
        `was_served()`
        Checks whether this Customer has been served or not
        
        @pre    : the given Customer object must be initialized
        @post   : a boolean indicating whether this particular Customer object
        has been served or not will be returned
        
        @param  : self  : Customer  : the customer object to operate upon
        @return : bool  : whether this particular Customer object has been
        served or not will be returned
        """
        return self.served == True
    
    def serve(self):
        """
        `serve()`
        Marks this Customer as having been served
        
        @pre    : the given Customer object must be initialized
        @pre    : the given Customer object must not have been served before
        this operation takes place (.was_served() should return False)
        @post   : the Customer's served attribute will be changed to True
        
        @param  : self  : Customer  : the customer object to operate upon
        @return : bool  : whether this particular Customer object has been
        served or not will be returned
        """
        self.served = True
    
    def wait_a_little(self, td=1):
        """
        `wait_a_little()`
        Increments the time this customer has been waiting
        
        @pre    : the given Customer object must be initialized
        @pre    : the time delta to add should be non-negative
        @post   : the given Customer's waiting time will be incremented by td
        
        @param  : self  : Customer  : the customer object to operate upon
        @param  : td    : int/float : the time delta to add to the customer's 
        waiting time [default 1]
        @return : none
        """
        assert type(td) == int or type(td) == float
        assert td >= 0
        self.has_waited += td
    
    def __str__(self):
        """
        `__str__`
        Represent a customer as a string
        
        @pre    : the given Customer must be initialized
        @post   : the Customer's is_available attribute will be changed to av
        
        @param  : self  : the Customer object to operate upon
        @return : str   : a string representation of the customer, including
        customer id and name
        """
        return "<Customer id='{}' name='{}' served='{}'/>".format(self.customer_id, self.name, self.was_served())
    
    def __repr__(self):
        """
        `__repr__`
        Represent a customer as a string (wraps self.__str__)
        
        @pre    : the given Customer must be initialized
        @post   : the Customer's is_available attribute will be changed to av
        
        @param  : self  : the Customer object to operate upon
        @return : str   : a string representation of the customer, including
        customer id and name
        """
        return str(self)
        
def main():
    pass

if __name__ == '__main__':
    main()
