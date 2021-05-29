names = ['nidhi chaubey','prashant pandey','smita srivastava','vaishali dixit','neha singh']

name_containing_e = [name for name in names if 'e' in name]
print(name_containing_e)

name_capitalized = [name.title() for name in names]
print(name_capitalized)

name_endwith_a = [name for name in names if name.endswith('a')]
print(name_endwith_a)