# Self-intersection numbers of arcs
- The main function is `intersection.py`: 
  - Input: a word `w=n_1 x_1 ... x_k n_2`
  - Output: the self-intersection number of `w`
- Note: surface word for a pair of pants: `a1A3b2B3`

### Example Usage:


```python
my_word = '1baBA2'  # Sample input
print("Self-intersection number:", intersection(my_word))  # Output the result
```

### Procedure:

- **Initialize** the intersection counter and set up index segments.

- **Loop through all pairs of index segments `(i, j), i<j`** to check if they intersect based on the following conditions:
    - If two index segments intersect immediately in their current domain.
    - If the index segments have matching start and end letters.
    - If the index segments have the same start or end letters but differ in the other.
    - If the start of one index segment matches the end of the other, and vice versa.

#### 8 Intersection Cases for Index Segment Pairs `(i, j)`:

1. **Immediate Intersection**: 
   - Two index segments intersect immediately in their current domain.

2. **No Intersection**: 
   - If the index segments do not intersect, no further checks are performed.

3. **Matching Start and End Letters**: 
   - The start and end letters of two index segments match. The function performs both:
     - A **forward check**, advancing to the next index segments until the end letters differ.
     - A **backward check**, moving to the previous index segments until the start letters differ.

4. **Same Start, Different End**: 
   - The index segments start with the same letter but end with different ones. The function performs:
     - A **backward check**, moving to the previous index segments until the start letters differ.

5. **Different Start, Same End**: 
   - The index segments have different start letters but the same end letter. The function performs:
     - A **forward check**, advancing to the next index segments until the end letters differ.

6. **Start i = End j, End i = Start j**: 
   - The start of index segment `i` matches the end of index segment `j`, and the end of index segment `i` matches the start of index segment `j`. The function performs:
     - A **backward check** on index segment `i` while performing a **forward check** on index segment `j` until their letters no longer match.
     - A **forward check** on index segment `i` while performing a **backward check** on index segment `j` until their letters no longer match.

7. **Start i = End j, End i ≠ Start j**: 
   - The start of index segment `i` matches the end of index segment `j`, but the end of index segment `i` doesn't match the start of index segment `j`. The function performs:
     - A **backward check** on index segment `i` while performing a **forward check** on index segment `j`.

8. **Start i ≠ End j, End i = Start j**: 
   - The start of index segment `i` doesn't match the end of index segment `j`, but the end of index segment `i` matches the start of index segment `j`. The function performs:
     - A **forward check** on index segment `i` while performing a **backward check** on index segment `j`.

