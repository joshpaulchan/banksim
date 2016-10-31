# `reception_queue.py`
# A queue-like object that models the waiting line for the bank
# 
# Written by Joshua Paul A. Chan

from .customer import Customer

class ReceptionQueue(object):
    """
    `ReceptionQueue`
    A queue-like object that models the waiting line for the bank
    
    # overrided/defined in-class
    @attr   : customers         : Customer[]   : A non-capped list of customers
    waiting to be served

    @method : insert_customer   : None          : Inserts a customer into the
    waiting line
    @method : get_next_customer : Customer      : Gets the next customer that needs
    to be served
    @method : __str__           : str           : returns a string
    representation of the ReceptionQueue instance
    @method : __repr__          : str           : returns a string
    representation of the ReceptionQueue instance (wraps __str__)
    """
    
    def __init__(self):
        self.customers = []
    
    def insert_customer(self, cust):
        """
        `insert_customer(cust)`
        Inserts a customer into the waiting line
        
        @pre    : Only allow Customer or Customer-like objects to be inserted
        into the queue
        @pre    : The Customer object must not have been served previously
        @post   : [success] The Customer will be inserted into the customer list
        following some criteria (tending towards FIFO behavior)
        @post   : [error] AssertionErrors will be rasied
        
        @param  : self  : ReceptionQueue    : The ReceptionQueue instance to add
        a customer to
        @param  : cust  : Customer          : The Customer or Customer-like
        object to add to the customer list
        """
        assert isinstance(cust, Customer)
        assert not cust.was_served()
        
        # FIFO
        self.customers.append(cust)
    
    def get_next_customer(self):
        """
        `get_next_customer()`
        Get the next customer that needs to be served
        
        @pre    : The ReceptionQueue object must be initialized
        @pre    : The ReceptionQueue object must have customers in it, otherwise
        an IndexError will be raised
        @post   : The Customer object that needs to be serviced will be popped
        from the line
        
        @param  : self      : the ReceptionQueue object to operate upon
        @return : Customer  : the next customer waiting to be served
        """
        # FIFO
        return self.customers.pop(0)
    
    def __iter__(self):
        """
        `__iter__`
        Allow the ReceptionQueue to be iterated upon in a pythonic way
        
        @pre    : The ReceptionQueue object must be initialized
        @post   : A iterable object will be returned
        
        @param  : self  : the ReceptionQueue object to operate upon
        @return : iter  : an iterable view over the ReceptionQueue's customers
        """
        return self.customers.__iter__()    
    
    def __len__(self):
        """
        `__len__`
        Returns the numbers of customers waiting in the queue
        
        @pre    : The ReceptionQueue object must be initialized
        @post   : The number of Customers waiting in the queue will be returned
        
        @param  : self  : the ReceptionQueue object to operate upon
        @return : int   : the number of Customers waiting in the queue
        """
        return len(self.customers)
    
    def __str__(self):
        """
        `__str__`
        Represent a ReceptionQueue as a string
        
        @pre    : the given ReceptionQueue must be initialized
        
        @param  : self  : the ReceptionQueue object to operate upon
        @return : str   : a string representation of the reception queue
        """
        return "<ReceptionQueue>\n{}\n</ReceptionQueue>".format("\n".join(map(lambda c: "    " + str(c), self.customers)))
    
    def __repr__(self):
        """
        `__repr__`
        Represent the items of a ReceptionQueue as a string
        
        @pre    : the given ReceptionQueue must be initialized
        
        @param  : self  : the ReceptionQueue object to operate upon
        @return : str   : a string representation of the items in the reception
        queue, in the format [ Customer.__repr__(), Customer.__repr__(), ... ]
        """
        return str(self)

def main():
    # [ small functionality test ]
    q = ReceptionQueue()
    
    for i in range(1, 10):
        c = Customer(str(i).zfill(3))
        q.insert_customer(c)

    print("length: {}".format(len(q)))
    print("{}".format(q))
    
    c = q.get_next_customer()
    
    print("c: {}".format(c))
    print("length: {}".format(len(q)))
    print("{}".format(q))

if __name__ == '__main__':
    main()
