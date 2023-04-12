#!/usr/bin/env python3


'''You are starting up your own event coordination business and want to create a Python application using generators to help manage your events'''

guests = {}


def read_guestlist(file_name):
    with open(file_name) as file:
        for line in file:
            name, age = line.strip().split(",")
            age = int(age)
            yield name, age
            # name, age = yield # to support generator obj. send method
            guests[name] = age


# create the generator object
guestlist = read_guestlist("guest_list.txt")

# iterate over the first 10 guests
for i in range(10):
    name, age = next(guestlist)
    print(name)

# add a new guest
next(guestlist)
guestlist.send("Jane, 35")

# iterate through the generator object using a for loop
for name, age in guestlist:
    print(name)

# iterate over the next 10 guests (including Jane)
#for i in range(10):
#    name, _ = next(guestlist)
#    print(name)

# over 21 generator expression
over_21 = (name for name, age in guests.items() if age >= 21)

# print out over 21 guests
print("Guests aged 21 and over:")
for name, age in over_21:
    print(name, age)

'''
if __name__ == '__main__':
  main()
'''
