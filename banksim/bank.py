# 
# `bank.py`
# A bank class that acts as the controller and sandbox for the teller simulation
# 
# Written by Joshua Paul A. Chan

from .customer import Customer
from .teller import Teller
from .reception_queue import ReceptionQueue

class Bank(object):
    """
    `Bank`
    A bank class that acts as the controller and sandbox for a teller
    simulation
    
    # defined in class
    @attr   : tellers   : Teller[]          : List of tellers
    @attr   : customers : ReceptionQueue    : Queue of customers waiting to be
    served
    @attr   : operating : bool              : Whether this bank is open
    (functioning) or not
    
    @method : __init__      : none              : Constructor initiliazing
    function for a Bank instance
    
    @method : _step_        : none    
    @method : is_open       : bool  : Checks whether this bank is open or not
    @method : open          : void  : Opens the bank for business/prepares the
    queue
    @method : close         : void  : Clears the queue and frees the tellers
    """
    
    def __init__(self, n_tellers=1):
        assert type(n_tellers) == int
        assert n_tellers > 0
        
        self.tellers = [Teller(str(i).zfill(3)) for i in range(n_tellers)]
        self.customers = ReceptionQueue()
        self.operating = False
        
    def _step_(self):
        pass
        
    def is_open(self):
        return self.operating == True
    
    def open(self):
        self.operating = True
    
    def close(self):
        self.operating = False
    
    def receive_customer(self, cust):
        assert isinstance(cust, Customer)
        if not self.is_open():
            raise Exception("Cannot visit a bank that is closed.")
        else:
            self.customers.insert_customer(cust)
    
    def __str__(self):
        pass
    
    def __repr__(self):
        pass

def main():
    pass
    

if __name__ == '__main__':
    main()
