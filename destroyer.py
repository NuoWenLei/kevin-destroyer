import json
def preprocess():
    with open("dictionary.txt", "r") as dict_txt:
        words = dict_txt.readlines()
    processed_words = []
    for word in words:
        w = word.strip()
        if len(w) < 3:
            continue
        processed_words.append({
            "word": w,
            "count": count([*w]),
            "length": len(w)
		})
    with open("anagram_dict.json", "w") as dict_json:
         json.dump(processed_words, dict_json)
        
def count(letters):
    counter = {}
    for letter in letters:
        if letter in counter.keys():
            counter[letter] += 1
        else:
            counter[letter] = 1
    return counter

def search(letters, gram_dict):
    filtered_words = []
    for w in gram_dict:
        c = w["count"]
        for k in c.keys():
            if k not in letters.keys():
                break
            if c[k] > letters[k]:
                break
        else:
            filtered_words.append((w["word"], w["length"]))
    return filtered_words
    
def main():
    letters = [*"dosasl"]
    with open("anagram_dict.json", "r") as dict_json:
        d = json.load(dict_json)
        
    results = search(count(letters), d)
    print("\n".join([item[0] for item in (sorted(results, key = lambda x: x[1], reverse=False))]))
    

if __name__ == "__main__":
    main()