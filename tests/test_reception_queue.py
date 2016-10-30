"""
`test_reception_queue.py`
Unit tests for the ReceptionQueue class

Written by Joshua Paul A. Chan
"""

import pytest
import sys, os

# Fix paths (thanks, @aruisdante)
# [http://stackoverflow.com/questions/24868733/how-to-access-a-module-from-outside-your-file-folder-in-python]
sys.path.append(os.path.abspath(os.path.join('.')))

from banksim.customer import Customer
from banksim.reception_queue import ReceptionQueue as rq

class TestReceptionQueue:
    
    def test_initialization(self):
        """
        `test_initialization()`
        Tests that the ReceptionQueue has the attributes and methods defined in
        the class design
        """
        q = rq()
        
        # [ case : customer list must exist ]
        assert hasattr(q, 'customers')
        assert type(q.customers) == list
        
        # [ case : insert_customer must be defined ]
        assert hasattr(q, 'insert_customer')
        assert callable(q.insert_customer)
        
        # [ case : get_next_customer must be defined ]
        assert hasattr(q, 'get_next_customer')
        assert callable(q.get_next_customer)
    
    def test_meta_functions(self):
        """
        `test_meta_functions()`
        Tests that the the length and string of the ReceptionQueue can be found
        via python standard practice
        """
        q = rq()
        
        # [ case : must be able to take the length of queue ]
        assert hasattr(q, '__len__')
        
        # [ case : must have a string representation ]
        assert hasattr(q, '__str__') and hasattr(q, '__repr__')

class TestReceptionQueueInsertCustomer:
    
    def test_initial_length(self):
        """
        `test_initial_length()`
        Test that the initial length of the queue is 0.
        """
        assert len(rq()) == 0
    
    def test_can_insert(self):
        """
        `test_can_insert()`
        Tests that you can insert only Customers
        """
        q = rq()
        
        # [ case : expect error to throw when not inserting Customer ]
        for test_val in [13, 1.0, True, 'hello', []]:
            with pytest.raises(AssertionError):
                q.insert_customer(test_val)
        
        # [ case : allow insert of Customer]
        c = Customer('123')
        old_len = len(q)
        q.insert_customer(c)
        assert len(q) == old_len + 1
        assert c in q.customers

class TestReceptionQueueRetrieveCustomer:

    def test_can_get_next_customer(self):
        """
        `test_can_get_next_customer()`
        Tests that you can retrieve Customers
        """
        q = rq()
        
        # [ case : expect error getting a customer from empty queue ]
        with pytest.raises(IndexError):
            q.get_next_customer()
        
        # [ case : retrieving a customer removes it from the queue ]
        c = Customer('123')
        old_len = len(q)
        q.insert_customer(c)
        assert len(q) == old_len + 1
        assert c in q.customers
        
        b = q.get_next_customer()
        assert b == c
        assert len(q) == old_len
        
