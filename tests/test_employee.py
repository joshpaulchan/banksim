"""
`test_employee.py`
Unit tests the employee model

Written by Joshua Paul A. Chan
"""

import pytest
import sys, os

# Fix paths (thanks, @aruisdante)
# [http://stackoverflow.com/questions/24868733/how-to-access-a-module-from-outside-your-file-folder-in-python]
sys.path.append(os.path.abspath(os.path.join('.')))

from banksim.employee import Employee

class TestEmployee:
    
    def test_name_validation(self):
        """
        `test_name_validation()`
        Tests the pre- and post-conditions of the name attribute
        """
        # [case: invalid name] name must be 3 characters or more
        with pytest.raises(AssertionError):
            Employee('a')
        
        # [case: invalid name] names truncated to be 64 chars 
        e = Employee(''.join([str(i % 9) for i in range(108)]))
        assert hasattr(e, 'name')
        assert len(e.name) == 64
    
    def test_uuid_generation(self):
        """
        `test_uuid_generation()`
        Tests the pre- and post-conditions of the uuid attribute
        """
        e = Employee('abcd')
        
        # [case: invalid uuid] test that UUID was generated successfully
        assert hasattr(e, 'employee_id')
        
        # [case: non-unique uuid] test that UUID is (usually) unique
        assert e.employee_id != Employee('fijk').employee_id
    
    def test_available(self):
        """
        `test_available()`
        Tests the pre- and post-conditions of the available attribute
        """
        e = Employee('abcd')
        
        # [case: missing `available` attr]
        assert hasattr(e, 'available')
        
        # [case: wrong attr `available` type]
        assert type(e.available) == bool
    
    def test_is_available(self):
        """
        `test_is_available()`
        Tests the pre- and post-conditions the funtionality of `is_available`
        """
        e = Employee('abcd')
        
        # [case: missing or un-callable`.is_available` method]
        assert hasattr(e, 'is_available')
        assert callable(e.is_available)
        
        # [case: wrong return type]
        assert type(e.is_available()) == bool
        
        # [case: wrong default return]
        assert e.is_available() == True
        
        # [case: irreflective of internal state]
        e.available = False
        assert e.is_available() == False
    
    def test_set_available(self):
        """
        `test_set_available()`
        Tests the pre- and post-conditions the funtionality of `set_available`
        """
        e = Employee('abcd')
        
        # [case: missing or un-callable`.set_available` method]
        assert hasattr(e, 'set_available')
        assert callable(e.set_available)
        
        # [case: incorrect operation]
        assert e.is_available() != False
        e.set_available(False)
        assert e.is_available() == False
        assert e.available == False
        
        
        
