import sqlite3
import pandas as pd

class Emotion():
    def __init__(self):
        self.data = self.getData()
        
    def getData(self):
        db = sqlite3.connect("./rsc/emotions.db")
        df = pd.read_sql("SELECT * FROM Word",db)
        db.close()
        return df