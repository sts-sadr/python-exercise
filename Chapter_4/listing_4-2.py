#!/usr/bin/env python
# -*- coding: utf-8 -*-

print
title = 'Dictionary Method Example'
print title
print len(title) * '-'

# A simple database using get()

people = {
	'Alice': {
		'phone': '2341',
		'addr': 'Foo drive 23'
	},
	'Beth': {
		'phone': '9102',
		'addr': 'Bar street 42'
	},
	'Cecil': {
		'phone': '3158',
		'addr': 'Baz avenue 90'
	}
}

labels = {
    'phone': 'phone number',
    'addr': 'address'
}

name = raw_input('Name: ')

# Are we looking for a phone number or an address?
request = raw_input('Phone number (p) or address (a)? ')

# Use the correct key:
key = request # In case the request is neither 'p' nor 'a'
if request == 'p': key = 'phone'
if request == 'a': key = 'addr'

# Use get to provide default values:
person = people.get(name, {})
label = labels.get(key, key)
result = person.get(key, 'not available')
print "%s's %s is %s." % (name, label, result)