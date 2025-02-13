def filter_by_state(info_users: list[dict], state: str = "EXECUTED") -> list[dict]:
    """ Принимает словари и возвращает новый список из переданных значений """
    sort_info_users = []
    for info in info_users:
        if info["state"] == state:
            sort_info_users.append(info)

    return sort_info_users


def sort_by_date(info_dicts: list[dict], sorting_parameter: bool = True) -> list[dict]:
    """ Функция для сортировки полученных значений """
    if sorting_parameter is not True:
        return sorted(info_dicts, key=lambda date: date["date"])
    else:
        return sorted(info_dicts, key=lambda date: date["date"], reverse=sorting_parameter)
