# Add Virtual Column

A small utility to create new columns in a Pandas DataFrame by applying arithmetic operations between existing columns.

---

## How it works

* Pass a DataFrame, an operation string (`"colA + colB"`, `"colX - colY"`, etc.), and the name of the new column.
* The new column name must contain `"label_"`.
* Supports: `+`, `-`, `*`, `/`.
* Returns an empty DataFrame if inputs are invalid.

---

## Example

```python
import pandas as pd
from your_module import add_virtual_column

df = pd.DataFrame({"colA": [1, 2, 3], "colB": [4, 5, 6]})

result = add_virtual_column(df, "colA + colB", "label_sum")

print(result)
```

Output:

```
   colA  colB  label_sum
0     1     4          5
1     2     5          7
2     3     6          9
```

---

## Function

```python
add_virtual_column(df, role, new_column)
```

* **df**: input DataFrame
* **role**: string like `"col1 + col2"`
* **new_column**: must contain `"label_"`
* **returns**: DataFrame with the new column, or empty DataFrame if invalid

---

## Requirements

* Python 3.8+
* pandas
