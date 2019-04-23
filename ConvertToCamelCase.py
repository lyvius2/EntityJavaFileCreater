import tocamelcase

class Changer:
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)

    def converter(self, snakeText, isClassName):
        convertResult = tocamelcase.convert(snakeText)
        if(isClassName is True):
            return convertResult
        else:
            return '{}{}'.format(convertResult[0].lower(), convertResult[1:])