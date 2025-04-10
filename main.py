import difflib

class WordDictionary:
    def __init__(self):
        self.words = set()

    def build_dictionary(self, file_path):
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    word = line.strip().lower()
                    if word:
                        self.words.add(word)
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")

    def search_word(self, query):
        query = query.lower().strip()

        if not query:
            return "Empty input is not a valid word."

        if query in self.words:
            return f"'{query}' found in dictionary."
        else:
            suggestions = difflib.get_close_matches(query, self.words, n=5, cutoff=0.75)
            if suggestions:
                return f"'{query}' not found. Did you mean: {', '.join(suggestions)}?"
            else:
                return f"No close match found for '{query}'."

if __name__ == "__main__":
    dictionary = WordDictionary()
    dictionary.build_dictionary("list.txt")

    print("Type a word to search (or 'exit' to quit):")
    while True:
        word_input = input(">> ").strip()
        if word_input.lower() == 'exit':
            break
        result = dictionary.search_word(word_input)
        print(result)
