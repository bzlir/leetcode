class  TrieNode:
    def __init__(self):
        self.kids = {}
        self.word = False


class WordDictionary(object):

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        cur = self.root
        for c in word:
            if c not in cur.kids:
                cur.kids[c] = TrieNode()
            cur = cur.kids[c]
        cur.word = True


    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        def dfs(j, root):
            cur = root
            for i in range(len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.kids.values():
                        if dfs(i+1, child):
                            return True
                    return False

                else:
                    if c not in cur.kids:
                        return False
                    cur = cur.kids[c]

        dfs(0,self.root)