count_hw_done = 12
count_hours = 1.5
name_course = "Python, "
time_for_1_task=count_hours/count_hw_done
print(name_course,"всего задач:",count_hw_done,'затрачено часов:',count_hours,"среднее время выполнения:",time_for_1_task)
#почему не получается складывать строки? получилось соединить переменную со словом, а после этого поставить цифру не вышло.
print(name_course+"всего задач:")#работает
word = "word"
print(name_course+"всего задач:"+word)#Работает
print(name_course+"всего:")#работает
print(name_course+"всего задач:"+count_hw_done)#это уже не работает
word = "snake"
print(name_course+"всего задач:"+word)
print(name_course+"всего:")