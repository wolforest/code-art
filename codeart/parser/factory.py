
from codeart.lang.parser import LineParser
from codeart.lang.java import JavaParser

class LangFactory(object):

    def create(lang: str) -> LineParser :
        if not lang:
            return None
        
        match lang.lower():
            case "java":
                return JavaParser()
            case _:
                raise SystemError("Can't find lang parser: " + lang)