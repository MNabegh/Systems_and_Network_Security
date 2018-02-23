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
			  37, 5, 45, 13, 33, 21, 61, 29,
			  36, 4, 44, 12, 52, 20, 60, 28,
			  35, 3, 43, 11, 51, 19, 59, 27,
			  34, 2, 42, 10, 50, 18, 58, 26,
			  33, 1, 41, 9, 49, 17, 57, 25]
rotation_steps = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

def permute_and_eliminate (input, table):
	return [input[pos-1] for pos in table]


def split_to_multiple_lists (list, step):
	return [list[k:k+step] for k in range(0, len(list), step)]


def rotate_left (vector, steps):
	return vector[steps:] + vector [:steps] 

def combine(C,D):
	return C + D

def generate_keys(initial_key):
	initial_key = string_to_bit_array (initial_key)
	key_prime = permute_and_eliminate(initial_key, initial_key_permutation)
	C_node, D_node = split_to_multiple_lists(key_prime, 28) # split key to two parts
	for i in range(16):		
		C_one = rotate_left(C_node, rotation_steps[i])
		D_one = rotate_left(D_node, rotation_steps[i])
		combination = combine(C_one,D_one)
		key_one = permute_and_eliminate(combination, key_choice)
		print (bit_array_to_HEX(key_one))
		keys.append(key_one)
		C_node = C_one
		D_node = D_one

def f_encrypt(input):
	for i in range(16):
		L_n, R_n = split_to_multiple_lists(input, 32)
		R_n_dash = f_prime(R_n, keys[i])
		R_n1 = []
		for j in range(32):
			R_n1[j] = L_n[j] ^ R_n_dash[j]
		ciphered_message = combine (R_n, R_n1)
		input = ciphered_message
	return ciphered_message;

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
        raise "binary value larger than the expected size"
    while len(binval) < bitsize:
        binval = "0"+binval #Add as many 0 as needed to get the wanted size
    return binval

def bit_array_to_HEX(val):
    binary_string = ''.join([str(num) for num in val])
    return hex(int(binary_string,2))

generate_keys('secret_k')