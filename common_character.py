class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # if len(words) < 2:
        #     return sorted(words)

        if len(words) == 1:
            return sorted(list(words[0]))

        result = list(words[0])
        
        for word in words[1:]:
            new_result = []
            
            for char in result:
                if char in word:
                    new_result.append(char)
                    word = word.replace(char, "", 1)  
            result = new_result
        
        return sorted(result)
        
