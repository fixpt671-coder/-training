from time import sleep

class User:
    def __init__(self, nickname: str, password: str, age: int):
        self.nickname = nickname
        self.age = age
        self.password = hash(password)

    def __str__(self):
        return self.nickname
class Video:
    def __init__(self, title: str, duration: int, adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

class UrTube:
    users:list[User] = []
    videos: list[Video] = []
    current_user: User = None
    def log_in(self, nickname: str, password: str):
        for user in self.users:
            if nickname == user.nickname:
                if user.password == hash(password):
                    self.current_user = user
                return True
        return False

    def register(self, nickname: str, password: str, age: int):
        if self.log_in(nickname, password):
            print(f"Пользователь {nickname} уже существует")
        else:
            self.users.append(User(nickname, password, age))
            self.log_in(nickname, password)

    def log_out(self):
        self.current_user = None

    def add(self, *video: Video):
        for v in video:
            if not(v in self.videos):
                self.videos.append(v)

    def get_videos(self, search_name):
        search_name = str(search_name)
        return [name.title for name in self.videos if search_name.lower() in name.title.lower()]

    def watch_video(self, name):
        name = str(name)
        if self.current_user == None:
            print("Войдите в профиль, чтобы смотреть видео")
        else:
            for video in self.videos:
                if name == video.title:
                    if video.adult_mode == False or self.current_user.age >= 18:
                        while video.duration >= video.time_now:
                            print(video.time_now, end = ' ')
                            sleep(1)
                            video.time_now += 1
                        video.time_now = 0
                        print("Конец видео")
                        break
                    else:
                        print("Повзрослейте, чтобы смотреть данное видео!:)")
                        break

if __name__ == "__main__":
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    print(ur.users[0].nickname)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    print(ur.current_user.nickname)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')