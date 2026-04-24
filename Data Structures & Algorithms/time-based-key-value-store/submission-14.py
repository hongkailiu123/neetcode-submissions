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
        # the values were stored in ascending time order
        left = 0
        right = len(keyList) - 1
        ans = ""
        
        while left <= right:
            mid = (left + right)//2
            if keyList[mid][1] <= timestamp:
                ans = keyList[mid][0]
                left = mid + 1
            else:
                right = mid - 1

        return ans


