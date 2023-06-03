# kings = ['генрих', 'фридрих', 'людвиг', 'ричард']
# pos = 2
# print(kings[pos])
# pos += 1
# print(kings[pos])

# #срез подсписок внутри списка !!!до
# drinks = ['пиво','чай','кофе','водка']
# print(drinks[1:3])


# terms = ['MVP','Маржинальность','Гипотеза','Деплой','ROI','IDE','Python']
# #term_en = terms[0:1] + terms[4:]
# terms_en = [terms[0]] + terms[4:]
# terms_ru = terms[1:4]

# print(terms)
# print(terms_en)
# print(terms_ru)

# #перебор и условия

# ex_gfs = ['Иветта', 'Лизетта', 'Мюзетта', 'Жанетта', 'Жоржетта']
# for ex in ex_gfs:
#     print(ex)
    
# print('покуда я с Вами - клянусь, моя песня не спета')

# reasons = ['ты', 'все твои мечты', 'боль']
# num = 1

# for reason in reasons:
#     print([f'{num} причина - это {reason}'])
#     num += 1
    
# #цикл и условие можно совмещать
# words = ["вероника","лавировали","тележка","маленький"]

# for word in words:
#     if "p" in word:
#         print(f"{word} - картавое слово")
        
    
# expenses = [200, 450, 320, 1100, 280, 325]
# total = 0
# for payment in expenses:
#     total += payment
# print(f'Всего потрачено: {total}')
    
# medals = ["gold", "silver", "gold", "silver", "bronze", "silver", "gold","silver", "gold","gold", "chocolate", "gold"]
# gold_count = 0 
# silver_count = 0 
# bronze_count = 0 
# chocolate_count = 0 

# for medal in medals:
#     if medal == 'gold':
#         gold_count += 1
#     elif medal == 'silver':
#         silver_count += 1
#     elif medal == 'bronze':
#         bronze_count += 1
#     elif medal == 'chocolate':
#         chocolate_count += 1
        
        
# print (f'золотых: {gold_count}')
# print (f'серебрянных: {silver_count}')
# print (f'бронзовых: {bronze_count}')
# print (f'шоколадных: {chocolate_count}')

# answer = None

# while answer != 'пошли':
#     answer = input ("пошли тусить?  ")
# print ("я знала, что ты согласишься!")

# num = 4 
# is_solved = False # булева переменна 

# while not is_solved:
#     ans = input ("угадай число ")
#     if int (ans) == num:
#         print ('угадал!')
#         is_solved = True 
#     else:
#         print("неа")


# num = 4 

# while True:
#     ans = input ("угадай число ")
#     if int (ans) == num:
#         print ('угадал!')
#         break
#     else:
#         print("неа")

# cities = ["ривенделл", "минас-тирит", "эребор", "шир"]
# for city in cities:
#     if city == "эребор":
#         print ('ну это уже эребор')
#         break
#     else:
#         print(city)
        
# #ривенделл
# # минас-тирит
# # ну это уже эребор



#while

# debt = 10000
# while debt > 0:
#     print(f"Ваш долг -  {debt}")
#     payment = int (input('введите сумму для погашения: '))
#     debt -= payment
# print('ваши долги выплачены')

# # Range 
# for num in range (1, 6):
#     print ("смеяться 1 минуту" )

# # верхняя граница 
# for num in range (10):
#     print(f"{num} * 9 = {num * 9}")
    
# # можно перебирать индексы 
# actions = ['buy it', 'use it', 'break it', 'fix it']
# #action_indexes = range(4)

# action_indexes = range(len(actions))

# for act_idx in action_indexes:
#     print(act_idx + 1, actions[act_idx])

# price = int (input("Введите полную сумму покупки "))
# for month in range(1, 13):
#     monthly_payment = int(price / month)
#     print(f'{month} месяцев - {monthly_payment} руб')


# #инвертировать список 
# print(letters[::-1])

