class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 1. The O(1) Shield
        if len(s) != len(t):
            return False
            
        # 2. The Empty Ledger
        letter_ledger = {}
        
        # 3. The First Pass (String 's')
        for letter in s:
            letter_ledger[letter] = letter_ledger.get(letter, 0) + 1
            
        # 4. The Second Pass (String 't')
        for letter in t:
            letter_ledger[letter] = letter_ledger.get(letter, 0) - 1
            
        # 5. The Final Audit
        for count in letter_ledger.values():
            if count != 0:
                return False
                
        # If it survives the entire audit, the scale is perfectly balanced.
        return True