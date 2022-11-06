#function to count the vowels in a given string 
def count_vowels(string, dictionary):
    vowels = 'aeiou'

    # converts string to lower case
    string = string.lower()
    
    # Add all the vowels to the dictionary with each vowel a key and initial value 0
    dictionary = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0, }
    
    #loop to count the vowels
    for char in string:
        
      if char in vowels:
          #increment the count by 1.
          dictionary[char] += 1
          
     
    for key in dictionary:
        print(key,":",dictionary[key])


#input from the user.
string = input("Enter the string:")

#empty dictionary.
dictionary = {}

# Calling the function and passing the string and dictionary as arguments
count_vowels(string, dictionary)