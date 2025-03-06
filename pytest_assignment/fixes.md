## Fixing and Identifying Bugs 🪲
In program.py, I was able to successfully handle some bugs made in `divide_numbers`, `reverse_string`, and `get_list_element`.

### What were the bugs?
1. For `divide_numbers`,
* No handling for division by zero
2. For `reverse_string`,
* Might not handle non-string input properly
3. For `get_list_element`,
* Incorrect boundary check
* Should probably raise an exception instead

### How did I identify the bugs?
Truthfully speaking, discovering the bugs wasn't too hard as it'd already been noted in the comments, but I did see the test results present a majority of what'd caused each failure in my tests. For instance, in `reverse_string`, I used an integer in my corner case and didn't raise an exception, which included this in my test's report, "TypeError: 'int' object is not subscriptable". Likely, even if I didn't see the initial comments, I'd still be able to locate the bugs because of the report.

### What fixes did I use?
