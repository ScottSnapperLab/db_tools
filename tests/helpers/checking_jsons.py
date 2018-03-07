import pandas as pd


def sort_columns(df):
    return df.T.sort_index().T.sort_index()


def check_json_string(df, json_str):
    df = sort_columns(df)
    cloned_df = sort_columns(pd.read_json(json_str))
    return df.equals(cloned_df)


def check_and_write_json(df, path=None, reset_index=False):
    if reset_index:
        df = df.reset_index()

    json_str = df.to_json()

    if not check_json_string(df=df, json_str=json_str):
        raise ValueError("check_json_string returned `False`.")

    if path is None:
        return json_str
    else:
        with path.open(mode='w') as out:
            out.write(json_str)
