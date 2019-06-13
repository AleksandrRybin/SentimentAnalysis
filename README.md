# SentimentAnalysis

Анализ тональности отзывов на мобильные телефоны

- Классификатор обучен оценивать тональность __негативная__ или __положительная__ отзывов на мобильные телефоны на русском языке.

- Для взаимодействия используется _веб интерфейс_.

Проект доступен на [**Heroku**](https://mobile-reviews-sentiment.herokuapp.com/)

##  Лоакальный запуск

1) Находясь в папке проекта запустить файл _run.py_

```python
python run.py
```

2) В браузере передти по адресу **localhost:5000**

## Использование

1) Ввести в текстовое поле отзыв

2) Нажать кнопку с иконкой *"загрузки в облако"*

3) Для очистки результатов нажать кнопку с иконкой *"мусорной корзины"*

### Примеры отзывов

В папке *samples* находятся разные примеры отзывов с разным количеством звёзд. Количество звёзд на данном отзыве указано в названии файла. Работу классификатора можно оценить на данных примерах.

### Повторение результатов

В папке *src/sentiment_classifier* находятся необходимые скрипты для повторения эксперимента

- **reviews_spider.py** - парсинг сайта с отзывами

- **train.py** - обучение модели на полученных данных

В папке *data* уже есть обучающая выборка (*reviews.json*) и обученная модель (*mobile_review_clf.dat*)
