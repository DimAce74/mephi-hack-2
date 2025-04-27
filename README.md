
План работ
------------
1. Разметка датасета
    1. Пробуем LLM
    1. Пробуем вручную
1. Подбор модели
    1. Стандартные средства библиотеки scikit
    1. Готовые модели (bert, llama)
    1. Сравнение метрик и выбор лучшего варианта
    1. Обучение и сериализация выбранной модели или перенос в .py код из ноутбуков
1. Создание вэб-сервиса (Flask)
1. Упаковка в Docker (docker-compose при необходимости)
1. Подготовка документации
1. Защита
1. Онлайн-празднование победы


Структура проекта
------------

```

├── README.md                  
├── data                         
│   ├── processed                # The final, canonical data sets for modeling.
│   └── raw                      # The original, immutable data dump.
│
├── docs                         # Project documentation.
│
├── models                       # Trained and serialized models.
│
├── notebooks                    # Jupyter notebooks.
├── requirements.txt             # The requirements file for reproducing the analysis environment.
└── src                          # Source code for use in this project.
    ├── __init__.py              # Makes src a Python module.
    │
    ├── data                     # Data engineering scripts.
    │
    └── models                   # ML model engineering (a folder for each model).
        └── model1      
```
