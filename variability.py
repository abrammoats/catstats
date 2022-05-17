import pandas as pd

def cat_variation(data: pd.DataFrame,
                  colName: str) -> float:
    """
    This function produces a measure of variability on a set of categorical data
    contained in a DataFrame column. It follows the work of Kader and Perry,
    which can be found here: https://doi.org/10.1080/10691898.2007.11889465.

    Values closer to 1 indicate low variability, whereas a value of 0 indicates
    absolute variability.

    This function seeks to assist the user in analyzing their categorical data.

    ****WARNING*******
    All columns are treated as categorical, regardless of what type of data is
    contained. Future updates will hopefully fix this problem.

    Inputs
    -----------------------
    data: pd.DataFrame
    Dataframe that contains data you wish to analyze

    colName: str
    Name of specific column you wish to analyze

    Outputs
    -----------------------

    The "variation" of a column in a pandas DataFrame, treating the column values
    as categories
    """

    prepped = data[colName].apply(lambda x: str(x))

    similarity_count = 0

    for i in prepped.index:
        for j in prepped.index:
            if prepped[i] != prepped[j]:
                similarity_count = similarity_count + 1

    return similarity_count/(len(prepped)**2-len(prepped))
