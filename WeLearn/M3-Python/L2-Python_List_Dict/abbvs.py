# labeled_states = ['NY: New York', 'CA: California', 'TX: Texas']
# print(labeled_states[1])
# states = ['New York', 'California', 'Texas']
# abbs = ['NY', 'CA', 'TX']
# print(abbvs[1] + "is short for" + states[1])

states = {"NY": "New York", "CA": "California", "TX": "Texas", "DE": "Delaware"}
states = {
    "NY": "New York",
    "CA": "California",
    "TX": "Texas",
    "DE": "Delaware"
}

for abbreviation in states:
    print(abbreviation + " is short for " + states[abbreviation])
