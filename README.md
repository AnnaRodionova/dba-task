# Задание на направление "Full Stack cтажёр в юнит DBA"

Запуск Docker контейнера с api:
```c
docker build -t dba-task:latest .
docker run  -p 5000:5000 -t dba-task:latest
```

После этого api станет доступно по ```http://localhost:5000```
