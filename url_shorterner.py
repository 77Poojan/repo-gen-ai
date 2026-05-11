class Codec:
    def __init__(self):
        self.id = 0
        self.map = {}
        self.base = "https://tinyurl.com/"
        self.BASE58 = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"

    # 🔹 Encode integer → Base58 string
    def encode_base58(self, num):
        if num == 0:
            return self.BASE58[0]
        
        res = []
        while num > 0:
            num, rem = divmod(num, 58)
            res.append(self.BASE58[rem])

        return ''.join(reversed(res))

    # 🔹 Decode Base58 → integer (optional)
    def decode_base58(self, s):
        num = 0
        for char in s:
            num = num * 58 + self.BASE58.index(char)
        return num

    # 🔹 Encode long URL → short URL
    def encode(self, longUrl: str) -> str:
        self.id += 1
        short_key = self.encode_base58(self.id)
        self.map[short_key] = longUrl
        return self.base + short_key

    # 🔹 Decode short URL → original URL
    def decode(self, shortUrl: str) -> str:
        key = shortUrl.split("/")[-1]
        return self.map.get(key)
    

if __name__ == "__main__":
    codec = Codec()

    short = codec.encode("https://google.com")
    print("Short URL:", short)
    short = codec.encode("https://bing.com")
    
    print("Short URL:", short)

    original = codec.decode(short)
    print("Original URL:", original)