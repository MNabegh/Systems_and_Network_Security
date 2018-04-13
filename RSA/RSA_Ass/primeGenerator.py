from Crypto.Util import number

n_length = 512
p = number.getPrime(n_length)
q = number.getPrime(n_length)
print ("p = ", p, "\nq = ", q)