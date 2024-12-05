team1_num = 5
score_1 = 40
team1_time = 18015.2

team2_num = 6
score_2 = 42
team2_time = 18015.2

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = "Победа команды Мастера кода!"
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = "Победа команды Волшебники Данных!"
else:
    result = "Ничья!"

task_total = score_1 + score_2
time_avg = (team1_time + team2_time)/task_total

print("В команде Мастера кода %d" %team1_num)
print("Итого сегодня в командах участников: %d и %d" %(team1_num, team2_num))
print("Команда Волшебники данных решила задач: {}".format(score_2))
print("Волшебники данных решили задачи за {} с!".format(team2_time))
print(f"Команды решили {score_1} и {score_2} задач")
print(f"Результат битвы: {result}")
print(f"Сегодня было решено {task_total} задач, в среднем по {time_avg:.2f} секунд на задачу!")