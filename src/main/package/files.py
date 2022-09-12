import os
import json

class JSON:
    def __init__(self, path, encoding="utf8") -> None:
        if os.path.isfile(path):
            self.path: str = path
        else:
            raise FileNotFoundError
        
        self.encoding: str = encoding
        self.data: dict | list = self.load()

    def load(self, 
             open_options: dict = {}, 
             load_options: dict = {}, 
             encoding: str | None = None) -> dict | list:
        encoding = encoding or self.encoding
        with open(self.path, 'r', encoding=encoding, **open_options) as file:
            return json.load(file, **load_options)
    
    def dump(self, 
             open_options: dict = {}, 
             dump_options: dict = {}, 
             encoding: str | None = None) -> None:
        encoding = encoding or self.encoding
        with open(self.path, 'w', encoding=encoding, **open_options) as file:
            json.dump(self.data, file, **dump_options)
    
    def save(self):
        for _ in range(3):
            self.dump()
            if (new:=self.load()) == self.data:
                self.data = new
                return self.data
        return new