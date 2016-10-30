"""
`test_bank.py`
Tests the Bank class as the bank simulator

Written by Joshua Paul A. Chan
"""

import pytest
import sys, os

# Fix paths (thanks, @aruisdante)
# [http://stackoverflow.com/questions/24868733/how-to-access-a-module-from-outside-your-file-folder-in-python]
sys.path.append(os.path.abspath(os.path.join('.')))

from banksim.teller import Teller
from banksim.customer import Customer
from banksim.teller import Teller
from banksim.reception_queue import ReceptionQueue
from banksim.bank import Bank as bk

class TestBank:
    
    def test_initialization(self):
        """
        `test_initialization()`
        Test the initialization pre and post-conditions of the Bank class
        """
        
        # [ case : bank should be take a non-negative int for n_tellers]
        bk(10)
        bk(1)
        fail_vals = [0, -1, 'a', True] 
        for val in fail_vals:
            with pytest.raises(AssertionError):
                bk(val)
        
        # [ case : n_tellers should default to 1 when unspecified ]
        a = bk()
        assert len(a.tellers) == 1
    
    def test_attrs(self):
        """
        `test_attrs()`
        Tests that the attrs specified in the class design are present
        """
        b = bk()
        
        # [ case : should have a list of at least 1 teller objects ]
        def should_be_teller(t): assert isinstance(t, Teller)
        
        assert hasattr(b, 'tellers')
        assert type(b.tellers) == list
        assert len(b.tellers) >= 1
        map(should_be_teller, b.tellers)
        
        # [ case : should have a reception queue with 0 or some customers ]
        assert hasattr(b, 'customers')
        assert type(b.customers) == ReceptionQueue
        
        # [ case : should have 'operating' attr, False upon initialization ]
        assert hasattr(b, 'operating')
        assert type(b.operating) == bool
        assert b.operating == False
    
    def test_methods(self):
        """
        `test_methods()`
        Tests that the methods specified in the class design are present
        """
        b = bk()
        
        # [ case : should have is_open method that returns bool ]
        assert hasattr(b, 'is_open')
        assert callable(b.is_open)
        assert type(b.is_open()) == bool
        
        # [ case : should have an 'open' method ]
        assert hasattr(b, 'open')
        assert callable(b.open)
        
        # [ case : should have a 'close' method ]
        assert hasattr(b, 'close')
        assert callable(b.close)
        
        # [ case : should have a 'receive_customer' method ]
        assert hasattr(b, 'receive_customer')
        assert callable(b.receive_customer)

class TestBankOpenAndClose:
    
    def test_open_and_close(self):
        """
        `test_open_and_close()`
        Test .open, .is_open and .close functionality
        """
        b = bk()
        c = Customer("Johnny")
        
        # [ case : should not be able to add customers to closed bank ]
        assert b.is_open() == False
        with pytest.raises(Exception):
            b.receive_customer(c)
        
        # [ case : should be able to add only customers to open bank ]
        b.open()
        assert b.is_open() == True
        b.receive_customer(c)
        # [ case : should be able to close bank after opening ]
        assert b.is_open() == True
        b.close()
        with pytest.raises(Exception):
            b.receive_customer(c)

class TestBankReceiveCustomer:
    
    def test_receive_customer(self):
        """
        `test_receive_customer()`
        Tests the pre- and post- conditions of .receive_customer
        """
        b = bk()
        b.open()
        c = Customer("Johnny")
        
        # [ case : should only be able to add customers to banks ]
        b.receive_customer(c)
        fail_vals = [1, 0, 'asdg', False]
        for val in fail_vals:
            with pytest.raises(AssertionError):
                b.receive_customer(val)