# words = ['ром','кола','виски','вино','вода','ок','пиво','коньяк','ель', 'ром','кола','виски','вино','вода','ок','пиво','коньяк','ель']
# found = None

# for word in words:
#     if len(word) == 2:
#         found = word
#         break
# print(found)




#weather = (4,5,5,3,5,7,5,7,4,8,5,8,6,5,9,6,4,5,5,7,8,11,6,7,11,9,7,8,6,7, 8)
#date = int ( input ( " Введите день: " ) )
#print (weather [date -1])


#Новые данные в список можно добавить методом append.
#brhd_ring = ["Арагорн", "Фродо", "Гондальф", "Гимли"]
#brhd_ring.append("Леголас") 
#print(brhd_ring)

# shopping_list = [ "яблоки","молоко"]
# destination = input ( "Куда пойдем? ")

# if destination == "пикник":
#     #shopping_list.append ("шашлык")
#     #shopping_list.append("дрова")
#     shopping_list.extend(["шашлык", "дрова" ]) 
# elif destination == "в гости":
#     shopping_list.append ("вино")
#     shopping_list.append ("торт" )
# elif destination == "никуда":
#     shopping_list.append( "мороженое" )
#     shopping_list.append( "попкорн" )
# else:
#     print("Не знаю такого места" )

# print (f"Ваш список покупок: {len (shopping_list)} товара, {shopping_list}" )


#Индексы и срезы 
# kings = ['Генрих', 'Людовик', 'Фридрих', 'Ричард']
# pos = 0
# print(kings[pos])
# pos += 1
# print(kings[pos])

# terms = ["MVP", "Маржинальность" , "Гипотеза" , "Деплой", "ROI", "IDE", "Python"]
# terms_en = terms [0:1] + terms [4:]
# terms_ru = terms [1:4]
# print(terms)
# print(terms_en)
# print(terms_ru)

# my_list = [1,2,1,2,2,1]
# for element in my_list:
#     if element == 1:
#         print ("Это единичка")
#     else:
#         print ("Это не единичка")


# HW__1 Привстствуем пользоватсля.
# print('Привет! Предлагаю проверить свои знания английского! ') 
# user_name = input("Расскажи как тебя зовут")
# print (f'Привет, {user_name}, начинаем тренировку! ')

# correct_answers = 0
# # Первый вопрос.
# first_question = 'My name___Lily\n'
# first_answer= 'is'
# user_answer = input(first_question)
# if user_answer == first_answer:
#     correct_answers += 1
#     print ('Ответ верный! \п Вы получаете 10 баллов! ')
# else:
#     print(f'Неправильно. Правильный ответ: {first_answer}')
    
# # Второй вопрос.
# second_question = 'I___coder\n'
# second_answer = 'am'
# user_answer = input(second_question)
# if user_answer == second_answer:
#     correct_answers += 1
#     print (' Ответ верный! Вы получаете 10 баллов!')
# else:
#     print (f'Неправильно. Правильный ответ: {second_answer}')
    
    
# # Третий вопрос.
# third_question = 'I live___Moscow\n'
# third_answer = 'in'
# user_answer = input(third_question)
# if user_answer == third_answer:
#     correct_answers += 1
#     print (' Ответ верный! Вы получаете 10 баллов!')
# else:
#     print (f'Неправильно. Правильный ответ: {third_answer}')
    
# #Количество баллов пользователя.
# user_score = correct_answers * 10
# # Количество процентов.
# user_percentage = round((correct_answers / 3) * 100, 2)
# # 2 знака после запятой

# print(
#     f'Boт и все, {user_name} ! \n'
#     f'Вы ответили на {correct_answers} вопросов из 3 верно. \n' 
#     f'Вы заработали {user_score} баллов. \n' 
#     f'Это {user_percentage} процентов'
# )


# range 

# letters = "a", "b","c","d","e","f","g"
# start = 0
# stop = len(letters)
# print (stop)
# print("---")
# for i in range (start, stop):
#     print(i, letters[i])
    
# # обратный 

