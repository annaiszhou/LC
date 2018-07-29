class Codec:
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        self.dict={}
        self.counter=0
        if longUrl not in self.dict:
            shortUrl="http://tinyurl.com/"+str(self.counter)
            self.dict[longUrl]=shortUrl
            self.dict[shortUrl]=longUrl
            self.counter+=1
            return shortUrl
        else:
            return self.dict[longUrl]

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        return self.dict[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

#Runtime: 24 ms
#Your runtime beats 100.00 % of python submissions.