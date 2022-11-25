import sqlite3

class Emoji():
    def __init__(self,set_emotion="乐",set_intensity=1):
        self.emotion = set_emotion
        self.intensity = set_intensity
        self.picture = self.getPicturePath(self.emotion,self.intensity)
        
    def getPicturePath(self,emo,its):
        db = sqlite3.connect("./rsc/emoji.db")
        cursor = db.cursor()
        query = "SELECT pngPath FROM Emoji WHERE emotion = ? and intensity - ? <= 4 and intensity - ? >= 0;"
        row = (emo,its,its,)
        results = cursor.execute(query, row).fetchall()
        cursor.close()
        db.close()
        return "./rsc/emoji/" + results[0][0]