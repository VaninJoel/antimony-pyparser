import lark
import os


# %import common.DIGIT
# %import common.NUMBER
# %import common.FLOAT
# %import common.WORD
# %import common.LETTER
# %import common.WS
# %ignore WS
# %ignore COMMENT
# /'[^']*'/

class WordTransformer(lark.Transformer):
    word_dict = dict(

    )

    def WORD(self, word):
        if word in self.word_dict:
            return self.word_dict[word]
        return word


class AntimonyParser(lark.Visitor):
    with open(os.path.join(os.path.dirname(__file__), "grammar.lark")) as f:
        grammar = f.read().strip()

    def __init__(self):
        self.lark = lark.Lark(self.grammar)

    def parse(self, antimony_string):
        tree = self.lark.parse(antimony_string)
        tree = WordTransformer(visit_tokens=True).transform(tree)
        return tree

    def assignment(self, tree):
        # assert tree.data == "assignment"
        # print(tree.data, type(tree.data), tree.children[1])
        tree.children[1] = str(float(tree.children[1]) + 1)
        return tree
