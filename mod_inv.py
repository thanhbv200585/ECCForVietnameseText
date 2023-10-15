Pcurve = 139 # The proven prime
Acurve = 19 # These two defines the elliptic curve. y^2 = x^3 + Acurve * x + Bcurve
Bcurve = 29
Gx = 1 
Gy = 7
GPoint = (int(Gx),int(Gy)) # This is our generator point.
N=127 # Number of points in the field

# Replace with any private key
privKey = 0x79FE45D61339181238E49424E905446A35497A8ADEA8B7D5241A1E7F2C95A04D

def modinv(a,n=Pcurve): #Extended Euclidean Algorithm/'division' in elliptic curves
    return pow(a, -1, n)

def ECadd(a,b): # EC Addition
    LamAdd = ((b[1]-a[1]) * modinv(b[0]-a[0],Pcurve)) % Pcurve
    x = (LamAdd*LamAdd-a[0]-b[0]) % Pcurve
    y = (LamAdd*(a[0]-x)-a[1]) % Pcurve
    return (x,y)

def ECdouble(a): # EC Doubling
    Lam = ((3*a[0]*a[0]+Acurve) * modinv((2*a[1]),Pcurve)) % Pcurve
    x = (Lam*Lam-2*a[0]) % Pcurve
    y = (Lam*(a[0]-x)-a[1]) % Pcurve
    return (x,y)

def EccMultiply(GenPoint,ScalarHex): # Doubling & Addition
    if ScalarHex == 0 or ScalarHex >= N: raise Exception("Invalid Scalar/Private Key")
    ScalarBin = str(bin(ScalarHex))[2:]
    Q=GenPoint
    for i in range (1, len(ScalarBin)):
        Q=ECdouble(Q); 
        if ScalarBin[i] == "1":
            Q=ECadd(Q,GenPoint)
    return (Q)

# print("******* Bitcoin Public Key Generation *********")

# PublicKey = EccMultiply(GPoint,privKey)
# print("the private key:")
# print(hex(privKey))

# print("the public key x-value (Hex):") 
# print(hex(PublicKey[0]))

# print("the public key y-value (Hex):") 
# print(hex(PublicKey[1]))

# print("the public key (Hex):") 
# print("0x" + "%064x" % PublicKey[0] + "%064x" % PublicKey[1])

for i in range(1, 10):
    print(EccMultiply(GPoint, i))

