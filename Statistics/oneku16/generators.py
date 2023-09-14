import typing


def get_array(n: int, v: float = .0) -> typing.List[float, ...]:
    return [v] * n


def get_matrix(n: int, m: int, v: float = .0) -> typing.List[typing.List[float, ...]]:
    return [[v] * m for _ in range(n)]



