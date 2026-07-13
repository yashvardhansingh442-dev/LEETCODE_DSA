12. Integer to Roman
Problem
Given integer num, convert it to a Roman numeral.
Symbols:
SymbolValueI1V5X10L50C100D500M1000
Rules:

Decimal place value ko highest se lowest tak convert karke append karo.
Agar place value 4 ya 9 se start nahi hoti → max symbol jo subtract ho sake wo append karo, uski value subtract karo, remainder ko recursively convert karo.
Agar 4 ya 9 se start hoti hai → subtractive form use karo. Sirf ye 6 allowed hain: 4→IV, 9→IX, 40→XL, 90→XC, 400→CD, 900→CM.
Powers of 10 (I, X, C, M) max 3 baar consecutively repeat ho sakte hain. V, L, D kabhi repeat nahi hote — agar 4x chahiye to subtractive form use hoga.

Examples
Example 1:
Input: num = 3749
Output: "MMMDCCXLIX"
3000 → MMM
 700 → DCC
  40 → XL
   9 → IX
Example 2:
Input: num = 58
Output: "LVIII"
50 → L
 8 → VIII
Example 3:
Input: num = 1994
Output: "MCMXCIV"
1000 → M
 900 → CM
  90 → XC
   4 → IV
Constraints

1 <= num <= 3999
