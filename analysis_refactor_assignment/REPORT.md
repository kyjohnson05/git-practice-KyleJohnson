# Static and Dynamic Code Analysis Report
 
## Static Analysis
 
**flake8**:
- Line 1: unused import `math`
- Line 3: unused import `random`
 
**pylint**:
- Function `slow_func` could be simplified
- `unused_function` never used
 
## Line Profiling
 
Bottleneck found in:
- `expensive_op`: Took ~3s for 1000 calls
 
### Fix:
- Replaced loop with arithmetic formula
- Also tested with `lru_cache` — significant speedup
 
## Code Coverage
 
- Coverage before: ~60%
- Coverage after: ~85%
- `unused_function()` was not covered, removed
 
## Fix Summary
 
- Removed dead code and unused imports
- Rewrote `expensive_op` using a math formula
- Simplified loop using list comprehension
- Confirmed coverage and performance improvements
