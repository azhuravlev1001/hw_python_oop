class InfoMessage:
    """Информационное сообщение о тренировке."""

    def __init__(self,
                 training_type: str,    # имя класса тренировки
                 duration: float,       # длительность тренировки в часах
                 distance: float,
                 # дистанция в километрах
                 # которую преодолел пользователь за время тренировки
                 speed: float,
                 # средняя скорость, с которой двигался пользователь
                 calories: float
                 # количество килокалорий
                 # которое израсходовал пользователь за время тренировки
                 ) -> None:

        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def get_message(self) -> str:

        return (f'Тип тренировки: {self.training_type}; Длительность: '
                f'{self.duration:.3f} ч.; Дистанция: {self.distance:.3f} км; '
                f'Ср. скорость: {self.speed:.3f} км/ч; Потрачено ккал: '
                f'{self.calories:.3f}.')


class Training:
    """Базовый класс тренировки."""

    # атрибут данных (переменная класса),
    # общая для всех экземпляров класса
    # константа для перевода значений из метров в километры
    M_IN_KM = 1000
    # константа для перевода значений из часов в минуты
    HOUR_IN_MIN = 60
    # длина шага или гребка в плавании
    LEN_STEP = 0.65

    def __init__(self,
                 # число шагов при ходьбе и беге либо гребков — при плавании
                 action: int,
                 duration: float,       # длительность тренировки
                 weight: float          # вес спортсмена
                 ) -> None:

        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""

        return (self.action * self.LEN_STEP / self.M_IN_KM)

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""

        # преодоленная_дистанция_за_тренировку / время_тренировки
        return self.get_distance() / self.duration

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""

        training_type: str    # имя класса тренировки
        duration: float       # длительность тренировки в часах
        # дистанция в километрах,
        # которую преодолел пользователь за время тренировки
        distance: float
        # средняя скорость, с которой двигался пользователь
        speed: float
        # количество килокалорий,
        # которое израсходовал пользователь за время тренировки
        calories: float

        training_type = self.__class__.__name__
        duration = self.duration
        distance = self.get_distance()
        speed = self.get_mean_speed()
        calories = self.get_spent_calories()

        return InfoMessage(training_type, duration,
                           distance, speed, calories)


class Running(Training):
    """Тренировка: бег."""

    def __init__(self, action: int,
                 duration: float, weight: float) -> None:
        super().__init__(action, duration, weight)
        super().get_distance()
        super().get_mean_speed()

    def get_spent_calories(self) -> float:

        coeff_calorie_1 = 18
        # параметр 1 для формулы подсчета калорий для бега
        coeff_calorie_2 = 20
        # параметр 2 для формулы подсчета калорий для бега

        # Расход калорий для бега
        return ((coeff_calorie_1 * self.get_mean_speed()
                - coeff_calorie_2) * self.weight / self.M_IN_KM
                * self.duration * self.HOUR_IN_MIN)


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""

    def __init__(self, action: int,
                 duration: float, weight: float,
                 height: float                           # рост спортсмена
                 ) -> None:
        # наследуем функциональность конструктора из класса-родителя
        super().__init__(action, duration, weight)
        super().get_distance()
        super().get_mean_speed()
        # добавляем новую функциональность
        self.height = height
        # дополнительный параметр - рост спортсмена

    def get_spent_calories(self) -> float:

        coeff_calorie_1 = 0.035
        # параметр 1 для формулы подсчета калорий для ходьбы
        coeff_calorie_2 = 0.029
        # параметр 2 для формулы подсчета калорий для ходьбы

        return ((coeff_calorie_1 * self.weight
                + (self.get_mean_speed() ** 2 // self.height)
                * coeff_calorie_2 * self.weight) * self.duration
                * self.HOUR_IN_MIN)


class Swimming(Training):
    """Тренировка: плавание."""
    LEN_STEP = 1.38

    def __init__(self, action: int,
                 duration: float, weight: float,
                 # длина бассейна в метрах
                 length_pool: float,
                 # сколько раз пользователь переплыл бассейн
                 count_pool: int
                 ) -> None:

        # наследуем функциональность конструктора из класса-родителя
        super().__init__(action, duration, weight)
        super().get_distance()
        # добавляем новую функциональность
        self.lenth_pool = length_pool
        self.count_pool = count_pool

    def get_mean_speed(self) -> float:

        return (self.lenth_pool * self.count_pool / self.M_IN_KM
                / self.duration)

    def get_spent_calories(self) -> float:

        coeff_calorie_1 = 1.1
        coeff_calorie_2 = 2

        return ((self.get_mean_speed() + coeff_calorie_1)
                * coeff_calorie_2 * self.weight)


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""

    training: Training

    # словарь, в котором сопоставляются коды тренировок и классы,
    # которые нужно вызвать для каждого типа тренировки
    dictionary = {'SWM': Swimming,
                  'RUN': Running,
                  'WLK': SportsWalking
                  }

    if workout_type == 'SWM':
        training = dictionary[workout_type](data[0],
                                            data[1],
                                            data[2],
                                            data[3],
                                            data[4])
    elif workout_type == 'RUN':
        training = dictionary[workout_type](data[0],
                                            data[1],
                                            data[2])
    elif workout_type == 'WLK':
        training = dictionary[workout_type](data[0],
                                            data[1],
                                            data[2],
                                            data[3])

    return training


def main(training: Training) -> None:
    """Главная функция."""

    info = training.show_training_info()

    print(info.get_message())
    # строка сообщения с данными о тренировке


if __name__ == '__main__':
    packages = [
        ('SWM',      # код тренировки
         [720,       # количество гребков
          1,          # время в часах
          80,         # вес пользователя
          25,         # длина бассейна
          40]         # сколько раз пользователь переплыл бассейн
         ),

        ('RUN',      # код тренировки
         [15000,     # количество шагов
          1,          # время тренировки в часах
          75]         # вес пользователя
         ),

        ('WLK',      # код тренировки
         [9000,      # количество шагов
          1,          # время тренировки в часах
          75,         # вес пользователя
          180]        # рост пользователя
         ),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
