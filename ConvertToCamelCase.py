import tocamelcase

class ToCamelcase:

    def __init__(self, filePath):
        self.filePath = filePath

    def converter(self, snakeText):
        convertResult = tocamelcase.convert(snakeText)
        return '{}{}'.format(convertResult[0].lower(), convertResult[1:])

    def executor(self):
        f = open(self.filePath, 'r')
        resultStr = ''
        while True:
            line = f.readline()
            if not line: break
            resultStr += self.converter(line)
        f.close()
        print(resultStr)
        return resultStr