    
class AnagramFinder:
    def __init__(self,firstWord,secondWord):
        self.firstWord = firstWord
        self.secondWord = secondWord

    def IsAnagram(self):
        if not self.AreLengthsEqual():
            return False
        if not self.DoesContainSameNumberOfElements():
            return False
        return True

        
        
    def AreLengthsEqual(self):
        return len(self.firstWord) == len(self.secondWord)
    
    def DoesContainSameNumberOfElements(self):
        
        countFirstWord, countSecondWord = {}, {}
        for i in range(len(self.firstWord)):
            countFirstWord[self.firstWord[i]] = 1 + countFirstWord.get(self.firstWord[i],0)
            # since we already know they have same number of element
            countSecondWord[self.secondWord[i]] = 1 + countSecondWord.get(self.secondWord[i],0)
        
        for c in countFirstWord:
            if  countFirstWord[c] != countSecondWord.get(c):
                return False
        return True
    
    def FindAnagramBySorting(self):
        # Alternative way which have better memory usage but worse time complexity: worst case O(n^2)
        first = sorted(self.firstWord)
        second = sorted(self.secondWord)
        if first == second:
            return True
        return False
        
        
    
firstWord = input('What is the first word\n')
secondWord = input('What is the second word\n')

finder = AnagramFinder(firstWord,secondWord)

print(finder.IsAnagram())

input("Press Enter to continue...")
