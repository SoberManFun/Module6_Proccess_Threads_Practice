#___________________МОДУЛЬ_6__УРОВЕНЬ1_НАЧАЛО____________________
# import threading
# import time

# def get_thread(thread_name):
# 	time.sleep(1)  # Ожидание в 1 секунду
# 	print(thread_name)  # Вывод названия потока

# # Создание и запуск 5 потоков
# threads = []
# for i in range(1, 6):
# 	thread = threading.Thread(target=get_thread, args=(f'Thread {i}',))
# 	thread.start()
# 	threads.append(thread)

# # Ожидание завершения всех потоков
# for thread in threads:
# 	thread.join() 
#___________________МОДУЛЬ_6__УРОВЕНЬ1_КОНЕЦ____________________

#___________________МОДУЛЬ_6__УРОВЕНЬ2_НАЧАЛО____________________
# import time
# import threading

# def task(type_task):
# 	print(type_task)
# 	time.sleep(1)

# start_time = time.time()
# for _ in range(5):
# 	task(f'Последовательный запуск: {_}')
# end_time = time.time()
# sequential_time = end_time - start_time

# start_time = time.time()
# threads = []
# for _ in range(5):
# 	thread = threading.Thread(target=task(f'Параллельный запуск с потоками: {_}'))
# 	threads.append(thread)
# 	thread.start()

# for thread in threads:
# 	thread.join()
# end_time = time.time()
# threading_time = end_time - start_time

# print('Последовательный запуск:', sequential_time)
# print('Параллельный запуск с потоками:', threading_time)
#___________________МОДУЛЬ_6__УРОВЕНЬ2_КОНЕЦ____________________

#___________________МОДУЛЬ_6__УРОВЕНЬ3_НАЧАЛО____________________
# import time
# import threading
# import requests

# def get_html(link):
# 	response = requests.get(link)
# 	html = response.text
# 	print(f'Загружена страница {link}')

# urls = ['https://www.google.ru', 'https://www.yandex.ru', 'https://ru.wikipedia.org/', 'https://www.mail.ru', 'https://www.brunoyam.com/']

# print('Последовательный запуск:')
# start_time = time.time()
# for url in urls:
#     get_html(url)
# # for i in range(1, 6):
# # 	get_html(f'https://example.com/{i}')
# end_time = time.time()
# sequential_time = end_time - start_time

# print('Параллельный запуск: ')
# start_time = time.time()
# threads = []
# # for i in range(1, 6):
# for url in urls:
# 	thread = threading.Thread(target=get_html, args=(url,))
# 	thread.start()
# 	threads.append(thread)
# for thread in threads:
# 	thread.join()
# end_time = time.time()
# threading_time = end_time - start_time

# print('Последовательный запуск:', sequential_time)
# print('Параллельный запуск с потоками:', threading_time)
#___________________МОДУЛЬ_6__УРОВЕНЬ3_КОНЕЦ____________________