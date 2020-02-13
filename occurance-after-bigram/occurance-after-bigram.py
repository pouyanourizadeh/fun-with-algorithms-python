"""
Given words first and second, consider occurrences in some text of the form "first second third", where second comes immediately after first, and third comes immediately after second.

For each such occurrence, add "third" to the answer, and return the answer.

 

Example 1:

Input: text = "alice is a good girl she is a good student", first = "a", second = "good"
Output: ["girl","student"]
"""

class Solution(object):
    def findOcurrences(self, text, first, second):
        
        output_list = []
        text_list = text.split(" ")
        
        counter = 0
        for word in text_list:
            if counter+3 <= len(text_list):
                if word == first and second == text_list[counter+1]:
                        output_list.append(text_list[counter+2])
                counter += 1
        return output_list