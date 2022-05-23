# Задание #1
Имеется корневая папка. В этой папке могут находиться текстовые файлы, а также другие папки. В других папках также могут находится текстовые файлы и папки (уровень вложенности может оказаться любым). Найти все текстовые файлы, отсортировать их по имени и склеить содержимое в один текстовый файл.<br>
<br>
Решение:<br>
Заводим словари directories и files, в которых хранятся связи между директориями и путями до них и файлами и путями до них соответственно. Проходимся по текущей директории, добавляем в соответствующие словари директории и файлы. Дальше проходимся по директориям следующего уровня. В переменной beg храним указатель на индекс директорий текущего уровня в словаре directories. В конце сортируем файлы по именам, склеиваем содержимое и записываем в result.txt. В разных директориях могут быть файлы с одинаковым именем, поэтому в словарь files записываются все пути до файла данного имени.<br>
<br>
Инструкция по запуску: <br>
python3 main.py
# Задание #2
Для выполнения задания выбери любую реляционную базу данных (oracle, sql server, mysql, postgresql, sqlite и т.д.).<br>
<br>
1. Заведи в БД таблицу данных о студентах, которая будет содержать: имя, фамилия, отчество, дата рождения, группа, уникальный номер.<br>
2. Создай веб-приложение (клиентскую и серверную части), с помощью которого можно добавить студента, удалить студента по уникальному номеру, вывести список студентов.<br>
<br>
Решение:<br>
Создаём базу данных, добавляем в неё значения. На основной странице отображается таблица с данными из базы данных и кнопки для добавления и удаления. При нажатии на кнопки приложение перенаправляет на страницы /create и /delete с формой для ввода данных, при заполнении и нажатии "Submit" возвращает на главную, где можно увидеть изменения.<br>
<br>
Инструкция по запуску:<br>
sudo apt update<br>
sudo apt install flask<br>
sudo apt install sqlite3<br>
python3 create_database.py<br>
flask run<br><br>
## Задание #3 <br>
Напиши Todo List в соответствии с макетом  (макет приблизительный, ты волен придумать свое дизайнерское решение).<br>
<br>
Решение:<br>
Верстаем макет, для календаря берём готовый скрипт и стили. Создаём базу данных, подключаем к ней приложение. Пишем скрипты для выполнения функций, заданных по ТЗ (я успела только поиск по названию сделать :() <br>
<br>
Инструкция по запуску:<br>
python3 create_database.py<br>
flask run<br>
