# Bytes - immutable sequence of bytes

#bytes literals
bytes1 = b'Python3'
bytes2 = b"Python3"

print(bytes1)
print(bytes2)

str1 = "Sample text to encode"
data = str1.encode('utf-8')
val = data.decode('utf-8')

print(str1)
print(data)
print(val)
print(val == str1)

# Testing
