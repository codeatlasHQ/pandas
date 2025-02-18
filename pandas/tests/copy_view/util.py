from pandas.core.arrays import BaseMaskedArray


def get_array(df, col):
    """
    Helper method to get array for a DataFrame column.

    Equivalent of df[col].values, but without going through normal getitem,
    which triggers tracking references / CoW (and we might be testing that
    this is done by some other operation).
    """
    icol = df.columns.get_loc(col)
    assert isinstance(icol, int)
    arr = df._get_column_array(icol)
    if isinstance(arr, BaseMaskedArray):
        return arr._data
    return arr
