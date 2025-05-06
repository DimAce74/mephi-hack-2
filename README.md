Запуск приложения
------------

1. Запуск из исходников (приложение доступно по адресу http://127.0.0.1:5000)
    ```
    pip install -r ./src/web/requirements.txt
    python ./src/web/server.py
    ```
1. Сборка и запуск докер-образа (приложение доступно по адресу http://localhost)
    ```
    docker build -f ./src/web/Dockerfile -t server_image ./src/web
    docker run -it --rm --name=server_container -p=80:80 server_image
    ```
1. Запуск готового образа с DockerHub (приложение доступно по адресу http://localhost)
    ```

    ```



Структура проекта
------------

```

├── README.md                  
├── data                         
│   ├── processed
│   │     ├── хакатон_2.xlsx            --  датасет после очистки и аугметации
│   │     ├── cleared.csv               --  датасет после очистки и аугметации, классы в виде списков
│   │     ├── cleared_one_class.csv     --  датасет после очистки и аугметации, оставлено 6 классов, multi-label убраны
│   │     ├── cleared_one_other.csv     --  датасет после очистки и аугметации, оставлено 7 классов (добавлен класс `другое`), multi-label убраны
│   │     └── deepseek.xlsx             --  датасет после классификации через DeepSeek
│   └── raw                             # The original, immutable data dump.
│
├── docs                         
│   ├── Ход работ.md                    -- описание хода работ
│   └── dataset description.txt         -- описание исходного датасета
├── models                              # Trained and serialized models.
│
├── notebooks                           # Jupyter notebooks.
│   ├── EDA.ipynb                       -- EDA и предобработка датасета
│   ├── baseline_denis.ipynb            -- обучение модели на базовых трансформерах
│   ├── bert2.ipynb                     -- обучение базовой модели Bert c multi-label
│   ├── bert_one_class.ipynb            -- обучение базовой модели Bert на 6 классах
│   ├── bert_one_class_ru.ipynb         -- обучение русскоязычной модели Bert на 6 классах с оверсемплингом
│   └── bert_ru_other.ipynb             -- **Итоговая модель.** Обучение русскоязычной модели Bert на 7 классах с оверсемплингом на обработанном датасете
├── requirements.txt                    # The requirements file for reproducing the analysis environment.
└── src                                 # Source code for use in this project.
    ├── __init__.py                     # Makes src a Python module.
    └── web                             web-приложение для демонстрации
        ├── models                      # ML model engineering (a folder for each model).
        ├── static                      -- CSS-стили
        ├── templates                   -- HTML-templates  
        ├── Dockerfile                  -- Dockerfile для сборки образа приложения
        ├── requirements.txt            # The requirements file for reproducing the analysis environment.
        ├── server.py                   -- серверная часть (на Flask)
        └── uwsg.ini                    -- конфигурация UWSG
              
```
