#!/usr/bin/env python3

first = "Ashish"
last = "Kumar"
message = f'{first} [{last}] is a DevOps Architect.'
#message = 'Ashish Kumar is a DevOps Architect.'
print(message)
print(len(message))
print(message.upper())
print(message.lower())
print(message.title())`
print(message.find('A'))
print(message.find('Architect'))
print(message.find('d'))
print(message.replace('Kumar', 'Prajapati'))
print('Ashish' in message)
print('Prajapati' in message)
