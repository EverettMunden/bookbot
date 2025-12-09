def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents= f.read()
    return file_contents
def num_count(path_to_file):
    count= 0
    text= get_book_text(path_to_file)
    words= text.split()
    for word in words:
        count+= 1
    return count
def letter_count(path_to_file):
    pops= get_book_text(path_to_file)
    texts= pops.split()
    let_count= {
            "a": 0,
            "b": 0,
            "c": 0,
            "d": 0,
            "e": 0,
            "f": 0,
            "g": 0,
            "h": 0,
            "i": 0,
            "j": 0,
            "k": 0,
            "l": 0,
            "m": 0,
            "n": 0,
            "o": 0,
            "p": 0,
            "q": 0,
            "r": 0,
            "s": 0,
            "t": 0,
            "u": 0,
            "v": 0,
            "w": 0,
            "x": 0,
            "y": 0,
            "z": 0,
            "$": 0,
            " ": 0,
            "=": 0,
            "?": 0,
            "!": 0,
            "%": 0,
            "+": 0
     }
    for text in texts:
        for ch in text:
            ch = ch.lower()
            if ch not in let_count:
                let_count[ch] = 0
                let_count[ch] += 1
            else:
                let_count[ch] += 1
    return let_count
def sorted_list(path_to_file):
    def sort_on(items):
        return items["num"]
    pun= letter_count(path_to_file)
    big_list = [
            ]
    for letter in pun:
        value = pun[letter]
        new = {"alph": letter, "num": value}
        big_list.append(new)
    big_list.sort(reverse=True, key=sort_on)
    return big_list



