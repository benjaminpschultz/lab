import pytest
from account import *

class Test:
    def setup_method(self):
        self.p1 = Account('Jimmy')
        
    def teardown_method(self):
        del self.p1
    
    def test_init(self):
        assert self.p1.get_name() == 'Jimmy'
        assert self.p1.get_balance() == 0
    
    def test_deposit(self):
        assert self.p1.deposit(20) == True
        assert self.p1.deposit(0) == False
        assert self.p1.deposit(-2) == False
        
    def test_withdraw(self):
        self.p1.deposit(20)
        assert self.p1.withdraw(0) == False
        assert self.p1.withdraw(-5) == False
        assert self.p1.withdraw(21) == False
        assert self.p1.withdraw(20) == True
        assert self.p1.withdraw(15) == True