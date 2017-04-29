import time
english_word_file = 'wordsEn.txt'
english_word_file = open(english_word_file)
english_word_list = english_word_file.read().splitlines()
english_word_file.close()


def get_words(letters):
    success_list = []
    for word in english_word_list:
        if not(letters[0] in word) or len(word) > 9 or len(word) < 4:
            continue
        
        success = True
        letters_copy = list(letters)
        for letter in word:
            if letter not in letters_copy:
                success = False
                break
            else:
                letters_copy.pop(letters_copy.index(letter))
                
        if success:
            success_list.append(word)
    
    return success_list
      
        
def display(fitting_words, duration):
    words_ending_in_s = []
    definite_words = []
    for word in fitting_words:
        if word[-1] == 's':
            words_ending_in_s.append(word)
        else:
            definite_words.append(word)
            
    print("Definite words:")

    for word in definite_words:
        print(word)
    
    if len(words_ending_in_s) > 0:
        print("\nPossible words:")
        for word in words_ending_in_s:
            print(word)

    print('\nFound in {0:.4f} seconds.\n'.format(duration))

    
def main():
    prompt = "Please give the 9 letters (middle first) or 'Q' to quit: "
    given_letters = input(prompt).lower()
    
    if given_letters != 'q':
        while len(given_letters) != 9:
            print("Could not parse given letters.")
            print("Format: \"ABCDEFGHI\" where A must be included in all.\n")
            
            given_letters = input(prompt).lower()
        
        start = time.time()
        fitting_words = get_words(given_letters)
        end = time.time()
        
        display(fitting_words, end - start)
        
        main()

if __name__ == "__main__":
    main()
