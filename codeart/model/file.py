
class ClassCounter(object):
    className: str
    staticAttributeNum: int = 0
    attributeNume: int = 0

class MethodCounter(object):
    parameterNum: int = 0
    totalLines: int = 0
    noIntentLines: int = 0
    maxIntentLevel: int = 0
    '''
    for/while/
    '''
    loopBlockNum: int = 0

class FileCounter(object):
    totalLines: int = 0

    importNum: int = 0
    classNum: int = 0
    methodNum: int = 0
    maxClassLines: int = 0
    maxMethodLines: int = 0

