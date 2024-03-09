def AddCategoryData(arr: list[list[any]], category, data: list[str], list: list[str]):
    if not(category in list):
        raise ValueError("category error!: " + category)
    
    categoryIdx = list.index(category)

    arr[categoryIdx].extend(data)