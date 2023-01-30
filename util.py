def get_unique_values_from_column(dataframe, column_name, separator):
    collection = set()
    for column_value in dataframe[column_name]:
        values = str(column_value).split(separator)
        collection.update(values)
    result = []
    for value in collection:
        result.append(str.strip(value))
    return result


