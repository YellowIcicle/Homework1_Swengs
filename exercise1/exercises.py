# Part 1: Strings, lists and control structures


def count_characters(str_under_test):
    return len(str_under_test)
    """Returns the length of str_under_test"""
    raise NotImplementedError()


def first_three_letters(str_under_test):
    return str_under_test[:3]
    """Returns the first three letters of str_under_test"""
    raise NotImplementedError()


def last_three_letters(str_under_test):
    return str_under_test[-3:]
    """Returns the last three letters of str_under_test"""
    raise NotImplementedError()


def split_words(str_under_test):
    return str_under_test.split(" ")
    """Splits str_under_test into a list of words"""
    raise NotImplementedError()


def replace(str_under_test,search_str,replace_by):
    return str_under_test.replace(search_str,replace_by)
    """Replace all occurrences of search_str by string given in replace_by"""
    raise NotImplementedError()


def normalize(str_under_test,mode):
    """Performs string normalization
    Keyword arguments:
    mode -- can either be 1,2 or 3. 1 returns the string lower case, 2 upper case and 3 capitalized. Any 
    other value raises an ValueError with message "Invalid mode" 
    """
    if mode == 1:
        return str_under_test.lower()
    elif mode == 2:
        return str_under_test.upper()
    elif mode == 3:
        return str_under_test.capitalize()
    else:
        raise ValueError("Invalid mode")
    raise NotImplementedError()


def find_title(titles,search_str):
    """Searches a list of strings
      
    If titles=["Blade Runner","Star wars","Star trek"] and 
    search_str="star" the function returns
    ["Star wars","Star trek"]. The search is case-insensitive. 
    If no match is found, an empty list is returned.  
    """
    result = []
    for name in titles:
        if search_str.lower() in name.lower():
            result.append(name)

    return result
    raise NotImplementedError()
    
# Part 2 - Working with lists and dictionaries


def calculate_mean(numbers):
    """This function returns the mean value of all numbers given in the list. 
    
    Thus, calculate_mean([8,4,10,2]) returns 6.0. 
    The function returns None, if the list is empty.
    """
    if len(numbers) == 0:
        return None
    else:
        return sum(numbers) / len(numbers)
    raise NotImplementedError()


def min_mean_max(numbers):
    """This function returns a tuple, the smallest element in numbers, the mean value of all 
    numbers and the highest number in the list. 
    
    Thus, calculate_mean([8,4,10,2]) should return (2,6.0,10)
    The function returns None, if the list is empty.
    """
    if len(numbers) == 0:
        return None
    else:
        return min(numbers), sum(numbers) / len(numbers), max(numbers)
    raise NotImplementedError()


def mean_temperature(weather_data):
    """Returns the mean temperature for the weather_data provided.
    
    This functions takes in a list of tuples providing weather data for a given city for a 
    year following this format:
    [ (1, 21) , (2,23) , ... (12,8) ] - whereas the first 
    variable indicates the month as integer and the second variable the actual temperature
    The functions returns the mean temperature for this city. Using Python's round function,
    the function rounds the result to 1 digit. 
    If the input list is empty, None is returned.
    """
    numbers = []
    for i in weather_data:
        numbers.append(i[1])
    if len(numbers) == 0:
        return None
    else:
        return round(sum(numbers) / len(numbers),1)
    raise NotImplementedError()


def word_count(document):
    """Returns a dictionary with a word count of all words given in document
    
    Thus, if "Los Angeles is bigger than Berlin but Berlin is older than Los Angeles ." is 
    provided in string document, the function returns the dictionary:
    {"Los":2, "Angeles":2, "is":2, "bigger:"1","than":2,"Berlin":2,"but":1,"older":1,".":1}
    """
    words = document.split()
    wordlist = dict()
    for word in words:
        wordlist[word] = wordlist.get(word,0) + 1
    return wordlist


    raise NotImplementedError()


def common_words(document,threshold=2):
    """Returns the most common words in document, ordered in descending order.
    
    Thus, if "Los Angeles is bigger than Berlin but Berlin is older than Los Angeles ." is 
    provided, the function returns a list of words with occurrences equal or greater as
    the number given in threshold. If threshold is 2, the function would return
    ["Los","Angeles","is","than","Berlin"]
    """
    words = document.split()
    wordlist = dict()
    for word in words:
        wordlist[word] = wordlist.get(word, 0) + 1

    resultlist = []
    for a in wordlist.items():
        if a[1] >= 2:
            resultlist.append((a[0]))

    return resultlist
    raise NotImplementedError()