# letters = "a","b","c","d","e","f","g"
# start = 0
# stop = len(letters)
# print (stop)
# print("---")
# for i in range (stop -1, start -1, -1):
#     print(i, letters[i])
    
    
# # инвертированный список 
# letters = "a","b","c","d","e","f","g"
# print(letters[::-1])


# while True:
#     print('Введите число 2')
#     user_input = input()
#     if user_input != "2":
#         print('Вы не ввели два')
#     else:
#         print('Вы не ввели два, но мы все равно выйдем из цикла')
#         break


# # HW__3 

# questions = ("My nane__Lily", "I__a coder", "i live__Pskov")
# answers = ['is', 'am', 'in']
# correct_count = 0
# incorrect_count = 0 

# print ("Привет! Предлагаю проверить свом знания английского!") 
# print ("Наберите \'ready\", чтобы начать!")
# user_input = input()
# if user_input != "ready":
#     print("Кажется, вы не хотите играть. Очень жаль")
# else:
    
#     for i in range(len(questions)):
   
#         question_text = questions[i]
#         answer_text = answers[i]
   
#         print(question_text)
        
#         user_input = input()
    
#         if user_input == answer_text:
#             print ("Ответ верный")
#             correct_count += 1
#         else:
#             print(f"Неправильно. Правильный ответ: {answer_text}")
#             incorrect_count +=1
            
#     questions_total = len(questions)
#     correct_percent = round(correct_count/questions_total * 100)
    
#     print(f"Вывести Вот и все! Вы ответили на {correct_count} вопросов"
#         f"из {questions_total} верно, "
#         f"это {correct_percent} процентов."
#         f"")


# weekdays = ["пн", "вт", "ср", "чт", "пт", "сб", "вс"]
# work = [True, True, True, True, True, False, False]
# plans = ["за покупкоми", "отдыхать", "играть","лениться", "гулять", "кутить", "страдать"]

# for i in range(7):
    
#     day = weekdays[i]
#     plan = plans[i]
    
#     if work[i]:
#         daytype= "рабочий"
#     else:
#         wework = "выходной"
#     print(f"{day} - это {daytype} день, а вечером {plan}")


# 4 урок строки и перебор строк 

# string = 'Мама, я графоман, спасити!'
# letters_count = 0
# words_count = 0
# spaces_count = 0

# for letter in string:
#     if letter not in [',' , ' ', '!']:
#         letters_count += 1 
#     elif letter == ' ':
#         spaces_count += 1

# if spaces_count > 0:
#     words_count = spaces_count + 1
# elif letters_count > 0:
#     words_count = 1
    
# print(f"Букв: {letters_count}")
# print(f"Количество слов: {words_count}")


# email ='my new mail@gmail.com'
# new_email = email.replace(' ', '_')
# print (new_email)

# my_str = "Кукушка кукушонку купила джинсы. Надел кукушонок джинсы, Как в капюшоне он смешон!"
# my_str = my_str.replace('джинсы','капюшон')
# print (my_str)


# упоминания и хештеги 
# message = """
# Всем привет, кто пришел изучать #питон и добро пожаловать в чат!
# Будем тут общаться, учиться, делать приложения вместе с @happysnake, @angrycoder @mewton
# """

# people_mentioned = []
# tags_mentioned = []
# text = message.replace(',', '')
# words = text.split(' ')
# for word in words:
#     if word.startswith('#'):
#         tags_mentioned.append(word)
#     elif word.startswith('@'):
#         people_mentioned.append (word)
        
# people_mentioned_joined = " ".join(people_mentioned)
# tags_mentioned_joined = " ".join(tags_mentioned)
# print (f"Упомянуты люди: {people_mentioned_joined}")
# print (f"Упомянуты теги: {tags_mentioned_joined}")


#создание и изменение словарей 
# dictionary = {
#     "cat": "Кошка",
#     "dog": "Собака",
#     "owl" : "Сов"
# }
# word = input ( "Введите слово: " )
# if word not in dictionary:
#     print ( "Не знаю таких слов")
# else:
#     translation = dictionary[word]
#     print (f"Перевод: {translation}")


