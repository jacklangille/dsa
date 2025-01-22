
class HashMap:
    def __init__(self, size):
        self.size = size
        self.buckets = [[] for _ in range(size)]  # List of lists for each k/v pair

    def _hash(self, k):
        """
        Private hash function
        """
        return hash(k) % self.size

    def put(self, k, v):
        """
        Insert or update key/value pair in hash map
        """
        idx = self._hash(k)
        bucket = self.buckets[idx]

        # Update for loop
        for i, (key, val) in enumerate(bucket):
            if k == key:
                bucket[i] = (k, v)
                return

        # Insert
        bucket.append((k, v))

    def remove(self, k):
        """
        Delete provided key and corresponding value from map
        """
        idx = self._hash(k)
        bucket = self.buckets[idx]

        for i, (key, val) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                return

    def get(self, k):
        """
        Retrieve the provided key's value
        """
        idx = self._hash(k)
        bucket = self.buckets[idx]

        for i, (key, value) in enumerate(bucket):
            if k == key:
                return value

    def __contains__(self, k):
        """
        Check for existence of key in hash map
        """
        return True if self.get(k) else False


if __name__ == "__main__":
    hash_map = HashMap(10)
    hash_map.put("name", "Jack")

    print("name" in hash_map)
    print("apple" in hash_map)
