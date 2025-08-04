questions = {'Сколько планет в солнечной системе': '8', 'Столица франции':'Париж'}

score = 0

for q, a in questions.items():
    user_ansver = input(q + ' ')
    if user_ansver.lower() == a.lower():
        print('Вернор!')
        score +=1
    else:
        print('Неверно!')

print(f'Ваш результат: {score} из {len(questions)}')