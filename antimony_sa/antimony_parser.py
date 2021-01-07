import lark


# %import common.DIGIT
# %import common.NUMBER
# %import common.FLOAT
# %import common.WORD
# %import common.LETTER
# %import common.WS
# %ignore WS
# %ignore COMMENT
# /'[^']*'/

class AntimonyParser:
    grammar = """
        ?start: "import" FILENAME -> import_filename

        // implementation of import statement parser        
        // DRIVE_LETTER allowed 0 or more times
        // recursive to allow for arbitrary filename segments
        FILENAME:  DOUBLE_QUOTE FILENAME_SEGMENT (FILENAME_SEGMENT)* DOUBLE_QUOTE 
        FILENAME_SEGMENT: FILE_SEPARATOR WORD 
        DOUBLE_QUOTE: /"/
        SINGLE_QUOTE: /'/
        WORD: /[A-Za-z0-9_\.]*/
        FILE_SEPARATOR: "/"
        
        %import common.WS
        %ignore WS
    
    """

    def __init__(self):
        self.lark = lark.Lark(self.grammar)

    def parse(self, antimony_string):
        return self.lark.parse(antimony_string)


















