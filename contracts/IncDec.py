import smartpy as sp

@sp.module
def main():
    class IncDec(sp.Contract):
        def __init__(self, initial_count):
                self.data.count = initial_count
        @sp.entrypoint
        def increment(self):
             self.data.count += 1

        @sp.entrypoint
        def decrement(self):
             self.data.count -= 1
        

@sp.add_test()
def test():
    sc = sp.test_scenario("IncDec Test Suite", main)
    c1 = main.IncDec(1)
    sc += c1

    c1.increment()
    sc.verify(c1.data.count == 2)

    c1.decrement()
    sc.verify(c1.data.count == 1)