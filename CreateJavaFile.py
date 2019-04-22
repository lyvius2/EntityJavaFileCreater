import GetScheme
import ConvertToCamelCase

class CreateJavaFile:
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)

    def defineType(self, type):
        return {'VARCHAR2': 'String', 'NUMBER': 'Long', 'DATE': 'Date'}.get(type, 'String')

    def writeJavaFile(self, className, content):
        f = open('{}.java'.format(className), 'w')
        f.write(content)
        f.close()

    def createContent(self, dbUrl, tableName):
        scheme = GetScheme.SchemeGetter(dbUrl, tableName)
        tableInfo = scheme.getTableInfo()
        if(tableInfo is not None):
            case = ConvertToCamelCase.ToCamelcase()
            className = case.converter(tableInfo['tableName'], True)
            content = ['@Data\n']
            content.append('@Entity\n')
            content.append('@Table(name = "{}")\npublic class {} {\n'.format(tableInfo['tableName'], className))
            for col in tableInfo['columns']:
                content.append('@Column(name = "{}")\n'.format(col['name']))
                content.append('private {} {};\n\n'.format(self.defineType(col['type']), case.converter(col['name'], False)))
            content.append('}')
            self.writeJavaFile(className, ''.join(content))
        else:
            print('스키마가 존재하지 않습니다.')
        