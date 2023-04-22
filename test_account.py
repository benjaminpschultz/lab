import pytest
from account import *

class Test:
    def setup_method(self):
        self.p1 = Account('Jimmothy')
        
    def teardown_method(self):
        del self.p1
    
    def test_init(self):
        assert self.p1.get_name() == 'Jimmothy'
        assert self.p1.get_balance() == 0
    
    def test_deposit(self):
        assert self.p1.deposit(37) == True
        assert self.p1.deposit(0) == False
        assert self.p1.deposit(-12) == False
        
    def test_withdraw(self):
        self.p1.deposit(26)
        assert self.p1.withdraw(0) == False
        assert self.p1.withdraw(-14) == False
        assert self.p1.withdraw(27) == False
        assert self.p1.withdraw(26) == True
        assert self.p1.withdraw(15) == True
