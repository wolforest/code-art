from enum import Enum

class CodeType(Enum):
    PACAGE = ';'
    IMPORT = ';'

    CLASS_DECLARATION = '{'
    CLASS = '}'

    ATTRIBUTE_DECLARATION = ';'

    METHOD_DECLARATION = '{'
    METHOD = '}'

    COMMENT_LINE = '//'
    COMMENT_START = '/*'
    COMMENT_END = '*/'



