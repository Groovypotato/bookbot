def get_num_words (text):
    text_split = text.split()
    wnumb = len(text_split)
    return wnumb

def letter_count(text):
    l_count = {}
    for t in text:
        lower =  t.lower()
        if lower in l_count:
            l_count[lower] += 1
        else:
            l_count[lower] = 1
    return l_count
          
            
def sorted_words(dictionary):
    dic_list = []
    for character, count in dictionary.items():
        # Create a dictionary with character and count
        char_dict = {"character": character, "count": count}
        dic_list.append(char_dict)
    
    # Define a function to tell sort which value to use
    def sort_on(dict):
        return dict["count"]
    
    # Sort the list in place
    dic_list.sort(reverse=True, key=sort_on)
    
    # Return the sorted list
    return dic_list
    