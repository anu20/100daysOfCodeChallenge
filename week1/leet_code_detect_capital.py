class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        isfirstLetterUpper=False
        if word[0].isupper():
            isfirstLetterUpper = True
        
        if isfirstLetterUpper:
            for i in range(1,len(word)-1):
                if word[i].isupper() and word[i+1].islower():
                    return False
                elif word[i].islower() and word[i+1].isupper():
                    return False
                
        else:
            for i in range(1,len(word)):
                if word[i].isupper():
                    return False
        return True
