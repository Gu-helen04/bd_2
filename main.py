import sqlalchemy
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

from class_bd import create_tables, publisher,book, shop,stock,sale

if __name__ == '__main__':
    login = 'postgres'
    password = '123raf2411'
    bd_name = 'db1_1'
    DSN = "postgresql://"+login+":"+password+"@localhost:5432/"+bd_name
    engine = sqlalchemy.create_engine(DSN)

    Session = sessionmaker(bind=engine)
    session = Session()
    # создание БД
    create_tables(engine)
    comand = int(input(f'Заполнить БД?\n 1 - Да\n 2 - Нет\nВвод: '))
    if comand == 1:
        # Заполнение таблицы publisher
        publisher_1 = publisher(name='Джордж Оруэлл')
        publisher_2 = publisher(name='Эрих Мария Ремарк')
        publisher_3 = publisher(name='Рей Брэдбери')
        publisher_4 = publisher(name='Стивен Кинг')
        session.add_all([publisher_1, publisher_2, publisher_3, publisher_4])
        session.commit()
        # Заполнение таблицы book
        book_1 = book(title='1984', publisher=publisher_1)
        book_2 = book(title='Три товарища', publisher=publisher_2)
        book_3 = book(title='451 градус по Фаренгейту', publisher=publisher_3)
        book_4 = book(title='Оно', publisher=publisher_4)
        book_5 = book(title='Кладбище домашних животных', publisher=publisher_4)
        session.add_all([book_1, book_2, book_3, book_4, book_5])
        session.commit()
        # Заполнение таблицы shop
        shop_1 = shop(name='Читай город')
        shop_2 = shop(name='Фолиант')
        session.add_all([shop_1, shop_2])
        session.commit()
        # Заполнение таблицы stock
        stock_1 = stock(count=10, shop=shop_1, book=book_1)
        stock_2 = stock(count=15, shop=shop_1, book=book_2)
        stock_3 = stock(count=20, shop=shop_2, book=book_3)
        stock_4 = stock(count=5, shop=shop_2, book=book_4)
        stock_5 = stock(count=13, shop=shop_2, book=book_5)
        session.add_all([stock_1, stock_2, stock_3, stock_4, stock_5])
        session.commit()
        # Заполнение таблицы sale
        sale_1 = sale(data_sale='2022-07-15', count=10, stock=stock_1)
        sale_2 = sale(data_sale='2022-07-17', count=18, stock=stock_4)
        session.add_all([sale_1, sale_2])
        session.commit()
    elif comand == 2:
        serch_p = int(input('Введите id писателя: '))
        for serch_ in session.query(publisher).filter(publisher.id == serch_p).all():
            print(f'\nИтог поиска:\n  {serch_}')
    else:
        print('Ошибка ввода!')

    session.close()