# store = {
#     "яблоки": 100,
#     "груши": 200,
#     "ананасы" : 300,
# }

# fruit = input ( "Выберите фрукт: ") 
# weight = int (input ("Вес в граммах: "))
# price = store[fruit] * weight / 1000
# print(f"Стоимость: {price}")

# ключ значение 
# guests = {
#     "Алексей" : 500,
#     "Василиса": 1200,
#     "Олег": 950,
#     "Лаша" : 8000,
# }
# guests_names = ', '.join(guests.keys())
# print (f"Гости: {guests_names}")
# total = 0
# for sum in guests.values():
#     total += sum
# print (f"Сумма: {total}")

# HW_4

# words_easy = {"cat": "котенка", "dog": "собаня","owl": "совунья"}
# words_medium = {"river": "речка", "mirror":"зеркало", "divide":"разделять"}
# words_hard = {"usual": "обычный","library":"библиотека","execute":"выполнять"}

# levels = {
#     0:"Нулевой",
#     1:"Так себе",
#     2:"Можно лучше",
#     3:"Норм",
#     4:"Хорошо",
#     5:"Отлично",
# }

# answers = {}

# print ("Выберите уровень сложности")
# print("Лёгкий, средний, сложный")

# user_answer = input().lower()

# if user_answer == "средний":
#     words = words_medium
# elif user_answer == "сложный":
#     words = words_hard
# else:
#     words = words_easy
    
# words_count = len(words)

# print(f"Выбран уровень сложности, мы предложим {words_count} слова, подберите перевод ")
# for word_en, word_ru in words.items():

#     input("Нажмите Enter")
    
#     letter_count = len(word_ru)
#     first_letter = word_ru[0]

#     print(f"{word_en}, {letter_count} букв, начинается на {first_letter}...")

#     user_answer = input().lower()

#     if user_answer == word_ru:
#         print(f"Верно, {word_en.title()} это {word_ru}")
#         answers[word_en] = True
#     else:
#         print (f"Неверно, {word_en.title()} это {word_ru}")
#         answers[word_en] = False

# correct_words = []
# incorrect_words = []


# for word_en, is_correct in answers.items():
#     if is_correct:
#         correct_words.append(word_en)
#     else:
#         incorrect_words.append(word_en)
        
        

# print("Правильно отвечены слова: ")
# print("\n".join(correct_words))
# print("Неправильно отвечены слова:")
# print("\n".join(incorrect_words))


# correct_count = len(correct_words)

# if correct_count in levels:
#     user_level = levels[correct_count]
# else:
#     user_level = "Неизвестный уровень"
    
# print()
# print("Ваш ранг:")
# print(f"{user_level}")


# randint, shuffle, sample
# import random
# gifts = ["коробка леденцов", "желейные мишки", "сладкая вата", "прыгающие мячики"]
# index = random.randint(0, len(gifts) - 1)
# gift = gifts index]

# random.shuffle(gifts)
# gift = gifts[0]

# gift = random.sample(gifts, 1)[0]
# print (f"Вы выиграли {gift}")

# Функции 
# import random
# def random_gift ():
#     gifts = ["коробка леденцов", "желейные мишки"," сладкая вата"]
#     gift = random.sample(gifts, 1)[0]
#     print (f"Вы выиграли {gift}")
# while True:
#     input ()
#     random_gift ()


# return 
# import random

# def random_gift():
#     gifts = ["коробка леденцов", "желейные мишки", "сладкая вата"]
#     gift = random.choice(gifts)
#     return gift

# while True:
#     user_input = input("Нажмите Enter, чтобы выиграть приз: ")
#     gift = random_gift()
#     print(f"Вы выиграли {gift}, поздравляем!")

    
# Аргументы 

# def calc(numbers):
#     i = 0
#     for number in numbers:
#         i += int(number)
#     return i

