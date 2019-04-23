import cx_Oracle

class SchemeGetter:
    def __init__(self, dbUrl, tableName):
        self.dbUrl = dbUrl
        self.tableName = tableName

    def convertToDic(self, queryResult):
        if(queryResult is not None and len(queryResult) > 0):
            scheme = {'tableName': queryResult[0][0], 'columns': []}
            for col in queryResult:
                scheme['columns'].append({'name': col[1], 'type': col[2]})
            return scheme
        else:
            return None

    def getTableInfo(self):
        con = cx_Oracle.connect(self.dbUrl)
        cur = con.cursor()
        cur.execute("SELECT TABLE_NAME, COLUMN_NAME, DATA_TYPE FROM ALL_TAB_COLUMNS WHERE TABLE_NAME = '{}' ORDER BY COLUMN_ID ASC".format(self.tableName))
        res = cur.fetchall()
        cur.close()
        con.close()
        return self.convertToDic(res)