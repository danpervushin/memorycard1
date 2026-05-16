#подключение библиотек
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton, QGroupBox, QButtonGroup
from random import shuffle, randint


class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3       




######################## создание приложения и главного окна ########################

app = QApplication([]) #приложение
window = QWidget() #главное окно
window.setWindowTitle('Memory card') #наименование проекта
window.resize(800, 600) #размер главного окна

######################## создание виджетов главного окна ########################

#вопрос
question = QLabel('Здесь будет вопрос') #главный вопрос

#или блок 1
btn_option1 = QRadioButton("Вариант 1")
btn_option2 = QRadioButton("Вариант 2")
btn_option3 = QRadioButton("Вариант 3")
btn_option4 = QRadioButton("Вариант 4")

#или блок 2
label_result = QLabel("Правильно/Неправильно")
label_correct = QLabel("Здесь будет правильный ответ")

#кнопка
button = QPushButton("Ответить") #кнопка для ответа

######################## расположение виджетов по лэйаутам ########################

layout_main_v = QVBoxLayout() #вертикальный главный слой
window.setLayout(layout_main_v) #привязываем главный слой к окну

#вопрос
layout_main_v.addWidget(question, alignment = Qt.AlignCenter) #добавляем вопрос к главному слою


#или блок 1
layout_options = QGroupBox("Варианты ответов!") #слой группировки переключателей с наименованием

layout_main_v.addWidget(layout_options) #показываем или группу с опциями к главному слою

layout_options_h = QHBoxLayout() #горизонтальный слой для ответов
layout_options.setLayout(layout_options_h) #привязываем слой для ответов к группе переключателей

layout_options1_v = QVBoxLayout() #вертикальный слой для первой половины ответов
layout_options1_v.addWidget(btn_option1) #добавляем виджеты для первой половины ответов
layout_options1_v.addWidget(btn_option2)
layout_options_h.addLayout(layout_options1_v)  #добавляем слой для первой половины ответов к слою для всех ответов

layout_options2_v = QVBoxLayout() #вертикальный слой для второй половины ответов
layout_options2_v.addWidget(btn_option3) #добавляем виджеты для второй половины ответов
layout_options2_v.addWidget(btn_option4)
layout_options_h.addLayout(layout_options2_v)  #добавляем слой для второй половины ответов к слою для всех ответов



#или блок 2
layout_answers = QGroupBox("Результаты теста!") #слой группировки переключателей с наименованием
layout_answers_v = QVBoxLayout()
layout_answers_v.addWidget(label_result)
layout_answers_v.addWidget(label_correct)
layout_answers.setLayout(layout_answers_v)
layout_main_v.addWidget(layout_answers) #показываем или  группу с ответом к главному слою


#кнопка
layout_main_v.addWidget(button, alignment = Qt.AlignCenter) #добавляем кнопку ответа к главному слою


######################## отображение блока приложения ########################

layout_options.show()
layout_answers.hide()

######################## функции ########################


answers = [btn_option1, btn_option2, btn_option3, btn_option4]

def ask(q:Question):

    # btn_option1.setChecked(False)
    # btn_option2.setChecked(False)
    # btn_option3.setChecked(False)
    # btn_option4.setChecked(False)

    layout_options.show()
    layout_answers.hide()
    shuffle(answers)
    question.setText(q.question)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    label_correct.setText(q.right_answer)
    button.setText("Ответить")


def show_correct(bool_answer):
    label_result.setText(bool_answer)
    # label_correct.setText(answers[0].text)
    button.setText("Следующий вопрос")
    layout_options.hide()
    layout_answers.show()


def check_answer():
    if answers[0].isChecked() or answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
        if answers[0].isChecked():
            show_correct("Правильно")
            window.score += 1
        else:
            show_correct("Неправильно")
        print(f"Кол-во правильных ответов: {window.score}")
        print(f"Кол-во вопросов: {window.total}")
        print(f"Процент правильных ответов: {window.score /  window.total * 100}")


qlist = [
    Question("Кто был в 4 части волшебника Изумрудного города?", "Эми и Тим ,Эли и Фред ", "Эли и Тим , Чарли", "Тата и Марта", "Лео и Тиг"),
    Question("Какого цвета яблоко?", "золотое", "зеленое", "красное", "желтое"),
    Question("Как звали друга Гарри Поттера?", "Рон", "Симус", "Малфой", "Креб"),
    Question("Cколько будет 30 * 30?", "900", "800", "1200", "5555"),
    Question("Какой газ преобладает в атмосфере Земли?", "азот", "кислород", "углекислый газ", "аргон"),
    Question("Кто написал роман «Война и мир»?", "Лев Толстой", "Фёдор Достоевский", "Иван Тургенев", "Антон Чехов"),
    Question("Какая планета Солнечной системы самая большая?", "Юпитер", "Сатурн", "Земля", "Нептун"),
    Question("В каком году человек впервые ступил на Луну?", "1969", "1957", "1975", "1980"),
    Question("Какой химический элемент обозначается символом O?", "кислород", "золото", "озон", "осмий"),
    Question("Кто открыл закон всемирного тяготения?", "Исаак Ньютон", "Альберт Эйнштейн", "Галилео Галилей", "Николай Коперник"),
    Question("Сколько континентов на Земле?", "6", "5", "7", "8"),
    Question("Какое животное является самым крупным на планете?", "синий кит", "африканский слон", "кашалот", "белый носорог"),
    Question("В какой стране находится город Венеция?", "Италия", "Франция", "Испания", "Греция"),
    Question("Какой орган вырабатывает инсулин?", "поджелудочная железа", "печень", "почки", "щитовидная железа")
]        


# window.cur = -1
def next_question():
    window.total += 1
    # window.cur += 1
    cur_question = randint(0, len(qlist) - 1)
    q = qlist[cur_question]
    # if window.cur >= len(qlist):
    #     window.cur = 0
    # q = qlist[window.cur]
    ask(q)


def clikc_ok():
    if button.text() == "Ответить":
        check_answer()
    elif button.text() == "Следующий вопрос":
        next_question()



# ask(Question("Какого цвета яблоко?", "золотое", "зеленое", "красное", "желтое"))
# button.clicked.connect(check_answer)

button.clicked.connect(clikc_ok)
window.score = 0
window.total = 0
next_question()


######################## отображение окна приложения ########################

window.show()
app.exec_()





# def show_question():
#     layout_answers.hide()
#     layout_options.show()
#     # layout_options.setExclusive(False)
#     btn_option1.setChecked(False)
#     btn_option2.setChecked(False)    
#     btn_option3.setChecked(False)
#     btn_option4.setChecked(False)
#     # layout_options.setExclusive(True)
#     button.setText("Ответить")

# def show_result():
#     RadioGroupBox.hide()
#     AnswerGroupBox.show()
#     button.setText("Следущий вопрос")

# def start_test():
#     if button.text() == "Ответить":
#         show_result()
#     else:
#         show_question()

# button.clicked.connect(start_test)
