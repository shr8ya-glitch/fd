input("(n & (n-1)) clears the rightmost bit. Press Enter.")
print("2 & 3",2 &3, "Binary:",bin(2&3)[2:])
print("110 & 111 ",110&111,"Binary:",bin(110&111)[2:])
n=int(input("Enter the number:"))
print("n&(n-1)","Binary:",bin(n&(n-1))[2:])

print("Power of 4:n%3==1. Press Enter.")
print("16 binary:",bin(16)[2:],16%3,"Power of 4")
print("18 binary:",bin(18)[2:],18%3,"Not Power of 4")

print("Power of 8:n%7==1. Press Enter.")
print("16 binary:",bin(64)[2:],64%7,"Power of 8")
print("18 binary:",bin(68)[2:],68%7,"Not Power of 8")

n=int(input("enter number:"))

print("Exponent:2^n",2^n)