import os

print('-'*20)

print(os.path.abspath('.'))
print(os.path.isabs('.'))
print(os.path.isabs(os.path.abspath('.')))
print(os.getcwd())
