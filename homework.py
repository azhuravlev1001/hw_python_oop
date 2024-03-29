from dataclasses import dataclass


@dataclass
class InfoMessage:
    """Информационное сообщение о тренировке."""
    MES_TEMPL = ('Тип тренировки: {0}; Длительность: {1:.3f} ч.; '
                 'Дистанция: {2:.3f} км; Ср. скорость: {3:.3f} км/ч; '
                 'Потрачено ккал: {4:.3f}.')
    training_type: str
    duration: float
    distance: float
    speed: float
    calories: float

    def get_message(self) -> str:
        return self.MES_TEMPL.format(self.training_type, self.duration,
                                     self.distance, self.speed, self.calories)


class Training:
    """Базовый класс тренировки."""
    M_IN_KM: int = 1000
    HOUR_IN_MIN: int = 60
    LEN_STEP: float = 0.65

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float
                 ) -> None:

        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        return (self.action * self.LEN_STEP / self.M_IN_KM)

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        return self.get_distance() / self.duration

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        raise NotImplementedError

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return InfoMessage(self.__class__.__name__, self.duration,
                           self.get_distance(), self.get_mean_speed(),
                           self.get_spent_calories())


class Running(Training):
    """Тренировка: бег."""
    coeff_calorie_1: int = 18
    coeff_calorie_2: int = 20

    def get_spent_calories(self) -> float:
        return ((self.coeff_calorie_1 * self.get_mean_speed()
                - self.coeff_calorie_2) * self.weight / self.M_IN_KM
                * self.duration * self.HOUR_IN_MIN)


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    coeff_calorie_1: float = 0.035
    coeff_calorie_2: float = 0.029

    def __init__(self, action: int,
                 duration: float, weight: float,
                 height: float
                 ) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self) -> float:
        return ((self.coeff_calorie_1 * self.weight
                + (self.get_mean_speed() ** 2 // self.height)
                * self.coeff_calorie_2 * self.weight) * self.duration
                * self.HOUR_IN_MIN)


class Swimming(Training):
    """Тренировка: плавание."""
    LEN_STEP: float = 1.38
    coeff_calorie_1: float = 1.1
    coeff_calorie_2: float = 2

    def __init__(self, action: int,
                 duration: float, weight: float,
                 length_pool: float,
                 count_pool: int
                 ) -> None:
        super().__init__(action, duration, weight)
        self.lenth_pool = length_pool
        self.count_pool = count_pool

    def get_mean_speed(self) -> float:
        return (self.lenth_pool * self.count_pool / self.M_IN_KM
                / self.duration)

    def get_spent_calories(self) -> float:
        return ((self.get_mean_speed() + self.coeff_calorie_1)
                * self.coeff_calorie_2 * self.weight)


def read_package(workout_type_mapping: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    dictionary = {'SWM': Swimming,
                  'RUN': Running,
                  'WLK': SportsWalking}
    return dictionary[workout_type_mapping](*data)


def main(training: Training) -> None:
    """Главная функция."""
    info = training.show_training_info()

    print(info.get_message())


if __name__ == '__main__':
    packages = [('SWM', [720, 1, 80, 25, 40]),
                ('RUN', [15000, 1, 75]),
                ('WLK', [9000, 1, 75, 180])]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
