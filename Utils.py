from types import ModuleType
from typing import List


def check_variables_exist(module: ModuleType, variables: List[str]):
    variables_set = set(variables)
    variables_subset = variables_set.issubset(dir(module))
    return variables_subset