# def main():
#     numbers = input('Введите числа через пробел: ')
#     list_number = numbers.split()
#     result = calc(list_number)
#     print(result)
 
# main()


# import random

# def random_gift (category):
#     books = ["Чистый код", "Совершенный код" , "Паттерны ООП", "Принципы", "Грокаем алгоритмы" ]
#     gadgets = [ "Умные часы", "Умные весы", "Робот пылесос" , "Экшн-камера", "Умная колбаса" ]
#     games = ["Village", "Halo Infinite", "Far Cry 6", "Hitman 3", "The Last Of Us" ]

#     if category == "игры":
#         return random.sample(games, 1)[0] 
#     elif category == "книги" :
#         return random.sample (books, 1)[0] 
#     elif category == "гаджеты" :
#         return random.sample (gadgets, 1) [0]
#     else:
#         return "Нет подарков"

# print(random_gift("игры" ))
# print(random_gift("книги" ))
# print(random_gift("гаджеты"))


# Необзательные аргументы 
# def check(prices, tip=10):
#     sum_ = sum(prices)
#     total = sum_* (100 + tip ) / 100
    
#     return total

# print (check([100, 300, 500]))
# print(check([100, 300, 500], 0))
# print(check([100, 300, 500], 20))

#  среднее
# def avg(*nums) :
#     count = len(nums)
#     nums_sum = sum(nums)
    
#     return round (nums_sum / count, 1)

# print(avg(1,2,3,4,5))
# print(avg(1,2,3,4,5,10))    

# распаковка
# def longest_word(*words):
#     leader = ""
    
#     for word in words:
#         if len(word) > len (leader):
#             leader = word
#     return leader

# print(longest_word( "Prpo","Бэклог", "Скрам" , "Достопримечательность"))


# HW__5

# import random

# words = ["code", "bit", "list", "soul", "next"]

# MORSE_CODES = {
#     "a": ".-",
#     "b": "-...",
#     "c": "-.-.",
#     "d": "-..",
#     "e": ".",
#     "f": "..-.",
#     "g": "--.",
#     "h": "....",
#     "i": "..",
#     "j": ".---",
#     "k": "-.-",
#     "l": ".-..",
#     "m": "--",
#     "n": "-.",
#     "o": "---",
#     "p": ".--.",
#     "q": "--.-",
#     "r": ".-.",
#     "s": "...",
#     "t": "-",
#     "u": "..-",
#     "v": "...-",
#     "w": ".--",
#     "x": "-..-",
#     "y": "-.--",
#     "z": "--..",
#     "1": ".----",
#     "2": "..---",
#     "3": "...--",
#     "4": "....-",
#     "5": ".....",
#     "6": "-....",
#     "7": "--...",
#     "8": "---..",
#     "9": "----.",
#     "0": "-----",
#     ", ": "--..--",
#     ".": ".-.-.-",
#     "?": "..--..",
#     "/": "-..-.",
#     "-": "-....-",
#     "(": "-.--.",
#     ")": "-.--.-"
# }

# answers = []

# def morse_encode(word):
#     """"
#     Переводит слова на английском языке в последовательности точек и тире. 
#     :param word: Исходное слово 
#     :return: строка морзянки
#     """
#     word_encoded = []
#     for letter in word:
#         word_encoded.append(MORSE_CODES.get(letter, ""))
#     return " ".join(word_encoded)

# def get_word():
#     """
#     Получает случайное слово из списка.
#     :return: строка слова
#     """
#     return random.choice(words)

# def print_statistics(answers):
#     """
#     На основе списка answers типа [True, False, False, True, False] выводит статистику.
#     :param answers: список верности ответов
#     """
#     answers_total = len(answers)
#     answers_correct = sum(answers)
#     answers_incorrect = answers_total - answers_correct
    
#     print(f"Всего задачек: {answers_total}\n"
#           f"Отвечено верно: {answers_correct}\n"
#           f"Отвечено неверно: {answers_incorrect}\n")

# def main():
#     print("Сегодня мы потренируемся расшифровывать азбуку Морзе.") 
#     print("Нажмите Enter и начнем.")
#     input()
    
