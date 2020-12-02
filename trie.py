import pickle


# We will be implementing trie.
# Methods used will be : search ,insert ,remove ,starts with.

# Root has a Dictionary to store a Parent child Relationship, and the boolean value

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = {}
        self.end_here = False


class Trie:
    def __init__(self):
        self.root = TreeNode(self)
        self.number_of_nodes = 0

    def remove(self, word):
        parent = self.root
        current = parent.children[word[0]]
        print("working remove")
        print(parent.value)
        print(current.value)
        self.delete1(current, parent, word, 0)

    def delete1(self, node, parent_node, word, i):
        print(i)
        if i == len(word) - 1:
            print("Last Word")
            if node.end_here:
                node.end_here = False
                if len(node.children) == 0:
                    print("delete")
                    del parent_node.children[word[i]]
                    return True
                else:
                    return False
            else:
                return False
        else:
            if word[i+1] in node.children and self.delete1(node.children[word[i+1]], node, word, i + 1):
                if len(node.children) == 0:
                    del parent_node.children[word[i]]
                    return True
                else:
                    return False
            else:
                return False

    def insert(self, word):
        current = self.root
        for i, char in enumerate(word):
            if char in current.children:
                current = current.children[char]
            else:
                current.children[char] = TreeNode(char)
                self.number_of_nodes += 1
                current = current.children[char]
            if i == len(word) - 1:
                current.end_here = True

    def words_start_with(self, word):
        list_of_words = []
        current_word = word
        current = self.root

        for i, char in enumerate(word):
            if char in current.children:
                current = current.children[char]

        self.words_recursion(current, current_word, list_of_words)  # we are reaching till the last prefix word node.
        return list_of_words

    def words_recursion(self, current, current_word, list_of_words):
        if current is None:
            return
        for x in current.children:
            current_word += x
            print(current_word)
            self.words_recursion(current.children[x], current_word,
                                 list_of_words)  # It goes till last character in a branch.
            print(current.children[x].end_here)
            if current.children[x].end_here:
                list_of_words.append(current_word)
                return
            current_word = current_word[0:-1]

    def search(self, word):
        current = self.root
        for i, char in enumerate(word):
            if char in current.children:
                if i == len(word) - 1:
                    return current.children[char].end_here
                current = current.children[char]
            else:
                return False

    def search_pre(self, word):
        current = self.root
        for char in word:
            if char in current.children:
                current = current.children[char]
            else:
                return False
        return True

    def print_tree(self):
        current = self.root
        node = 0
        self.print_tree_recursion(current, node)

    def print_tree_recursion(self, current, node):
        for x in current.children:
            if node == 0:
                print()
                print("-" * 50, end="")

            if len(current.children) > 1:
                print()
                print('*' * node + x, end="")
            elif len(current.children) == 1 and current.end_here:
                print()
                print('*' * node + x, end="")
            else:
                print(x, end="")

            self.print_tree_recursion(current.children[x], node + 1)


with open("t1.data", "rb") as my_data:
    t1 = pickle.load(my_data)

while True:
    t1.print_tree()
    print()
    ans = input("Enter a task to perform : ")

    if ans == "insert":
        input_word = input("Enter word : ")
        t1.insert(input_word)
    elif ans == "delete":
        input_word = input("Enter word : ")
        t1.remove(input_word)
    elif ans == "search":
        input_word = input("Enter word : ")
        print(t1.search(input_word))
        input()
    elif ans == "search_pre":
        input_word = input("Enter word : ")
        print(t1.search_pre(input_word))
        input()
    elif ans == "all":
        input_word = input("Enter word : ")
        print(t1.words_start_with(input_word))
        input()
    else:
        break

with open("t1.data", "wb") as my_data:
    pickle.dump(t1, my_data)

t1.print_tree()
