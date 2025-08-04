import time

questions = {'Сколько планет в солнечной системе': '8', 'Столица франции':'Париж'}

score = 0

for q, a in questions.items():
    start_time = time.time()
    user_ansver = input(q + ' ')
    end_time = time.time()
    if round(end_time - start_time, 1) > 5:
        print('Вы неуложились в таймер 5 секунд!')
        user_ansver = 'wrong'

    print(f'Время ответа: {round(end_time - start_time, 1)} сек.')
    if user_ansver.lower() == a.lower():
        print('Вернор!')
        score +=1
    else:
        print('Неверно!')

print(f'Ваш результат: {score} из {len(questions)}')