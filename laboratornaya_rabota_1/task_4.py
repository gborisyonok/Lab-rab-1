list_ = [1, 2, 9, 13, 'a']
print('Изначальный список:', list_)

len(list_) #длина списка
print("длина списка:", len(list_))

sr_ar = sum(list_[:3]) / len(list_)
print('Найдем среднее арифметическое:', sr_ar)

list_ = [1, 2, 9, 13, sr_ar]
print('Получим новый список:', list_)
