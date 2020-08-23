import string
import random

if __name__ == "__main__":
    s1 = string.ascii_lowercase
    
    s2 = string.ascii_uppercase
   
    s3 = string.digits
    
    s4 = string.punctuation
   
    passlen = int()
    
    print("---------------------------------")
    print("|  Created By iThACK Community  |")
    print("---------------------------------")
    
    try:
        passlen = int(input("Enter Password Length \n==>> "))
        s = []
        s.extend(s1)
        s.extend(s2)
        s.extend(s3)
        s.extend(s4)
       
        random.shuffle(s)
      
        sam = random.sample(s, passlen)
        
        print("\n-----------------------------------------------------------------------------\n")
        print("Your 1th Password : ",("".join(s[0:passlen])))
        print("Your 2nd Password : ",("".join(sam)))
   
    except ValueError:
        print("\nOnly Interger Value Allowed")
        print("Try Again...")
   
    except TypeError:
        print("\nOnly Interger Value Allowed")
        print("Try Again...")
        
    
    
