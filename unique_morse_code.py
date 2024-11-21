class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        t = {}
        i = 'a'
        for m in morse_code:
            t[i] = m
            i = chr(ord(i) + 1)

        pairs = set()
        for w in words:
            string = ""
            for k in w:
                string += t[k]
            pairs.add(string)

        return len(pairs)
