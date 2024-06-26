'''
Problem: 271. Encode and Decode Strings

Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.
Please implement encode and decode

Example 1:
Input: ["neet","code","love","you"]
Output:["neet","code","love","you"]

Example 2:
Input: ["we","say",":","yes"]
Output: ["we","say",":","yes"]

Constraints:
0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains only UTF-8 characters.
'''

class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        # add string_length followed by '#' to indicate end-of-word
        for s in strs:
            encoded_str += str(len(s)) + "#" +s
        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_string = []
        i = 0
        while i < len(s):
            j = i
            # first compute the sub-string length by moving j
            # increment j till you encounter '#' which denotes end-of-word
            while s[j]!="#":
                j += 1
            string_length = int(s[i:j])

            # select window from j to string length and append to the list
            decoded_string.append(s[j:j+string_length+1])
            i = j + string_length + 1
        return decoded_string