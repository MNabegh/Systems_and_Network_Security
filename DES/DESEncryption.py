IP = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

initial_key_permutation = [57, 49, 41, 33, 25, 17, 9,
					       1, 58, 50, 42, 34, 26, 18,
					       10, 2, 59, 51, 43, 35, 27,
					       19, 11, 3, 60, 52, 44, 36,
					       63, 55, 47, 39, 31, 23, 15,
					       7, 62, 54, 46, 38, 30, 22,
					       14, 6, 61, 53, 45, 37, 29,
					       21, 13, 5, 28, 20, 12, 4]

key_choice = [14, 17, 11, 24, 1, 5, 3, 28,
              15, 6, 21, 10, 23, 19, 12, 4,
              26, 8, 16, 7, 27, 20, 13, 2,
              41, 52, 31, 37, 47, 55, 30, 40,
              51, 45, 33, 48, 44, 49, 39, 56,
              34, 53, 46, 42, 50, 36, 29, 32]

expansion_table =   [32, 1, 2, 3, 4, 5,
					 4, 5, 6, 7, 8, 9,
					 8, 9, 10, 11, 12, 13,
					 12, 13, 14, 15, 16, 17,
					 16, 17, 18, 19, 20, 21,
					 20, 21, 22, 23, 24, 25,
					 24, 25, 26, 27, 28, 29,
					 28, 29, 30, 31, 32, 1]

keys = []
IP_inverse = [40, 8, 48, 16, 56, 24, 64, 32,
			  39, 7, 47, 15, 55, 23, 63, 31,
			  38, 6, 46, 14, 54, 22, 62, 30,
			  37, 5, 45, 13, 53, 21, 61, 29,
			  36, 4, 44, 12, 52, 20, 60, 28,
			  35, 3, 43, 11, 51, 19, 59, 27,
			  34, 2, 42, 10, 50, 18, 58, 26,
			  33, 1, 41, 9, 49, 17, 57, 25]
S_boxes = [

    [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
     [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
     [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
     [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
     ],

    [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
     [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
     [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
     [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
     ],

    [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
     [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
     [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
     [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
     ],

    [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
     [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
     [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
     [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
     ],

    [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
     [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
     [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
     [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
     ],

    [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
     [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
     [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
     [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
     ],

    [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
     [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
     [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
     [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
     ],

    [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
     [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
     [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
     [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
     ]
] #these are the f dash s boxes, from s1 to s8
f_prime_PermutationTable = [16, 7, 20, 21, 29, 12, 28, 17,
                         1, 15, 23, 26, 5, 18, 31, 10,
                         2, 8, 24, 14, 32, 27, 3, 9,
                         19, 13, 30, 6, 22, 11, 4, 25]
rotation_steps = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

def permute_and_eliminate (input, table):
	return [input[pos-1] for pos in table]


def split_to_multiple_lists (list, step):
	return [list[k:k+step] for k in range(0, len(list), step)]


def rotate_left (vector, steps):
	return vector[steps:] + vector [:steps]

def combine(C,D):
	return C + D
def xor(l1, l2):
    return [x ^ y for x, y in zip(l1, l2)]
def swap_left_right(input):
	L,R = split_to_multiple_lists(input,32)
	return combine(R,L)

def string_to_bit_array(text):#Convert a string into a list of bits
    bit_array = list()
    for char in text:
        binval = binvalue(char, 8)#Get the char value on one byte
        bit_array.extend([int(x) for x in list(binval)]) #Add the bits to the final list
    return bit_array

def binvalue(val, bitsize): #Return the binary value as a string of the given size
    binval = bin(val)[2:] if isinstance(val, int) else bin(ord(val))[2:]
    if len(binval) > bitsize:
        raise ("binary value larger than the expected size")
    while len(binval) < bitsize:
        binval = "0"+binval #Add as many 0 as needed to get the wanted size
    return binval

def bit_array_to_HEX(val):
    binary_string = ''.join([str(num) for num in val])
    return hex(int(binary_string,2))

def generate_keys(initial_key):
	initial_key = string_to_bit_array (initial_key)
	key_prime = permute_and_eliminate(initial_key, initial_key_permutation)
	C_node, D_node = split_to_multiple_lists(key_prime, 28) # split key to two parts
	for i in range(16):
		C_one = rotate_left(C_node, rotation_steps[i])
		D_one = rotate_left(D_node, rotation_steps[i])
		combination = combine(C_one,D_one)
		key_one = permute_and_eliminate(combination, key_choice)
		#print (bit_array_to_HEX(key_one))
		keys.append(key_one)
		C_node = C_one
		D_node = D_one

def f_encrypt(input):
	for i in range(16):
		L_n, R_n = split_to_multiple_lists(input, 32)
		R_n_dash = f_prime(R_n, keys[i])
		R_n1 = []
		for j in range(32):
			R_n1.append(L_n[j] ^ R_n_dash[j])
		ciphered_message = combine (R_n, R_n1)
		input = ciphered_message
	return ciphered_message;

def f_prime(inputData,key):
    expandOutput = permute_and_eliminate(inputData, expansion_table)
    xorOutput = xor(expandOutput, key)
    combineOutput = substitute(xorOutput)
    result = permute_and_eliminate(combineOutput,f_prime_PermutationTable)
    return result


def substitute(list48):
    Bs = split_to_multiple_lists(list48, 6)  #splitting the 48 bit vector into 8 sublists
    combinedList = list()
    for i in range(len(Bs)):  # For all the sublists
        block = Bs[i]
        row = int(str(block[0]) + str(block[5]), 2)
        column = int(''.join([str(x) for x in block[1:][:-1]]), 2)
        val = S_boxes[i][row][column]
        bin = binvalue(val, 4)  # Convert the value to binary
        combinedList += [int(x) for x in bin]  # And append it to the resulting list
    return combinedList

#integrating
def DES(input,key):
    inputInBinary= string_to_bit_array(input)
    inputInBinary = add_padding(inputInBinary)
    encrypted = []
    generate_keys(key)
    for i in range(0,len(inputInBinary),64):
        afterIP = permute_and_eliminate(inputInBinary[i:i+64],IP)
        ciphered_message= f_encrypt(afterIP)
        swapped= swap_left_right(ciphered_message)
        encrypted += permute_and_eliminate(swapped,IP_inverse)
    return encrypted

def add_padding(input):
    pad_length = 64 - (len(input) % 64)
    last_byte = '{0:08b}'.format(int(pad_length/8))
    padding_array = [0] * (pad_length - 8) + [int(bit) for bit in last_byte]
    print ()
    return input + padding_array

encrypted = DES("Hello world", "secret_k")
print (bit_array_to_HEX(encrypted)[2:])
print("dfe5fde5da9f5c9d612c1a5f8acdcbc3")
print("DFE5FDE5DA9F5C9D612C1A5F8ACDCBC3")