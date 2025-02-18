from datetime import datetime

class Nota:


    High: str = "high"
    medium: str = "medium"
    low: str = "low"



  def __int__(self, code: str, title: str, text: str, importance: str):
        self.code: str = code
        self.title: str = title
        self.text: str = text
        self.importance: str = importance
        self.creation_date = datetime.now()
        self.tags: list[str] = []
























