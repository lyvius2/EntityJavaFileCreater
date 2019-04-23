import GetScheme
import ConvertToCamelCase
import os

class Maker:
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)

    def defineType(self, type):
        return {'VARCHAR2': 'String', 'NUMBER': 'Long', 'DATE': 'Date'}.get(type, 'String')

    def writeJavaFile(self, className, content):
        javaFile = '{}.java'.format(className)
        f = open(javaFile, 'w')
        f.write(content)
        f.close()
        if(os.path.exists(javaFile)):
            print('Entity Java파일 생성 완료되었습니다.')

    def createContent(self, dbUrl, tableName):
        scheme = GetScheme.SchemeGetter(dbUrl, tableName)
        tableInfo = scheme.getTableInfo()
        if(tableInfo is not None):
            case = ConvertToCamelCase.Changer()
            className = case.converter(tableInfo['tableName'], True)
            content = ['@Data\n']
            content.append('@Entity\n')
            content.append('@Table(name = "{}")\npublic class {}  implements Serializable '.format(tableInfo['tableName'], className))
            content.append('{\n')
            for col in tableInfo['columns']:
                content.append('\t@Column(name = "{}")\n'.format(col['name']))
                content.append('\tprivate {} {};\n\n'.format(self.defineType(col['type']), case.converter(col['name'], False)))
            content.append('}')
            self.writeJavaFile(className, ''.join(content))
        else:
            print('스키마가 존재하지 않습니다.')
        