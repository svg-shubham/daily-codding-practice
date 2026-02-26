"""
Group Anagrams
Standard: ["eat", "tea", "tan", "ate", "nat", "bat"]

Ans: [["eat","tea","ate"], ["tan","nat"], ["bat"]]

No Anagrams: ["abc", "def", "ghi"] (Ans: [["abc"], ["def"], ["ghi"]])

Empty Elements: ["", ""] (Ans: [["", ""]])

Single Element: ["a"] (Ans: [["a"]])"""

def group_anagram(arr:list[str])->list[str]:
    dic = {}
    for i in arr:
        if "".join(sorted(i)) not in dic:
            dic["".join(sorted(i))] = [i]
        else:
            dic["".join(sorted(i))].append(i)
        
    return list(dic.values())


