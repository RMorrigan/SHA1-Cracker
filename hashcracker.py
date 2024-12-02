import hashlib
import itertools
#import numpy as np

'''
def generate_numeric_passwords():
    num_passwords = []
    numDict = np.arange(1000000)
    num_passwords.append(str(numDict))

    return num_passwords
'''
#This is the old one. Testing the one above for memory
def generate_numeric_passwords():
    num_passwords = ['123456']
    print("Generating Numeric Passwords...")
    '''
    for i in range(1000001):
        ##byteVal = i.to_bytes(6, 'big')
        #num_passwords.append(str(i))
        num_passwords.append(f"{i:07d}")
    '''
    return num_passwords
'''
def generate_numeric_passwords():
    num_passwords = []
    stringbuf = []
    for i in range(9):
        for j in range (9):
             for k in range (9):
                  for l in range (9):
                       for m in range (9):
                            for n in range (9):
                                 for o in range (9):
'''

# Function to generate word-based passwords using a dictionary file
def generate_word_passwords(dictionary_file):
    word_passwords = []
    print("Generating Word Passwords...")
    with open(dictionary_file, 'r') as file:
        for line in file:
            word = line.strip()
            # Add the word itself
            word_passwords.append(word)
            # Add numbers after the word (e.g., word1, word2, ..., word9)
            for i in range(1000001):
                #word_passwords.append(word + str(i))
                word_passwords.append(word + f"{i:07d}")
    
    return word_passwords

def generate_phrase_passwords(dictionary_file):
    print("Generating Phrase Passwords...")
    phrase_passwords = []
    with open(dictionary_file, 'r') as file:
        words = file.read().splitlines()
    
    #Generates all combination of phrases length 2
    word_combos =[''.join(pair) for pair in itertools.combinations(words, 2)]
    for combo in word_combos:
        for num in range(1001):  # numbers from 0 to 1000
            phrase_passwords.append(f"{combo} {num}")

    return phrase_passwords

# Function to read the password file and return user_id -> hashed_password mapping
def read_password_file(password_file):
    user_password_hashes = {}
    with open(password_file, 'r') as file:
        for line in file:
            user_id, hashed_password = line.strip().split()
            user_password_hashes[user_id] = hashed_password
    return user_password_hashes

# Function to crack the passwords using a list of candidate passwords
def crack_passwords(passwords_file, dictionary_file):
    # Step 1: Read the passwords file (user ID -> SHA-1 hash)
    user_password_hashes = read_password_file(passwords_file)
    
    # Step 2: Generate potential passwords
    potential_passwords = generate_numeric_passwords()
    #potential_passwords += generate_word_passwords(dictionary_file)
    potential_passwords += generate_phrase_passwords(dictionary_file)
    
    # Step 3: Try to crack each user's password by comparing hashes
    print("Cracking Passwords...")
    cracked_passwords = {}
    
    for user_id, hashed_password in user_password_hashes.items():
        for password in potential_passwords:
            # Hash the current password and check if it matches
            hashed_attempt = hashlib.sha1(password.encode()).hexdigest()
            if hashed_attempt == hashed_password:
                cracked_passwords[user_id] = password
                print(f"User {user_id} cracked with password: {password}")
                break  # Stop once the password is found
    
    return cracked_passwords

# Main function to execute the password cracking process
if __name__ == '__main__':
    passwords_file = 'passwords.txt'  # Path to the file containing user IDs and SHA-1 hashes
    dictionary_file = 'dictionary.txt'  # Path to the dictionary file containing common words
    
    print("Generating Passwords...")
    # Step 4: Crack passwords
    cracked_passwords = crack_passwords(passwords_file, dictionary_file)
    
    # Step 5: Print the number of cracked passwords
    print(f"Cracked passwords for {len(cracked_passwords)} users.")


    '''
    


    '''