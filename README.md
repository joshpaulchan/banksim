# Programming Methodology II | Project 1
Joshua Chan | 1490009699 | jpc256

[![CircleCI](https://circleci.com/gh/joshpaulchan/banksim.svg?style=svg)](https://circleci.com/gh/joshpaulchan/banksim)

We discussed the decision faced by a Bank Manager on whether to hire additional
teller(s) to supplement the existing single teller, so as to provide better
service to customers (she wants to know how better the service will be given the
additional cost). Impressed by PM-II students of year's past, she has decided to
hire you to help her make this decision. Your project is to:

i. Formulate the problem precisely and define the use case. Use UML to identify
user scenarios, interaction/sequence diagrams, class diagrams etc to analyze and
design a solution to the problem. [2 points]

ii. Implement a simulation that will mimic the arrival of customers, service by
the Teller and successful departure of a customer. Your simulation MUST be able
to handle more than 1 teller, different service and arrival times of customers.
[4 points]

iii. Assume 10 customers arrive every minute for 10 minutes. Assume each service
time is of duration 1 unit. What is the average wait time for the 100 customers
when there is (1) 1 Teller, (ii) 2 Tellers, (iii) 10 Tellers? [1 point]

iv. Design and implement unit tests, integration, system and acceptance tests
for your project. [3 points]

Discussion: You will need to identify the different events in the system. Your
simulation should be able to identify the time of different events in the
system, as well as the time that a customer is waiting to be served, the time
duration for which a customer is being served etc. 

iv. [Extra credit 2 points] Use a continuous integration (CI) capability like
Jenkins (or any other CI) and make them accessible as a webpage. 

## I. Formulate and transcribe problem and use case(s).

The prompt is: "We discussed the decision faced by a Bank Manager on whether to
hire additional teller(s) to supplement the existing single teller, so as to
provide better service to customers (she wants to know how better the service
will be given the additional cost):"

What this is really saying is:
1. Build a system that simulates in-person bank teller(s) and account holder(s)
interactions.
1. Measure the effectiveness of varying the number of tellers with respect to
different loads of customers.
1. Use-case: The client (the Bank Manager) can use this system to gain critical
insight into potential customer scenarios and use that insight to make key
staffing decisions.

To build such a system, we will need to do a few things, mainly:

* Define the capabilities of a teller
* Define the scenarios/interactions a customer might produce
* Define a "reception orders" that determines when which customers will be
  served
  
### Features

* random entry in x-min time span
* [optional] random (discrete) service time
* avg. wait time
* salary cost

In this system, we will be assuming these following things about our object
models from the get-go, but will tweak these assumptions during the simulation.

### Models

A **customer** can:
* open a bank account
* close a bank account
* deposit money
* withdraw money

and has:
* ids
* purpose for visit
* served

A **bank teller** can:
* service a customer
* call a manager

and has:
* currently servicing customer
* employee_ids

and we ***assume*** that servicing a user only takes **one time unit**

A **manager** can:
* override the current "reception order"
* service a user

A **"reception queue"** has:
* the customers waiting to be serviced

and determines:
* who gets serviced next

A **bank** can:
* Put people into the queue

and serves as the "container" or "scene" for our simulation

### Interaction Diagrams

actor user;
line  
actor -> bank

### Program Design

#### Main Event Loop

This is the general flow of how bank teller servicing will be accomplished - at
each step, 

```python
# queue : Queue : The reception order - the customers waiting to be serviced
# tellers : Tellers[] : List of teller objects

while (bank is open):
  
  # Make sure all tellers that were servicing people are done
  tellers_available = update_tellers()
  
  # While tellers can service people, match them up
  while tellers_available > 0:
    # get first available teller
    teller = get_first_available_teller()
  
    # remove user from queue
    user = queue.pop()
    
    # start servicing the user
    teller.service(user)
    
    # teller goes unavailable
    tellers_available -= 1

```

#### Main Async/Interrupt-like customer addition

This shows how users actually end up added to the bank's queue.

```python

user.visit(bank)
# this line adds the user to the bank's queue, to be serviced by a teller.

```

<small><strong>Note:</strong> Interestingly enough, The design of this simulation is similar to that of a flip-flop and clock guided electronic system</small>


## II. Write a program that simulates the arrival of 1 customer and a successful departure.


## Installation

```bash
$ pip install -r requirements.txt
```

## Running the project

```bash
# first you need to load the virtual environment into the shell
$ source venv/bin/activate
# then you can run the program
$ python main.py
# once you're done running it, exit the virtual environment
$ deactivate
```

## Testing the project

```bash
# first you need to load the virtual environment into the shell
$ source venv/bin/activate
# then you can run the program
$ pytest
# once you're done running it, exit the virtual environment
$ deactivate
```
