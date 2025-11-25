#
# @lc app=leetcode.cn id=49 lang=python3
# @lcpr version=30204
#
# [49] 字母异位词分组
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = {}
        for word in strs:
            sorted_words = ''.join(sorted(word))
            if sorted_words in anagrams_dict:
                anagrams_dict[sorted_words].append(word)
            else:
                anagrams_dict[sorted_words] = [word]
        return list(anagrams_dict.values())
            
        
# @lc code=end



#
# @lcpr case=start
# ["eat", "tea", "tan", "ate", "nat", "bat"]\n
# @lcpr case=end

# @lcpr case=start
# [""]\n
# @lcpr case=end

# @lcpr case=start
# ["a"]\n
# @lcpr case=end

#

