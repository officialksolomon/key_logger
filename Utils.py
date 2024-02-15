from types import ModuleType
from typing import List


def check_variables_exist(module: ModuleType, variables: List[str]):
    variables_set = set(variables)
    return variables_set.issubset(dir(module))