#     for i in range(1, len(words) + 1):
#         current_word = get_word()
#         current_encoded = morse_encode(current_word)
#         print(f"Слово {i}: {current_encoded}")
        
#         user_input = input()
        
#         if user_input.lower() == current_word:
#             print(f"Верно, {current_word}!") 
#             answers.append(True)
#         else:
#             print(f"Неверно, {current_word}!") 
#             answers.append(False)
        
#     print_statistics(answers)

# main()


# with open('write_data.txt', 'wt') as file: # write, text
#     file.write("Hello\n")
#     file.write("World\n")
    
    

# user_language = input ("Какой язык вы учите?")
# user_time = input ("Как давно?")
# user_institution = input("Где?")
# with open('answers.txt', 'w') as file:
#     file.write (f"{user_language}\n")
#     file.write(f"{user_time}\n")
#     file.write(f"{user_institution}\n")
# print("Ответы записаны")


# HW__7




# Вложенные структуры 

# my_skills = set(["python", "flask", "django", "критическое мышление", "планирование",
# "переговоры"])
# backend_skills = {"linux","terminal" , "python", "flask", "django", "restapi"}
# frontend_skills = {"html","css", "javascript"}
# soft_skills = {"презентация","планирование", "переговоры", "лидерство", "критическое мышление"}
# print(frontend_skills.difference(my_skills))
# print(my_skills.intersection(backend_skills))
# print(my_skills.difference(backend_skills.union(frontend_skills)))
# print(soft_skills.issubset(my_skills))

# print(backend_skills.union (frontend_skills))

# 1 ifference разницу те все элементы, которые есть в `frontend_skills`, но отсутствуют в `my_skills`.

# 2 intersection пересечение То есть, все элементы, которые есть и в `my_skills`, и в `backend_skills`.

# 3 difference разницу между множеством `my_skills` и объединением множеств `backend_skills` и `frontend_skills`. То есть, все элементы, которые есть в `my_skills`, но не входят ни в `backend_skills`, ни в `frontend_skills`.

# 4 issubset является ли множество `soft_skills` подмножеством множества `my_skills`. Если все элементы из `soft_skills` есть в `my_skills`, то метод `issubset` возвращает `True`, в противном случае - `False`.

# 5 union объединение множеств, включая дубликаты.


# # Кортежи 
# def fullname_split (fullname_str):
#     name_parts = fullname_str.split ()
#     return name_parts [0], name_parts [1], name_parts [2]
# _, name, patronymic = fullname_split ( "Гаврилов Юлиан Александрович" )

# print (name)
# # print (surname)
# print (patronymic)

# # Добавляем элемены в список 

# actions = ["Написать алгоритм","Написать код","Протестировать"]
# actions.insert (0, "Посоветоваться с коллегами")
# actions.insert (2, "Посоветоваться с коллегами" )
# actions.insert (len(actions) , "Похвастаться коллегам")
# print(actions)

# # Удаляем элемет из списка 
# actions = [ "Написать алгорити", "Написать код", "Протестировать" ]
# actions.remove ( "Протестировать" )
# print(actions)


# actions = [ "Написать алгоритм","Написать код","Протестировать"]
# actions.append([ "Похвастаться","Пойти отдохнуть"])
# print(actions)
# # ['Написать алгоритм', 'Написать код', 'Протестировать', ['Похвастаться', 'Пойти отдохнуть']]


# actions = ["Написать алгоритм", "Написать код" , "Протестировать" ]
# actions.extend (["Похвастаться", "Пойти отдохнуть" ] )
# print(actions)
# # ['Написать алгоритм', 'Написать код', 'Протестировать', 'Похвастаться', 'Пойти отдохнуть']


# actions = [ "Написать алгоритм", "Написать код"," Протестировать"]
# actions.index( "Написать код")


