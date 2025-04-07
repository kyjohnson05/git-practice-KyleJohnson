# Static and Dynamic Code Analysis Report
 
## Static Analysis
 
**flake8**:
- Line 1: unused import `math` (removed)
- Line 3: unused import `random` (removed)
 
**pylint**:
- Function `slow_func` could be simplified (rewritten with list comprehension)
- `unused_function` never used (removed)
 
## Line Profiling
 
Bottleneck found in:
- `expensive_op`: Took ~3s for 1000 calls
 
### Fix:
- Replaced loop with arithmetic formula
 
## Code Coverage
 
- Coverage before: ~62%
- Coverage after: ~71%
- `unused_function()` was not covered, removed
 
## Fix Summary
 
- Removed unused imports and functions
- Rewrote `expensive_op` using a math formula
- Rewrote `slow_func` using list comprehension
- Confirmed coverage and performance improvements
