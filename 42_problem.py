'''You are given two sets of students who attended two workshops.
python = {"Aman", "Ravi", "Neha", "Pooja"}
ai = {"Neha", "Pooja", "Rahul"}'''
python = {"Aman", "Ravi", "Neha", "Pooja"}
ai = {"Neha", "Pooja", "Rahul"}
# Students who attended both workshops
both=python.intersection(ai)
print(both)

# # Students who attended only Python
only_python=python-ai
print(only_python)

# # Students who attended only AI
only_ai=ai-python
print(only_ai)

# # Students who attended at least one workshop
at_least=python.union(ai)
print(at_least)
