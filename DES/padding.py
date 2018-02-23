def string_to_bit_array(text):#Convert a string into a list of bits
    bit_array = list()
    for char in text:
        binval = binvalue(char, 8)#Get the char value on one byte
        bit_array.extend([int(x) for x in list(binval)]) #Add the bits to the final list
    return bit_array

def binvalue(val, bitsize): #Return the binary value as a string of the given size 
    binval = bin(val)[2:] if isinstance(val, int) else bin(ord(val))[2:]
    if len(binval) > bitsize:
        raise "binary value larger than the expected size"
    while len(binval) < bitsize:
        binval = "0"+binval #Add as many 0 as needed to get the wanted size
    return binval

def bit_array_to_HEX(val):
    binary_string = ''.join([str(num) for num in val])
    return hex(int(binary_string,2))

def add_padding(input):
	pad_length = 64 - (len(input) % 64)
	last_byte = '{0:08b}'.format(pad_length)
	padding_array = [0] * (pad_length - 8) + [int(bit) for bit in last_byte]
	print (len(input))
	print (pad_length)
	print (len(padding_array))
	print (bit_array_to_HEX(padding_array[(len(padding_array) - 8):]))	 

text = input("Enter text \n")
bit_array = string_to_bit_array(text)
add_padding(bit_array)