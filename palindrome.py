def ispalindrome(string) :
  leftposition = 0 
  rightposition = len(string) - 1


  while rightposition >= leftposition:  

   if not string[leftposition] == string[rightposition]:  

        return False  

    
   leftposition += 1 
   rightposition -= 1 

  return True  


print("Is this a Palindrome?") 

print(ispalindrome('malayalam'))