# words = ["разработчики" , "сервисов" , "ориентируются", "на","скорость" , "ответа" , "и" , "производительность", "при" , "проектировании","архитектуры"]
# words_with_letter = []
# for word in words:
#     if "р" in word:
#         words_with_letter.append(word)
# words_with_letter.sort(reverse=True)
# print(words_with_letter)

#  список словарей 


# store = [
#     {"name": "Яблоки", "price": "100", "available": 40},
#     {"name" : "Апельсины", "price": "200", "available": 20},
#     {"name": "Гранаты","price": "400","available": 5},
# ]
# for fruit in store:
#     if fruit ['available'] > 5:
#         print(fruit ['name'], fruit['price'])

# вдлженные словари 

# store = [
#     {"name": "Яблоки", "price": "100", "available": 40},
#     {"name" : "Апельсины", "price": "200", "available": 20},
#     {"name": "Гранаты","price": "400","available": 5},
# ]

# for item in store:
#     item ['price'] = int(item ['price']) / 2
#     print(item)


# store = {
#     "apples": {"name": "Яблоки", "price": "100", "available": 40},
#     "oranges": {"name": "Апельсины", "price": "200","available": 20},
#     "pomegranate": {"name": "Гранаты", "price": "400","available": 5},
# }
# stocktaking = {}

# for key, value in store.items():
#     stocktaking[key] = value ['available']
    
# print (stocktaking)


# переупаковка словарей 


# coder_info = {
#     "name": "Алексей",
#     "languages": {
#         "java": "beginner",
#         "php": "middle",
#         "python": "senior",
#         "go": "none"
#     }
# }
# coder_info_short = {
#     "name": coder_info["name"],
#     "languages": [],
# }
# for language, level in coder_info ['languages'].items():
#     if level in ("middle", "senior"):
#         coder_info_short["languages"].append(language)
    
# print(coder_info_short)


# в JSON 

# import json

# profile = {
#     "name": "Alice",
#     "is_online": True,
#     "hobbies" : {
#             1: "cryptography",
#             2: "coding",
#             3: "outdoor activities"
#         },
# }

# json_str = json.dumps(profile) 
# print(json_str)

# обратно из Json в пайтон объект 

# import json
# raw_json = """{
#     "name" : "Алиса",
#     "is_online":true,
#     "hobbies":{
#         "1" : "cryptography",
#         "2": "coding",
#         "3": "outdoor activities"
#     }
# }"""
# profile = json.loads (raw_json)
# print (type(profile))
# print (profile["name"])
# print (profile["is_online"])
# print (profile ["hobbies"])

# реквест не работает 

# import requests

# for x in range (3):
#     response = requests.get('https://catfact.ninja/fact')
#     fact = response.json()
#     print (f"#{x + 1} - {fact['fact']}")


# HW__7





# абстракции 


# Создать класс Princess, у которого есть методы:
# • sleep (выводит "принцесса устала и прилегла поспать")
# • hide (выводит "принцесса прячется")
# • walk (выводит "принцесса прогуливается туда-сюда")
# Создать экземпляр класса, вызвать три метода  по очереди

# class Princess:
#     def sleep(self):
#         print ( "принцесса устала и прилегла поспать" )

#     def hide (self):
#         print ( "принцесса прячется" )

#     def walk (self):
#         print ( "принцесса прогуливается туда-сюда" )


# princess = Princess()

# princess.hide()
# princess.sleep()
# princess.walk()


# init and self     

# class Hero:
#     def __init__(self, name, things):
#         self.name = name
#         self.things = things
#         print ("Я", self.name, "у меня есть", self.things)
#     def iteratate_things (self): 
#         for thing in self.things:
#             print(thing)

# hero_1 = Hero ("Кусантий", [ "Голова", "Лапки", "Пуговичка", "Масочка" ])
# hero_1.iteratate_things ()

# экземпляры в деле 


# class Ticket ( ):
#     def __init__(self, flight, seat_class): # нельзя использовать переменную class
#         self.flight = flight
#         self.seat_class = seat_class
#     def print(self): # а вот принт - можно, ведь методы не конфликтуют с фукциями!
#         print(f"Я билетик на рейс {self.flight} в класс {self.seat_class}")

