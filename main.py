# 
# main.py
# Bank simulator
# 
# Written by Joshua Paul A. Chan

import argparse

from banksim.customer import Customer
from banksim.bank import Bank

# set up argument parsing
parser = argparse.ArgumentParser()
parser.add_argument("c", type=int, help="the number of customers to visit the \
bank")
parser.add_argument("-t", type=int, default=1, help="the number of tellers at \
the bank")
parser.add_argument("-v", "--verbose", help="increase the level of output \
logging", action="store_true")

def distribute(items, ticks):
    """
    `distribute(items, ticks)`
    Groups the items over the specified number of ticks so that they're evenly
    distributed
    
    @param  : items : items to group together into buckets
    @param  : ticks : the number of groups/buckets to group items into
    @return : list  : a list of lists, with some items grouped into each
    individual list
    """
    assert type(items) == list
    
    assert type(ticks) == int
    assert ticks > 0
    
    buckets = []
    chunk = []
    
    for i, item in enumerate(items):
        chunk.append(item)
        if ticks % (i + 1) == 0:
            buckets.append(chunk)
            chunk = []
    buckets.append(chunk)
    
    return buckets

def main():
    args = parser.parse_args()
    
    def log(s):
        print(s) if args.verbose
    
    N = args.c
    n_tellers = args.t
    
    # instantiate the bank
    bank = Bank(n_tellers)
    
    # set up simulation
    bank.open()
    t = 0
    wait_time = 0
    
    visitors_over_time = distribute(
        [Customer(str(n).zfill(3)) for n in range(N)],
        N
    )
    
    while bank.is_open():
        log("=" * 32 + " timestep: {} ".format(str(t).zfill(4)) + "=" * 32)
        
        # get new customers
        if t < len(visitors_over_time):
            visitors = visitors_over_time[t]
            for visitor in visitors:
                bank.receive_customer(visitor)
            log("[visitors that came in] {}".format(len(visitors)))
        
        # update internal bank state
        bank.update()
        
        # get available tellers
        available_tellers = list(
            filter(lambda t: t.is_available(), bank.tellers)
        )
        
        while len(available_tellers) > 0 and len(bank.customers) > 0:
            # get teller
            free_teller = available_tellers.pop(0)
            
            # move a customer from queue to available teller
            next_customer = bank.customers.get_next_customer()
            
            free_teller.serve(next_customer)
            
            wait_time += next_customer.has_waited
            # print("{} is serving: {}".format(free_teller, next_customer))
        log("[visitors left to serve] {}".format(len(bank.customers)))
        
        # increment time step
        t += 1
        
        # if no more customers visiting, break
        if t >= len(visitors_over_time) - 1 and len(bank.customers) == 0:
            bank.close()
        
    
    print("=" * 80)
    print("[stats]")
    print("total number of tellers          = {}".format(n_tellers))
    print("total number of customers served = {}".format(N))
    print("total number of unit time steps  = {}".format(t - 1))
    print("average wait time per customer   = {}".format(wait_time / N))
    print("=" * 80)
    
if __name__ == '__main__':
    main()
        
