import operator
import pandas as pd

# Mapping of supported arithmetic operators to their corresponding Python functions
ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}


def add_virtual_column(df: pd.DataFrame, role: str, new_column: str) -> pd.DataFrame:
    # Ensure the new column name follows the naming convention (must contain "label_")
    if "label_" not in new_column:
        return pd.DataFrame([])

    col_1 = col_2 = oper = ""

    # Detect which operator is used in the role string
    for op in ops.keys():
        if op in role:
            parts = role.split(op)

            # The role string must contain exactly two operands
            if len(parts) != 2:
                return pd.DataFrame([])

            col_1, col_2 = [part.strip() for part in parts]  # Remove extra spaces
            oper = op
            break

    # Validate that both referenced columns exist in the DataFrame
    columns = df.columns.tolist()
    if col_1 not in columns or col_2 not in columns:
        return pd.DataFrame([])

    # Create a copy of the DataFrame and add the computed column
    df_result = df.copy()
    df_result[new_column] = ops[oper](df_result[col_1], df_result[col_2])

    return df_result
