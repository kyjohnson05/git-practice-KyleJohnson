## Fixing and Identifying Bugs 🪲
In program.py, I was able to successfully handle some bugs made in `divide_numbers`, `reverse_string`, and `get_list_element`.

### What were the bugs?
1. For `divide_numbers`,
* `result = a / b` has no handling for division by zero
2. For `reverse_string`,
* `reversed_s = s[::-1]` might not handle non-string input properly
3. For `get_list_element`,
* `if index < len(lst):` is an incorrect boundary check
* `return "Not found"` should probably raise an exception instead

### How did I identify the bugs?
Truthfully speaking, discovering the bugs wasn't too hard as it'd already been noted in the comments, but I did see the test results present a majority of what'd caused each failure in my tests. For instance, in `reverse_string`, I used an integer in my corner case and didn't raise an exception, which included this in my test's report:
> TypeError: 'int' object is not subscriptable.
Likely, even if I didn't see the initial comments, I'd still be able to locate the bugs because of the report.

### What fixes did I use?
1. For `divide_numbers`,
* I raised a `ZeroDivisionError` to handle division by zero
2. For `reverse_string`,
* I raised a `TypeError` to handle non-string input
3. For `get_list_element`,
* I changed `if index < len(lst):` to `if index >= len(lst) or index < 0:` for a correct boundary check
* I removed `return "Not found"` and raised an `IndexError` to properly handle an out-of-range index
