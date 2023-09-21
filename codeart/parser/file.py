
from codeart.model.file import FileCounter
from codeart.lang.factory import LangFactory
from pywolf.utils import pathutils, fileutils

class FileParser(object):

    def __init__(self, fileName):
        if not fileName:
            raise SystemError("fileName can't be blank")
        
        if not fileutils.exists(fileName):
            raise SystemError("can't find file: " + fileName)
        
        self.fileName = fileName
        self.fileCounter = FileCounter()
    
    def parse(self) -> FileCounter:
        self.get_lang_parser()
        self.parse_file()

        return self.fileCounter


    def get_lang_parser(self):
        ext = pathutils.extension(self.fileName, withoutDot=True, toLower=True)
        self.langParser = LangFactory.create(ext)


    def parse_file(self):
        file = open(self.fileName, 'r')

        for line in file:
            self.parse_line(line)

        file.close()

    def parse_line(self, line: str):
        pass

    
