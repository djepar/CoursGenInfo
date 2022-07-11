"""
One input dict
"""
number = [1,2,3,4,5,6,7,8,9,10,11,12]
oneInputDict = {x:x**2 for x in number}
print(oneInputDict)

"""
Two-input dict
"""


months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]


months_dict = {key:value for (key,value) in zip(number,months)}
print("Using two lists :", months_dict)

"""
Dict dict comprehension
"""

employee_list = [
   {"id": 12345, "name": "John", "department": "Kitchen"},
   {"id": 12456, "name": "Paul", "department": "House Floor"},
   {"id": 12478, "name": "Sarah", "department": "Management"},
   {"id": 12434, "name": "Lisa", "department": "Cold Storage"},
   {"id": 12483, "name": "Ryan", "department": "Inventory Mgmt"},
   {"id": 12419, "name": "Gill", "department": "Cashier"}
]
