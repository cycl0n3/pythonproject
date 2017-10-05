import os

print('-'*20)

print(os.path.abspath('.'))
print(os.path.isabs('.'))
print(os.path.isabs(os.path.abspath('.')))
print(os.getcwd())

print('-'*20)

curl_path = '/usr/bin/curl'
print(os.path.basename(curl_path))
print(os.path.dirname(curl_path))
print(os.path.split(curl_path))
print(curl_path.split(os.path.sep))
print(os.path.getsize(curl_path))
documents_path = '/home/milind/Documents'
print(os.listdir(documents_path))

totalSize = 0
for filename in os.listdir(documents_path):
    totalSize += os.path.getsize(os.path.join(documents_path, filename))
print(totalSize)

print('-'*20)

helloFile = open('hello.txt', 'r')

