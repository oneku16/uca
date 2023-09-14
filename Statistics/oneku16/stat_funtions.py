from typing import List


def mean(sequence: List[float, ...]) -> float:
    assert isinstance(sequence, List)
    return sum(sequence) / len(sequence)


def std(sequence: List[float, ...], *, power: float = 2.) -> float:
    assert isinstance(sequence, List)
    _mean = mean(sequence=sequence)
    _squared = sum((v - _mean) ** power for v in sequence)
    _std = (_squared / (len(sequence) - 1)) ** (1/power)
    return _std


def describe(sequence: List[float, ...]) -> str:
    size = len(sequence)
    _mean = mean(sequence)
    _std = std(sequence)
    MIN = min(sequence)
    _25 = None
    _50 = None
    _75 = None
    MAX = max(sequence)

    return (f'{size=}\n'
            f'mean={_mean}\n'
            f'std={_std}')
