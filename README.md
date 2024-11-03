# innoglob
### Инструкция по запуску проекта

1. **Клонируйте репозиторий**:
    ```bash
    git clone https://github.com/MrAndroPC/innoglob
    cd innoglob/ml_api
    ```

2. **Установите зависимости**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Запустите сервер**:
    Для запуска приложения с использованием Uvicorn выполните команду:
    ```bash
    uvicorn ml_api.main:app --reload
    ```
    Опция `--reload` автоматически перезапускает сервер при изменении кода. 

После этого приложение будет доступно по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).
