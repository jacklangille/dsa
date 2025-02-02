

class HashMap:
    def __init__(self, size):
        self.size = size 
        self.buckets = [[] for _ in range(size)]

    def _hash(self, k):
        return hash(k) % self.size

    def insert(self, k, v):
        # hash provided k
        idx = self._hash(k)
        bucket = self.buckets[idx]
    
        for i, (key,val) in enumerate(bucket):
            if k == key:
                bucket[i] = (k,v)
                return 
        bucket.append((k,v))

    def remove(self, k):
        idx = self._hash(k)
        bucket = self.buckets[idx]
        
        for i, (key,val) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                return True
        return False

    def get(self, k):
        idx = self._hash(k)
        bucket = self.buckets[idx]
        
        for i, (key,val) in enumerate(bucket):
            if k == key:
                return val
        return None


if __name__ == "__main__":
    hm = HashMap(size=10)
    print(hm.get("name"))

    hm.insert("name", "Jack")
    print(hm.get("name"))












