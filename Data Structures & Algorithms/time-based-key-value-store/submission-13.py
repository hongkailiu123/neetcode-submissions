class TimeMap:

    def __init__(self):
        #key, list of value + timestamp
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store.keys():
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store.keys():
            return ""
        keyList = self.store[key]
        listLength = len(keyList)
        for i in range(listLength-1, -1, -1):
            if keyList[i][1] <= timestamp:
                return keyList[i][0] 

        return ""


