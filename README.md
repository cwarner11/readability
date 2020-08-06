### Specification:

Design and implement a program, readability, that computes the Coleman-Liau index of the text.

Implement the program in a file called readability.py
The program must prompt the user for a string of text (using get_string).
The program should count the number of letters, words, and sentences in the text. One may assume that a letter is any lowercase character from a to z or any uppercase character from A to Z, any sequence of characters separated by spaces should count as a word, and that any occurrence of a period, exclamation point, or question mark indicates the end of a sentence.
The program should print as output "Grade X" where X is the grade level computed by the Coleman-Liau formula, rounded to the nearest integer.
If the resulting index number is 16 or higher (equivalent to or greater than a senior undergraduate reading level), the program should output "Grade 16+" instead of giving the exact index number. If the index number is less than 1, the program should output "Before Grade 1".