# ticket_1 = Ticket ("PD-320", "econom")
# ticket_2 = Ticket ("SP-101", "econom")

# tickets = {"Туда": ticket_1, "Обратно": ticket_2}

# tickets["Туда"].print()
# tickets["Обратно"].print()


# объектный подход рефакторинг 

# было 

# def can_i_buy (money, price):
    
#     if money >= price:
#         return True 
#     else:
#         return False
    
# i_have = 400
# cookie_price = 350

# can_i_buy (i_have, cookie_price)
# print(can_i_buy(i_have, cookie_price))


# стало  Сделаем такой класс, который поглотил бы нашу функцию и присвоил ее себе



# class Hero:
#     def __init__ (self, money):
#         self.money = money

#     def can_i_buy(self, price):
#         return self.money >= price

# hero = Hero (400)
# print(hero.can_i_buy (350))
# print(hero.can_i_buy (250))
# print(hero.can_i_buy (550))


# class Question:
#     def __init__(self, question, answer):
#             self.question = question
#             self.answer = answer
#     def check (self, answer):
#         return answer == self.answer
    
# question_1 = Question("Текст вопроса?", "правильный ответ")
# print(question_1.check("test"))
# print(question_1.check ("правильный ответ"))


# улучшение читаемости 

# class Employee():
#     " " " Класс Сотрудника, который описывает Фамилию, Имя и Отчество." " "
#     def __init__(self, f, i, o):
#         self.f = f
#         self.i = i
#         self.o = o
        
#     def __repr__ (self):
#         return f" {self.f} {self.i[0]}.{self.o[0]}."

# employees = [
#     Employee ("Питерская","Анисья", "Григорьевна"),
#     Employee ("Меньшова", "Изольда","Александровна"),
#     Employee ("Кручинина", "Калерия", "Тимофеевна")
# ]

# print(employees)

# дети и родители 
# ошибка ниже 

# from models import Article 

# class ArticleExtended(Article):
#     def count_symbols(self):
#         return len(self.content)
    
#     def count_words(self):
#         words = self.content.split()
#         return len(words)

# article = ArticleExtended(
#     """
#     Ваш баланс составляет $ -567.072.565,13.
#     Номер заблокирован.
#     Вас ожидает 26 лет рабства на урановых рудниках».
#     Одна СМСка. Чёртов роуминг на Сириусе." (С) Юрий Ермаков - "Баланс"
#     """
# )
# print(article.count_symbols())
# print(article.count_words())

# цепочки наследования 

# class Person():
#     def eat (self) :
#         print ("Ням ням")
# class Employee (Person):
#     def visit_demo (self):
#         print ("Все сотрудники ходят на демо. Я тоже схожу!")
# class Developer (Employee):
#     def review_code(self) :
#         print ("Делаю код-ревью коллеге. Все неплохо, пара замечаний и мерджим! " )
# class FrontendDeveloper (Developer):
#     def code_frontend(self) :
#         print ("Делаю запрос на сервер, кидаю данные в стор, раскладываю по компонентам, пушим!")
# class BackendDeveloper (Developer):
#     def code_backend (self):
#         print("Ловим параметры запроса, проверяем права, дергаем базу, сериализуем, пишем тест, тестим, пушим! ")



# несколько классов в один 

# class SMSSender ( ) :
#     def send_sms (self, message):
#         print ("Отправим сообщение через смс:", message)
# class PushSender ( ):
#     def send_push (self, message):
#         print ("Отправим сообщение через пуш-уведомления:", message)
# class MailSender ( ):
#     def send_mail (self, message):
#         print ("Отправим сообщение через почту:", message)
# class SuperSender (SMSSender, PushSender, MailSender):
#     def send_all (self, message):
#         self.send_sms (message)
#         self.send_push (message)
#         self.send_mail (message)

# sender = SuperSender()
# sender.send_all ("text message")