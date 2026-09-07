class TimeMap:
    # info: all timestamps of set are increasing -> can be searched with binary search
    # 

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        new_value = [timestamp,value]
        if self.hashmap.get(key,"") == "":
            self.hashmap[key] = [new_value]
        else:
            self.hashmap[key].append(new_value)
        
    def get(self, key: str, timestamp: int) -> str:
        if self.hashmap.get(key, ",") == ",":
            return ""
        tv_list = self.hashmap[key]
        l, r = 0, len(tv_list) - 1
        potential_val = ""
        while l <= r:
            mid = (l+r) // 2
            if tv_list[mid][0] == timestamp:
                return tv_list[mid][1]
            elif tv_list[mid][0] < timestamp:
                potential_val = tv_list[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        return potential_val
                

            


            
        
