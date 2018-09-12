import pyodbc

class DBAccessor:
    """DB Access"""

    config = "DRIVER={SQL Server};SERVER=ECOLOGDB2016;DATABASE=ECOLOGDBver3"

    @classmethod
    def ExecuteQuery(self, query):
        cnn = pyodbc.connect(self.config)
        cur = cnn.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        cur.close()
        cnn.close()
        return rows

    @classmethod
    def QueryString(self):
        query = """
        SELECT SEMANTIC_LINK_ID, ENDPOINTS_OF_SEMANTIC_LINKS.DIRECTION, 
		CASE WHEN ENDPOINTS_OF_SEMANTIC_LINKS.LATITUDE IS NULL THEN LINKS.LATITUDE ELSE ENDPOINTS_OF_SEMANTIC_LINKS.LATITUDE END, 
		CASE WHEN ENDPOINTS_OF_SEMANTIC_LINKS.LONGITUDE IS NULL THEN LINKS.LONGITUDE ELSE ENDPOINTS_OF_SEMANTIC_LINKS.LONGITUDE END
        FROM ENDPOINTS_OF_SEMANTIC_LINKS, LINKS
        WHERE ENDPOINTS_OF_SEMANTIC_LINKS.NODE_ID = LINKS.NODE_ID AND ENDPOINTS_OF_SEMANTIC_LINKS.LINK_ID = LINKS.LINK_ID
        ORDER BY DIRECTION
        """
        return query 

    @classmethod
    def ExecuteManyInsert(self, query, dataList):
        cnn = pyodbc.connect(self.config)
        cur = cnn.cursor()
        cur.executemany(query, dataList)
        cur.commit()
        cur.close()
        cnn.close()

    @classmethod
    def QueryInsertString(self):
        query = "INSERT INTO GOOGLE_DISTANCE_MATRIX VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
        return query