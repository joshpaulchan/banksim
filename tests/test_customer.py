"""
`test_customer.py`
Unit tests the customer model

Written by Joshua Paul A. Chan
"""

import pytest
import sys, os

# Fix paths (thanks, @aruisdante)
# [http://stackoverflow.com/questions/24868733/how-to-access-a-module-from-outside-your-file-folder-in-python]
sys.path.append(os.path.abspath(os.path.join('banksim')))

import customer

class TestCustomer:
    
    def test_name_validation(self):
        """
        `test_name_validation()`
        Tests the pre- and post-conditions of the name attribute
        """
        # [case: invalid name] name must be 3 characters or more
        with pytest.raises(AssertionError):
            customer.Customer('a')
        
        # [case: invalid name] names truncated to be 64 chars
        name = ''.join([str(i % 9) for i in range(108)])
        e = customer.Customer(name)
        assert hasattr(e, 'name')
        assert len(e.name) == 64
        assert e.name == name[:64]
        
        # [case: invalid name] names should be directly assigned to .name
        d = customer.Customer('john')
        assert d.name == 'john'
    
    def test_uuid_generation(self):
        """
        `test_uuid_generation()`
        Tests the pre- and post-conditions of the uuid attribute
        """
        e = customer.Customer('abcd')
        
        # [case: invalid uuid] test that UUID was generated successfully
        assert hasattr(e, 'customer_id')
        
        # [case: non-unique uuid] test that UUID is (usually) unique
        assert e.customer_id != customer.Customer('fijk').customer_id
    
    def test_available(self):
        """
        `test_available()`
        Tests the pre- and post-conditions of the available attribute
        """
        e = customer.Customer('abcd')
        
        # [case: missing `available` attr]
        assert hasattr(e, 'available')
        
        # [case: wrong attr `available` type]
        assert type(e.available) == bool
    
    def test_serve(self):
        """
        `test_set_available()`
        Tests the pre- and post-conditions the funtionality of `set_available`
        """
        e = customer.Customer('abcd')
        
        # [case: missing or un-callable`.set_available` method]
        assert hasattr(e, 'set_available')
        assert callable(e.set_available)
        
        # [case: incorrect operation]
        assert e.is_available() != False
        e.set_available(False)
        assert e.is_available() == False
        assert e.available == False
            
        
        