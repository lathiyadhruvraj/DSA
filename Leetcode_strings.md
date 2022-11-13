### [1047. Remove All Adjacent Duplicates In String](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/)

### You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them. We repeatedly make duplicate removals on s until we no longer can.

### Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.
 
Example 1:

Input: s = "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
Example 2:

Input: s = "azxxzy"
Output: "ay"
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.

```diff
class Solution:
    def removeDuplicates(self, s: str) -> str:
        ans = []
        for c in s:
            if ans and ans[-1] == c: 
                ans.pop()
            else: 
                ans.append(c)
        return ''.join(ans)

```

---

### [151. Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/description/)

### Given an input string s, reverse the order of the words.

### A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

### Return a string of the words in reverse order concatenated by a single space.

##### Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

Example 1:
Input: s = "the sky is blue"
Output: "blue is sky the"


Example 2:
Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.


Example 3:
Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 

Constraints:
1 <= s.length <= 104
s contains English letters (upper-case and lower-case), digits, and spaces ' '.
There is at least one word in s.


```diff
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])

```

