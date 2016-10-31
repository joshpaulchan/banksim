"""
`test_customer.py`
Unit tests the customer model

Written by Joshua Paul A. Chan
"""

import pytest
import sys, os

# Fix paths (thanks, @aruisdante)
# [http://stackoverflow.com/questions/24868733/how-to-access-a-module-from-outside-your-file-folder-in-python]
sys.path.append(os.path.abspath(os.path.join('.')))

from banksim.customer import Customer

class TestCustomer:
    
    def test_name_validation(self):
        """
        `test_name_validation()`
        Tests the pre- and post-conditions of the name attribute
        """
        # [case: invalid name] name must be 3 characters or more
        with pytest.raises(AssertionError):
            Customer('a')
        
        # [case: invalid name] names truncated to be 64 chars
        name = ''.join([str(i % 9) for i in range(108)])
        e = Customer(name)
        assert hasattr(e, 'name')
        assert len(e.name) == 64
        assert e.name == name[:64]
        
        # [case: invalid name] names should be directly assigned to .name
        d = Customer('john')
        assert d.name == 'john'
    
    def test_uuid_generation(self):
        """
        `test_uuid_generation()`
        Tests the pre- and post-conditions of the uuid attribute
        """
        e = Customer('abcd')
        
        # [case: invalid uuid] test that UUID was generated successfully
        assert hasattr(e, 'customer_id')
        
        # [case: non-unique uuid] test that UUID is (usually) unique
        assert e.customer_id != Customer('fijk').customer_id
    
    def test_served(self):
        """
        `test_served()`
        Tests the pre- and post-conditions of the served attribute
        """
        e = Customer('abcd')
        
        # [case: missing `served` attr]
        assert hasattr(e, 'served')
        
        # [case: wrong attr `served` type]
        assert type(e.served) == bool
        
        # [case: wrong initival value of `served` attr]
        assert e.served == False
    
    def test_was_served(self):
        """
        `test_was_served()`
        Tests the pre- and post-conditions the funtionality of `was_served`
        """
        e = Customer('abcd')
        
        # [case: missing or un-callable`.was_served` method]
        assert hasattr(e, 'was_served')
        assert callable(e.was_served)
        
        # [case: incorrect operation]
        e.served = True
        assert e.was_served() == True
    
    def test_serve(self):
        """
        `test_serve()`
        Tests the pre- and post-conditions the funtionality of `serve`
        """
        e = Customer('abcd')
        
        # [case: missing or un-callable`.serve` method]
        assert hasattr(e, 'serve')
        assert callable(e.serve)
        
        # [case: incorrect operation]
        assert e.was_served() == False
        e.serve()
        assert e.was_served() and e.served == True
    
    def test_wait_a_little(self):
        """
        `test_wait_a_little()`
        Tests the pre- and post-conditions the funtionality of `wait_a_little`
        """
        e = Customer('abcd')
        
        # [case: missing or un-callable`.wait_a_little` method]
        assert hasattr(e, 'wait_a_little')
        assert callable(e.wait_a_little)
        
        # [case: default waiting value is 1]
        old_time = e.has_waited
        e.wait_a_little()
        assert e.has_waited - 1 == old_time
        
        # [ case : negative numbers are a no-go]
        with pytest.raises(AssertionError):
            e.wait_a_little(-1)
