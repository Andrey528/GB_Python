from flask import Flask, render_template
from LoginForm import Lf
from AuthForm import AuthF

def flask_bootcamp():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hello hello hello hello hello world'

    @app.route('/')
    def main():
        return render_template('base.html')
        # with open('phon.txt', 'r') as file:
        #     list_1 = list()
        #     resultData = list()
        #     for line in file.readlines():
        #         resultData.append(tuple(line.split('\n')[0].split(',')))
        #
        # return render_template('base.html', data=resultData)

    @app.route('/about')
    def about():
        return render_template('about.html')

    @app.route('/register', methods=['GET', 'POST'])
    def reg():
        form = Lf()
        if form.validate_on_submit():
            if form.password_again.data != form.password.data:
                return render_template('register.html', title='Регистрация', form=form, message='Пароли не совпадают')
            with open('phon.txt', 'a') as file:
                file.write(f'{form.name.data};{form.email.data};{form.password.data}\n')
            return render_template('register.html', message='Регистрация прошла успешно')
        return render_template('register.html', title='Регистрация', form=form)

    @app.route('/index/<x>/<y>')
    def index(x, y):
        return f'Результат: {int(x) + int(y)}'

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        form = AuthF()
        if form.validate_on_submit():
            with open('phon.txt', 'r') as file:
                data = ' '.join(file.readlines())

            if form.email.data not in data:
                return render_template('login.html', title='Авторизация', form=form, message='Вы не зарегистрированы')
            else:
                for i in data.split():
                    if form.email.data in i:
                        if i.split(';')[-1] == form.password.data:
                            return render_template('login.html', title='Авторизация', message='Вы успешно авторизовались')
        return  render_template('login.html', title='Авторизация', form=form)

    app.run()