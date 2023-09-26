

def image_filter(
        original_image: list[list[float, ...], ...],
        mask: list[list[float, ...], ...],
) -> list[list[float, ...], ...]:
    assert mask and len(mask) == len(mask[0]) and len(mask) & 1

    mid = len(mask) >> 1

    for i in range(mid, len(mask) - mid):
        for j in range(mid, len(mask) - mid):
            ...

    return [[]]


def linear_filter(
        original_image: list[list[float, ...], ...],
        filter_size: int = 3,
) -> list[list[float, ...], ...]:
    assert filter_size & 1
    N, M, mid = len(original_image), len(next(iter(original_image))), filter_size // 2
    filtered_image = [[0 for _ in range(M)] for _ in range(N)]

    def apply(i_, j_):
        for x in range(i_ - mid, i_ + mid):
            for y in range(j_ - mid, j_ + mid):
                filtered_image[i_][j_] += original_image[x][y]

    for i in range(mid, N - mid):
        for j in range(mid, M - mid):
            apply(i_=i, j_=j)

    return filtered_image



