"""
This file contains competitive coding problems and their templates in different languages.
Each problem has:
1. Problem description
2. Input/Output format
3. Example test cases
4. Template code in different languages
"""

PROBLEMS = {
    "arrays": {
        "two_sum": {
            "title": "Two Sum",
            "difficulty": "Easy",
            "description": "Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twice.",
            "input_format": "nums: List[int], target: int",
            "output_format": "List[int]",
            "example": {
                "input": "nums = [2,7,11,15], target = 9",
                "output": "[0,1]",
                "explanation": "Because nums[0] + nums[1] == 9, we return [0, 1]."
            },
            "test_cases": [
                {
                    "input": {"nums": [2,7,11,15], "target": 9},
                    "output": [0,1]
                },
                {
                    "input": {"nums": [3,2,4], "target": 6},
                    "output": [1,2]
                },
                {
                    "input": {"nums": [3,3], "target": 6},
                    "output": [0,1]
                }
            ],
            "templates": {
                "python": """def twoSum(nums: List[int], target: int) -> List[int]:
    # Write your code here
    pass""",
                "java": """class Solution {
    public int[] twoSum(int[] nums, int target) {
        // Write your code here
        return new int[]{};
    }
}""",
                "cpp": """class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // Write your code here
        return {};
    }
};""",
                "javascript": """/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
function twoSum(nums, target) {
    // Write your code here
}"""
            }
        },
        "max_subarray": {
            "title": "Maximum Subarray",
            "difficulty": "Medium",
            "description": "Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.",
            "input_format": "nums: List[int]",
            "output_format": "int",
            "example": {
                "input": "nums = [-2,1,-3,4,-1,2,1,-5,4]",
                "output": "6",
                "explanation": "The subarray [4,-1,2,1] has the largest sum = 6."
            },
            "test_cases": [
                {
                    "input": {"nums": [-2,1,-3,4,-1,2,1,-5,4]},
                    "output": 6
                },
                {
                    "input": {"nums": [1]},
                    "output": 1
                },
                {
                    "input": {"nums": [5,4,-1,7,8]},
                    "output": 23
                }
            ],
            "templates": {
                "python": """def maxSubArray(nums: List[int]) -> int:
    # Write your code here
    pass""",
                "java": """class Solution {
    public int maxSubArray(int[] nums) {
        // Write your code here
        return 0;
    }
}""",
                "cpp": """class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        // Write your code here
        return 0;
    }
};""",
                "javascript": """/**
 * @param {number[]} nums
 * @return {number}
 */
function maxSubArray(nums) {
    // Write your code here
}"""
            }
        },
        "rotate_array": {
            "title": "Rotate Array",
            "difficulty": "Medium",
            "description": "Given an array, rotate the array to the right by k steps, where k is non-negative.",
            "input_format": "nums: List[int], k: int",
            "output_format": "None (modify nums in-place)",
            "example": {
                "input": "nums = [1,2,3,4,5,6,7], k = 3",
                "output": "[5,6,7,1,2,3,4]",
                "explanation": "rotate 1 steps to the right: [7,1,2,3,4,5,6], rotate 2 steps to the right: [6,7,1,2,3,4,5], rotate 3 steps to the right: [5,6,7,1,2,3,4]"
            },
            "test_cases": [
                {
                    "input": {"nums": [1,2,3,4,5,6,7], "k": 3},
                    "output": [5,6,7,1,2,3,4]
                },
                {
                    "input": {"nums": [-1,-100,3,99], "k": 2},
                    "output": [3,99,-1,-100]
                },
                {
                    "input": {"nums": [1,2], "k": 1},
                    "output": [2,1]
                }
            ],
            "templates": {
                "python": """def rotate(nums: List[int], k: int) -> None:
    # Write your code here
    pass""",
                "java": """class Solution {
    public void rotate(int[] nums, int k) {
        // Write your code here
    }
}""",
                "cpp": """class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        // Write your code here
    }
};""",
                "javascript": """/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
function rotate(nums, k) {
    // Write your code here
}"""
            }
        },
        "product_except_self": {
            "title": "Product of Array Except Self",
            "difficulty": "Medium",
            "description": "Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i]. You must write an algorithm that runs in O(n) time and without using the division operation.",
            "input_format": "nums: List[int]",
            "output_format": "List[int]",
            "example": {
                "input": "nums = [1,2,3,4]",
                "output": "[24,12,8,6]",
                "explanation": "answer[0] = 2*3*4 = 24, answer[1] = 1*3*4 = 12, answer[2] = 1*2*4 = 8, answer[3] = 1*2*3 = 6"
            },
            "test_cases": [
                {
                    "input": {"nums": [1,2,3,4]},
                    "output": [24,12,8,6]
                },
                {
                    "input": {"nums": [-1,1,0,-3,3]},
                    "output": [0,0,9,0,0]
                },
                {
                    "input": {"nums": [0,0]},
                    "output": [0,0]
                }
            ],
            "templates": {
                "python": """def productExceptSelf(nums: List[int]) -> List[int]:
    # Write your code here
    pass""",
                "java": """class Solution {
    public int[] productExceptSelf(int[] nums) {
        // Write your code here
        return new int[]{};
    }
}""",
                "cpp": """class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        // Write your code here
        return {};
    }
};""",
                "javascript": """/**
 * @param {number[]} nums
 * @return {number[]}
 */
function productExceptSelf(nums) {
    // Write your code here
}"""
            }
        },
        "find_duplicate": {
            "title": "Find the Duplicate Number",
            "difficulty": "Medium",
            "description": "Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive. There is only one repeated number in nums, return this repeated number.",
            "input_format": "nums: List[int]",
            "output_format": "int",
            "example": {
                "input": "nums = [1,3,4,2,2]",
                "output": "2",
                "explanation": "2 is the repeated number in the array."
            },
            "test_cases": [
                {
                    "input": {"nums": [1,3,4,2,2]},
                    "output": 2
                },
                {
                    "input": {"nums": [3,1,3,4,2]},
                    "output": 3
                },
                {
                    "input": {"nums": [1,1]},
                    "output": 1
                }
            ],
            "templates": {
                "python": """def findDuplicate(nums: List[int]) -> int:
    # Write your code here
    pass""",
                "java": """class Solution {
    public int findDuplicate(int[] nums) {
        // Write your code here
        return 0;
    }
}""",
                "cpp": """class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        // Write your code here
        return 0;
    }
};""",
                "javascript": """/**
 * @param {number[]} nums
 * @return {number}
 */
function findDuplicate(nums) {
    // Write your code here
}"""
            }
        }
    },
    "strings": {
        "longest_palindrome": {
            "title": "Longest Palindromic Substring",
            "difficulty": "Medium",
            "description": "Given a string s, return the longest palindromic substring in s.",
            "input_format": "s: str",
            "output_format": "str",
            "example": {
                "input": "s = 'babad'",
                "output": "'bab'",
                "explanation": "'aba' is also a valid answer."
            },
            "test_cases": [
                {
                    "input": {"s": "babad"},
                    "output": "bab"
                },
                {
                    "input": {"s": "cbbd"},
                    "output": "bb"
                },
                {
                    "input": {"s": "a"},
                    "output": "a"
                }
            ],
            "templates": {
                "python": """def longestPalindrome(s: str) -> str:
    # Write your code here
    pass""",
                "java": """class Solution {
    public String longestPalindrome(String s) {
        // Write your code here
        return "";
    }
}""",
                "cpp": """class Solution {
public:
    string longestPalindrome(string s) {
        // Write your code here
        return "";
    }
};""",
                "javascript": """/**
 * @param {string} s
 * @return {string}
 */
function longestPalindrome(s) {
    // Write your code here
}"""
            }
        },
        "valid_parentheses": {
            "title": "Valid Parentheses",
            "difficulty": "Easy",
            "description": "Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.",
            "input_format": "s: str",
            "output_format": "bool",
            "example": {
                "input": "s = '()[]{}'",
                "output": "true",
                "explanation": "The string contains valid parentheses."
            },
            "test_cases": [
                {
                    "input": {"s": "()[]{}"},
                    "output": True
                },
                {
                    "input": {"s": "([)]"},
                    "output": False
                },
                {
                    "input": {"s": "{[]}"},
                    "output": True
                }
            ],
            "templates": {
                "python": """def isValid(s: str) -> bool:
    # Write your code here
    pass""",
                "java": """class Solution {
    public boolean isValid(String s) {
        // Write your code here
        return false;
    }
}""",
                "cpp": """class Solution {
public:
    bool isValid(string s) {
        // Write your code here
        return false;
    }
};""",
                "javascript": """/**
 * @param {string} s
 * @return {boolean}
 */
function isValid(s) {
    // Write your code here
}"""
            }
        },
        "longest_common_prefix": {
            "title": "Longest Common Prefix",
            "difficulty": "Easy",
            "description": "Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string ''.",
            "input_format": "strs: List[str]",
            "output_format": "str",
            "example": {
                "input": "strs = ['flower','flow','flight']",
                "output": "'fl'",
                "explanation": "The longest common prefix is 'fl'."
            },
            "test_cases": [
                {
                    "input": {"strs": ["flower","flow","flight"]},
                    "output": "fl"
                },
                {
                    "input": {"strs": ["dog","racecar","car"]},
                    "output": ""
                },
                {
                    "input": {"strs": ["interspecies","interstellar","interstate"]},
                    "output": "inters"
                }
            ],
            "templates": {
                "python": """def longestCommonPrefix(strs: List[str]) -> str:
    # Write your code here
    pass""",
                "java": """class Solution {
    public String longestCommonPrefix(String[] strs) {
        // Write your code here
        return "";
    }
}""",
                "cpp": """class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        // Write your code here
        return "";
    }
};""",
                "javascript": """/**
 * @param {string[]} strs
 * @return {string}
 */
function longestCommonPrefix(strs) {
    // Write your code here
}"""
            }
        },
        "reverse_words": {
            "title": "Reverse Words in a String",
            "difficulty": "Medium",
            "description": "Given an input string s, reverse the order of the words. A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space. Return a string of the words in reverse order concatenated by a single space.",
            "input_format": "s: str",
            "output_format": "str",
            "example": {
                "input": "s = 'the sky is blue'",
                "output": "'blue is sky the'",
                "explanation": "The words are reversed while maintaining their order."
            },
            "test_cases": [
                {
                    "input": {"s": "the sky is blue"},
                    "output": "blue is sky the"
                },
                {
                    "input": {"s": "  hello world  "},
                    "output": "world hello"
                },
                {
                    "input": {"s": "a good   example"},
                    "output": "example good a"
                }
            ],
            "templates": {
                "python": """def reverseWords(s: str) -> str:
    # Write your code here
    pass""",
                "java": """class Solution {
    public String reverseWords(String s) {
        // Write your code here
        return "";
    }
}""",
                "cpp": """class Solution {
public:
    string reverseWords(string s) {
        // Write your code here
        return "";
    }
};""",
                "javascript": """/**
 * @param {string} s
 * @return {string}
 */
function reverseWords(s) {
    // Write your code here
}"""
            }
        },
        "valid_anagram": {
            "title": "Valid Anagram",
            "difficulty": "Easy",
            "description": "Given two strings s and t, return true if t is an anagram of s, and false otherwise. An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.",
            "input_format": "s: str, t: str",
            "output_format": "bool",
            "example": {
                "input": "s = 'anagram', t = 'nagaram'",
                "output": "true",
                "explanation": "The strings are anagrams of each other."
            },
            "test_cases": [
                {
                    "input": {"s": "anagram", "t": "nagaram"},
                    "output": True
                },
                {
                    "input": {"s": "rat", "t": "car"},
                    "output": False
                },
                {
                    "input": {"s": "listen", "t": "silent"},
                    "output": True
                }
            ],
            "templates": {
                "python": """def isAnagram(s: str, t: str) -> bool:
    # Write your code here
    pass""",
                "java": """class Solution {
    public boolean isAnagram(String s, String t) {
        // Write your code here
        return false;
    }
}""",
                "cpp": """class Solution {
public:
    bool isAnagram(string s, string t) {
        // Write your code here
        return false;
    }
};""",
                "javascript": """/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
function isAnagram(s, t) {
    // Write your code here
}"""
            }
        }
    },
    "backtracking": {
        "n_queens": {
            "title": "N-Queens",
            "difficulty": "Hard",
            "description": "The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other. Given an integer n, return all distinct solutions to the n-queens puzzle.",
            "input_format": "n: int",
            "output_format": "List[List[str]]",
            "example": {
                "input": "n = 4",
                "output": "[[\".Q..\",\"...Q\",\"Q...\",\"..Q.\"],[\"..Q.\",\"Q...\",\"...Q\",\".Q..\"]]",
                "explanation": "There exist two distinct solutions to the 4-queens puzzle."
            },
            "test_cases": [
                {
                    "input": "n = 4",
                    "output": "[[\".Q..\",\"...Q\",\"Q...\",\"..Q.\"],[\"..Q.\",\"Q...\",\"...Q\",\".Q..\"]]"
                },
                {
                    "input": "n = 1",
                    "output": "[[\"Q\"]]"
                }
            ],
            "templates": {
                "python": """def solveNQueens(n: int) -> List[List[str]]:
    # Write your code here
    pass""",
                "java": """class Solution {
    public List<List<String>> solveNQueens(int n) {
        // Write your code here
        return new ArrayList<>();
    }
}""",
                "cpp": """class Solution {
public:
    vector<vector<string>> solveNQueens(int n) {
        // Write your code here
        return {};
    }
};""",
                "javascript": """/**
 * @param {number} n
 * @return {string[][]}
 */
function solveNQueens(n) {
    // Write your code here
}"""
            }
        },
        "permutations": {
            "title": "Permutations",
            "difficulty": "Medium",
            "description": "Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.",
            "input_format": "nums: List[int]",
            "output_format": "List[List[int]]",
            "example": {
                "input": "nums = [1,2,3]",
                "output": "[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]",
                "explanation": "All possible permutations of [1,2,3] are returned."
            },
            "test_cases": [
                {
                    "input": "nums = [1,2,3]",
                    "output": "[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]"
                },
                {
                    "input": "nums = [0,1]",
                    "output": "[[0,1],[1,0]]"
                }
            ],
            "templates": {
                "python": """def permute(nums: List[int]) -> List[List[int]]:
    # Write your code here
    pass""",
                "java": """class Solution {
    public List<List<Integer>> permute(int[] nums) {
        // Write your code here
        return new ArrayList<>();
    }
}""",
                "cpp": """class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        // Write your code here
        return {};
    }
};""",
                "javascript": """/**
 * @param {number[]} nums
 * @return {number[][]}
 */
function permute(nums) {
    // Write your code here
}"""
            }
        }
    },
    "dynamic_programming": {
        "climbing_stairs": {
            "title": "Climbing Stairs",
            "difficulty": "Easy",
            "description": "You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?",
            "input_format": "n: int",
            "output_format": "int",
            "example": {
                "input": "n = 3",
                "output": "3",
                "explanation": "There are three ways to climb to the top: 1. 1 step + 1 step + 1 step, 2. 1 step + 2 steps, 3. 2 steps + 1 step"
            },
            "test_cases": [
                {
                    "input": "n = 3",
                    "output": "3"
                },
                {
                    "input": "n = 2",
                    "output": "2"
                }
            ],
            "templates": {
                "python": """def climbStairs(n: int) -> int:
    # Write your code here
    pass""",
                "java": """class Solution {
    public int climbStairs(int n) {
        // Write your code here
        return 0;
    }
}""",
                "cpp": """class Solution {
public:
    int climbStairs(int n) {
        // Write your code here
        return 0;
    }
};""",
                "javascript": """/**
 * @param {number} n
 * @return {number}
 */
function climbStairs(n) {
    // Write your code here
}"""
            }
        },
        "longest_palindromic_substring": {
            "title": "Longest Palindromic Substring",
            "difficulty": "Medium",
            "description": "Given a string s, return the longest palindromic substring in s.",
            "input_format": "s: str",
            "output_format": "str",
            "example": {
                "input": "s = 'babad'",
                "output": "'bab'",
                "explanation": "'aba' is also a valid answer."
            },
            "test_cases": [
                {
                    "input": "s = 'babad'",
                    "output": "'bab'"
                },
                {
                    "input": "s = 'cbbd'",
                    "output": "'bb'"
                }
            ],
            "templates": {
                "python": """def longestPalindrome(s: str) -> str:
    # Write your code here
    pass""",
                "java": """class Solution {
    public String longestPalindrome(String s) {
        // Write your code here
        return "";
    }
}""",
                "cpp": """class Solution {
public:
    string longestPalindrome(string s) {
        // Write your code here
        return "";
    }
};""",
                "javascript": """/**
 * @param {string} s
 * @return {string}
 */
function longestPalindrome(s) {
    // Write your code here
}"""
            }
        }
    },
    "trees": {
        "binary_tree_level_order": {
            "title": "Binary Tree Level Order Traversal",
            "difficulty": "Medium",
            "description": "Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).",
            "input_format": "root: TreeNode",
            "output_format": "List[List[int]]",
            "example": {
                "input": "root = [3,9,20,null,null,15,7]",
                "output": "[[3],[9,20],[15,7]]",
                "explanation": "Level order traversal: 3, then 9 and 20, then 15 and 7"
            },
            "test_cases": [
                {
                    "input": "root = [3,9,20,null,null,15,7]",
                    "output": "[[3],[9,20],[15,7]]"
                },
                {
                    "input": "root = [1]",
                    "output": "[[1]]"
                }
            ],
            "templates": {
                "python": """def levelOrder(root: TreeNode) -> List[List[int]]:
    # Write your code here
    pass""",
                "java": """class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        // Write your code here
        return new ArrayList<>();
    }
}""",
                "cpp": """class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        // Write your code here
        return {};
    }
};""",
                "javascript": """/**
 * @param {TreeNode} root
 * @return {number[][]}
 */
function levelOrder(root) {
    // Write your code here
}"""
            }
        }
    },
    "linked_lists": {
        "reverse_linked_list": {
            "title": "Reverse Linked List",
            "difficulty": "Easy",
            "description": "Given the head of a singly linked list, reverse the list, and return the reversed list.",
            "input_format": "head: ListNode",
            "output_format": "ListNode",
            "example": {
                "input": "head = [1,2,3,4,5]",
                "output": "[5,4,3,2,1]",
                "explanation": "The linked list is reversed"
            },
            "test_cases": [
                {
                    "input": "head = [1,2,3,4,5]",
                    "output": "[5,4,3,2,1]"
                },
                {
                    "input": "head = [1,2]",
                    "output": "[2,1]"
                }
            ],
            "templates": {
                "python": """def reverseList(head: ListNode) -> ListNode:
    # Write your code here
    pass""",
                "java": """class Solution {
    public ListNode reverseList(ListNode head) {
        // Write your code here
        return null;
    }
}""",
                "cpp": """class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        // Write your code here
        return nullptr;
    }
};""",
                "javascript": """/**
 * @param {ListNode} head
 * @return {ListNode}
 */
function reverseList(head) {
    // Write your code here
}"""
            }
        }
    },
    "stacks_queues": {
        "valid_parentheses": {
            "title": "Valid Parentheses",
            "difficulty": "Easy",
            "description": "Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.",
            "input_format": "s: str",
            "output_format": "bool",
            "example": {
                "input": "s = '()[]{}'",
                "output": "true",
                "explanation": "The string contains valid parentheses"
            },
            "test_cases": [
                {
                    "input": "s = '()[]{}'",
                    "output": "true"
                },
                {
                    "input": "s = '([)]'",
                    "output": "false"
                }
            ],
            "templates": {
                "python": """def isValid(s: str) -> bool:
    # Write your code here
    pass""",
                "java": """class Solution {
    public boolean isValid(String s) {
        // Write your code here
        return false;
    }
}""",
                "cpp": """class Solution {
public:
    bool isValid(string s) {
        // Write your code here
        return false;
    }
};""",
                "javascript": """/**
 * @param {string} s
 * @return {boolean}
 */
function isValid(s) {
    // Write your code here
}"""
            }
        }
    }
} 