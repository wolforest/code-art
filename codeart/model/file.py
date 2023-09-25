from collections import deque

class CodeBlock(object):
    totalLines: int = 0

    children = [] 

class MethodBlock(CodeBlock):
    parameterNum: int = 0

    maxIntentLevel: int = 0

    ifBlockNum: int = 0
    '''
    for/while/foreach
    '''
    loopBlockNum: int = 0

class ClassBlock(CodeBlock):
    className: str

    staticAttributeNum: int = 0
    attributeNum: int = 0

    publicMethodNum: int = 0
    privateMethodNum: int = 0
    protectedMethodNum: int = 0

    attributeList: list = []
    methodList: list = []

class FileBlock(CodeBlock):
    importNum: int = 0
    classNum: int = 0
    methodNum: int = 0
    maxClassLines: int = 0
    maxMethodLines: int = 0

    classList: list = []
    methodList: list = []


class FileContext(object):
    
    def __init__(self) -> None:
        self.blockStack = deque()