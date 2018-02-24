IP = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

IP_inverse = [40, 8, 48, 16, 56, 24, 64, 32,
			  39, 7, 47, 15, 55, 23, 63, 31,
			  38, 6, 46, 14, 54, 22, 62, 30,
			  37, 5, 45, 13, 53, 21, 61, 29,
			  36, 4, 44, 12, 52, 20, 60, 28,
			  35, 3, 43, 11, 51, 19, 59, 27,
			  34, 2, 42, 10, 50, 18, 58, 26,
			  33, 1, 41, 9, 49, 17, 57, 25]

initialKeyPermutation = [57, 49, 41, 33, 25, 17, 9,
					       1, 58, 50, 42, 34, 26, 18,
					       10, 2, 59, 51, 43, 35, 27,
					       19, 11, 3, 60, 52, 44, 36,
					       63, 55, 47, 39, 31, 23, 15,
					       7, 62, 54, 46, 38, 30, 22,
					       14, 6, 61, 53, 45, 37, 29,
					       21, 13, 5, 28, 20, 12, 4]

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

ExpansionTable = [32, 1, 2, 3, 4, 5,
                  4, 5, 6, 7, 8, 9,
                  8, 9, 10, 11, 12, 13,
                  12, 13, 14, 15, 16, 17,
                  16, 17, 18, 19, 20, 21,
                  20, 21, 22, 23, 24, 25,
                  24, 25, 26, 27, 28, 29,
                  28, 29, 30, 31, 32, 1]

fdashPermutationTable = [16, 7, 20, 21, 29, 12, 28, 17,
                         1, 15, 23, 26, 5, 18, 31, 10,
                         2, 8, 24, 14, 32, 27, 3, 9,
                         19, 13, 30, 6, 22, 11, 4, 25]

rotation_steps = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

key_choice = [14, 17, 11, 24, 1, 5, 3, 28,
              15, 6, 21, 10, 23, 19, 12, 4,
              26, 8, 16, 7, 27, 20, 13, 2,
              41, 52, 31, 37, 47, 55, 30, 40,
              51, 45, 33, 48, 44, 49, 39, 56,
              34, 53, 46, 42, 50, 36, 29, 32]

def textToBinVector(string):
    unicode = ""
    for x in string:
        unicode = unicode + toBinary(ord(x), 8)
    input = []
    for x in unicode:
        input.append(int(x))
    return input

def keyFromHexToBinVector(my_hexdata,num_of_bits):
    scale = 16  ## equals to hexadecimal
    keyBin = bin(int(my_hexdata, scale))[2:].zfill(num_of_bits)
    key=[]
    for y in keyBin:
        key.append(int(y))
    return key

def fromBinVectorToHex(input):
    x = ""
    for y in input:
        x = x + str(y)
    result = hex(int(x, 2))
    return result[2:]


def split(s, n):#this method splits a list s into sublists each have n elements
    return [s[k:k+n] for k in range(0, len(s), n)]

def toBinary(val, bitsize): #converts val(decimal) to bin in string(no. of bits is bitsize)
    binval = bin(val)[2:] if isinstance(val, int) else bin(ord(val))[2:]
    #ord return the numerical value for a char in decimal
    if len(binval) > bitsize:
        raise ("binary value is larger than bitsize required")
    while len(binval) < bitsize:
        binval = "0"+binval #Add as many 0 as needed to get the wanted size
    return binval

def expand_bits(vector,table):#vector is the input data and the table is
    return [vector[x-1] for x in table]#the expansion table

def permute(vector,table):
    return [vector[x-1] for x in table]

def xor(p1, p2):
    return [x ^ y for x, y in zip(p1, p2)]

def rotate_left (inputToRotate, n):
	return inputToRotate[n:] + inputToRotate [:n]


def swap_left_right(input):
	L,R = split(input,32)
	return R+L

class DES():

    def __init__(self,inputData, key): #input data64bits,key64bits
        self.keys = []
        self.result=[]
        self.generate_keys(key)
        ciphered_message = []
        inputBlocks = split(inputData,64)
        nOfInputs = inputBlocks.__len__()
        lastBlockLength=(inputBlocks[nOfInputs-1]).__len__()
        if((lastBlockLength)==64):
            inputBlocks.append(keyFromHexToBinVector("8",64))
            nOfInputs=nOfInputs+1
        else:
            remaining=64-lastBlockLength
            bytes=int(remaining/8)
            padding=remaining-8
            inputBlocks[nOfInputs-1]=inputBlocks[nOfInputs-1]+[0]*padding
            inputBlocks[nOfInputs-1]=inputBlocks[nOfInputs-1]+keyFromHexToBinVector(str(bytes),8)

        for inputs in range(nOfInputs):
            temp = self.rep(inputBlocks[inputs])
            self.result=self.result+temp

    def rep(self,vector):
        outputFromIP = permute(vector, IP)
        input = outputFromIP
        for i in range(16):
            L_n, R_n = split(input, 32)
            R_n_dash = self.fDash(R_n, self.keys[i])
            R_n1 = xor(L_n,R_n_dash)
            ciphered_message = R_n + R_n1
            input = ciphered_message
        ciphered_message = swap_left_right(ciphered_message)
        return permute(ciphered_message,IP_inverse)

    def getResult(self):
        return self.result

    def generate_keys(self,initial_key):
        key_prime = permute(initial_key, initialKeyPermutation)
        C_node, D_node = split(key_prime, 28)  # split key to two parts
        for i in range(16):
            C_one = rotate_left(C_node, rotation_steps[i])
            D_one = rotate_left(D_node, rotation_steps[i])
            combination = C_one + D_one
            key_one = permute(combination, key_choice)  # this one decreases the vector
            self.keys.append(key_one)
            C_node = C_one
            D_node = D_one

    def fDash(self,inputData,key):
        expandOutput = expand_bits(inputData, ExpansionTable)
        xorOutput = xor(expandOutput, key)
        combineOutput = self.substitute(xorOutput)
        result = permute(combineOutput, fdashPermutationTable)
        return result



    def substitute(self, list48):
        Bs = split(list48, 6)  #splitting the 48 bit vector into 8 sublists
        combinedList = list()
        for i in range(len(Bs)):  # For all the sublists
            block = Bs[i]
            row = int(str(block[0]) + str(block[5]), 2)
            column = int(''.join([str(x) for x in block[1:][:-1]]), 2)
            val = S_boxes[i][row][column]
            bin = toBinary(val, 4)  # Convert the value to binary
            combinedList += [int(x) for x in bin]  # And append it to the resulting list
        return combinedList


string = "Hello world"
input = textToBinVector(string)
key = keyFromHexToBinVector("7365637265745f6b",64)
#print(key)
new = DES(input,key)
print(fromBinVectorToHex(new.getResult()))
print("6DE7F39F4094F3D81C6AAAF8A883086D")
print("6DE7F39F4094F3D8051E2019B13FF797")