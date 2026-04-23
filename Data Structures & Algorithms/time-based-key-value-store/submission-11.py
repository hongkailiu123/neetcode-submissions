class TimeMap:

    def __init__(self):
        #Number of distinct keys stored
        self.numOfKeys = 0
        #[key to index in values]
        self.keyToArray = {}
        #[key0's list, key1's list ...]
        self.values = []
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyToArray.keys():
            self.keyToArray[key] = self.numOfKeys
            self.numOfKeys += 1
            self.values.append([None]*1002)

        self.values[self.keyToArray[key]][timestamp] = value
        


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keyToArray.keys():
            return ""
        
        for i in range(timestamp, 0, -1):
            if self.values[self.keyToArray[key]][i]:
                return self.values[self.keyToArray[key]][i]
        
        return ""


