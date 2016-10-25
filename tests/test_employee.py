"""
`test_employee.py`
Unit tests the employee model

Written by Joshua Paul A. Chan
"""

import pytest
import sys, os

# Fix paths (thanks, @aruisdante)[http://stackoverflow.com/questions/24868733/how-to-access-a-module-from-outside-your-file-folder-in-python]
sys.path.append(os.path.abspath(os.path.join('banksim')))
import employee

class TestEmployee:
    
    def test_name_validation(self):
        """
        `test_name_validation()`
        Tests the pre- and post-conditions of the name attribute
        """
        # [case: invalid name] name must be 3 characters or more
        with pytest.raises(AssertionError):
            employee.Employee('a')
        
        # [case: invalid name] names truncated to be 64 chars 
        e = employee.Employee(''.join([str(i % 9) for i in range(108)]))
        assert hasattr(e, 'name') == True
        assert len(e.name) == 64
    
    def test_uuid_generation(self):
        """
        `test_uuid_generation()`
        Tests the pre- and post-conditions of the uuid attribute
        """
        e = employee.Employee('abcd')
        
        # [case: invalid uuid] test that UUID was generated successfully
        assert hasattr(e, 'employee_id') == True
        
        # [case: non-unique uuid] test that UUID is (usually) unique
        assert e.employee_id != employee.Employee('fijk').employee_id
    
    def test_available(self):
        """
        `test_available()`
        Tests the pre- and post-conditions of the available attribute
        """
        e = employee.Employee('abcd')
        
        # [case: missing `available` attr]
        assert hasattr(e, 'available') == True
        
        # [case: wrong attr `available` type]
        assert type(e.available) == bool
    
    def test_is_available(self):
        """
        `test_is_available()`
        Tests the pre- and post-conditions the funtionality of `is_available`
        """
        e = employee.Employee('abcd')
        
        
        
        
