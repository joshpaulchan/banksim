# 
# main.py
# Bank simulator
# 
# Written by Joshua Paul A. Chan

import argparse
import math

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
    
    i = 0
    items_per_bucket = math.ceil(len(items) / ticks)
    buckets = [ [] for _ in range(ticks) ]
    
    for j, item in enumerate(items):
        if j % items_per_bucket == 0:
            bucket = buckets[i]
            i += 1
        bucket.append(item)
    
    return buckets

def main():
    args = parser.parse_args()
    
    def log(s):
        if args.verbose: print(s) 
    
    N = args.c if args.c > 0 else 1
    n_tellers = args.t if args.t > 0 else 1
    
    # instantiate the bank
    bank = Bank(n_tellers)
    
    # set up simulation
    bank.open()
    t = 0
    wait_time = 0
    
    visitors_over_time = distribute(
        [Customer(str(n).zfill(3)) for n in range(N)],
        n_tellers
    )
    
    while bank.is_open():
        log("=" * 32 + " timestep: {} ".format(str(t).zfill(4)) + "=" * 32)
            
        # update waiting times
        for customer in bank.customers:
            customer.wait_a_little()
        
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
        
