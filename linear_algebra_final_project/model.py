from typing import Tuple, List


class Model:
    __slots__ = ('__independent_values', '__dependent_values', '__slope',
                 '__intercept', '__x_mean', '__y_mean',
                 '__x_sum', '__y_sum')

    def __init__(self, x_values: List[float], y_values: List[float]):
        self.__independent_values = x_values
        self.__dependent_values = y_values
        self.__x_sum = sum(x_values)
        self.__y_sum = sum(y_values)
        self.__x_mean, self.__y_mean = self.__get_means()
        self.__slope, self.__intercept = self.super_setter()

    def outliers(self, x_values, y_values) -> Tuple[int, int, int]:
        x_sum = y_sum = xy_sum = 0
        N = len(x_values)
        for x, y in zip(x_values, y_values):
            x_sum += x ** 2
            y_sum += y ** 2
            xy_sum += x * y
        R = (N * self.__x_mean - self.__y_mean - xy_sum) / ((N * x_sum - self.__x_sum ** 2) ** .5 * (N * y_sum - self.__y_sum ** 2) ** .5)
        ...

    @staticmethod
    def standard_deviation(array: List[float]) -> float:
        N = len(array)
        if N <= 1:
            return .0
        mean = sum(array) / N
        variance = (sum((x - mean) ** 2 for x in array) / (N - 1)) ** .5
        return variance

    @property
    def slope(self):
        return self.__slope

    @property
    def intercept(self):
        return self.__intercept

    @property
    def x_mean(self):
        return self.__x_mean

    @property
    def y_mean(self):
        return self.__y_mean

    @property
    def x_sum(self):
        return self.__x_sum

    @property
    def y_sum(self):
        return self.__y_sum

    def __get_means(self) -> Tuple[float, float]:
        return self.__x_sum / len(self.__independent_values), self.__y_sum / len(self.__dependent_values)

    def super_setter(self) -> Tuple[float, float]:

        numerator = denominator = 0
        difference = lambda a, b: a - b

        for x, y in zip(self.__independent_values, self.__dependent_values):
            numerator += difference(x, self.__x_mean) * difference(y, self.__y_mean)
            denominator += difference(x, self.__x_mean) ** 2

        return numerator / denominator, difference(self.__y_mean, numerator / denominator * self.__x_mean)
