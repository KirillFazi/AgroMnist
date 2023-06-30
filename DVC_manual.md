# Русский
# Руководство: Установка и внедрение системы DVC в ML-проект

## Введение
DVC (Data Version Control) - это система контроля версий, разработанная специально 
для проектов машинного обучения. Она помогает отслеживать изменения в ваших данных, 
коде и файлах моделей, облегчая совместную работу, 
воспроизведение результатов и управление крупномасштабными рабочими процессами ML. 
Это руководство проведет вас через процесс установки и внедрения системы DVC в ваш ML-проект.

## Предварительные условия
Убедитесь, что у вас есть следующие предварительные условия:
1. В вашей системе установлен Python 3.6 или выше.
2. Установлен менеджер пакетов Pip.
3. Установлен Git (необязательно, но рекомендуется для лучшей совместной работы).
4. Рабочая директория проекта ML.

## Шаг 1: Установка DVC
1. Откройте терминал или командную строку.
2. Выполните следующую команду для установки DVC с помощью pip:
```bash
pip install dvc
```
Ссылка на официальную документацию по установке DVC: https://dvc.org/doc/install

## Шаг 2: Инициализация DVC в каталоге проекта ML
1. Перейдите в каталог проекта ML в терминале.
2. Выполните следующую команду для инициализации DVC:
```bash
dvc init
```
Ссылка на официальную документацию по инициализации DVC: https://dvc.org/doc/command-reference/init

## Шаг 3: Настройка DVC
1. Если у вас установлен Git и вы хотите интегрировать его с DVC 
для улучшения совместной работы и контроля версий, выполните следующую команду:
```bash
dvc remote add -d myremote storage://path/to/remote
```

Пример:
```bash
dvc remote add -d myremote s3://mybucket/dvcstore
```

Замените `myremote` именем, которое вы хотите дать своему удаленному хранилищу, 
а `storage://path/to/remote` - URL или путем к вашему удаленному хранилищу 
(например, bucket, AWS, S3 или SSH).

Ссылка на официальную документацию по добавлению
удаленного хранилища: https://dvc.org/doc/command-reference/remote/add

## Шаг 4: Создание этапов DVC.
Для того чтобы создать этапы DVC, вам нужно выполнить следующие шаги:

a. Добавление исходного дата-сета в DVC.
- Откройте терминал и перейдите в каталог проекта ML.
- Выполните следующую команду для добавления исходного дата-сета в DVC:
```bash
dvc add data/board_detect
```
Ссылка на официальную документацию по добавлению файлов в DVC: https://dvc.org/doc/command-reference/add

b. Этап: `train`
- Откройте терминал и перейдите в каталог проекта ML.
- Выполните следующую команду для создания этапа DVC:
```bash
dvc run -n train -d configs/config_resunet.yaml -d data/board_detect -d neuroengine/engine_train.py -o models python neuroengine/engine_train.py --config=configs/config_resunet.yaml
```
Эта команда создает стадию DVC с именем `train` с указанными зависимостями и выходами.

c. Этап: `apply`
- Откройте терминал и перейдите в каталог проекта ML.
- Выполните следующую команду для создания стадии DVC:
```bash
dvc run -n apply -d neuroengine/engine_apply.py -d models -o data/apply python neuroengine/engine_apply.py
```
Эта команда создает стадию DVC с именем `apply` с указанными зависимостями и выходами.

Ссылка на официальную документацию по созданию этапов DVC: https://dvc.org/doc/command-reference/run

После этого мы получим следующую структуру файла dvc.yaml:
```yaml
stages:
  train:
    cmd: python neuroengine/engine_train.py --config=configs/config_resunet.yaml
    deps:
    - configs/config_resunet.yaml
    - data/board_detect
    - neuroengine/engine_train.py
    outs:
    - models
  apply:
    cmd: python neuroengine/engine_apply.py
    deps:
    - neuroengine/engine_apply.py
    - models
    outs:
    - data/apply
```

При желании и необходимости, файл dvc.ymal можно отредактировать вручную. 
Редактирование в ручную включает в себя создание новых этапов DVC и редактирование старых.

## Шаг 5: Запуск DVC pipelines

1. Чтобы выполнить этапы DVC и запустить связанные с ними команды, используйте следующую команду:
```bash
dvc repro
```
Эта команда выполнит определенные этапы и обеспечит актуальность выходных данных.

Ссылка на официальную документацию по воспроизведению 
этапов DVC: https://dvc.org/doc/command-reference/repro

## Шаг 6: Сотрудничество и контроль версий с DVC (необязательно)
1. Если вы интегрировали DVC с Git'ом в Шаге 3, 
то теперь вы можете перенести свой проект в Git-репозиторий с помощью обычных команд Git'а. 
DVC будет обрабатывать версионирование больших файлов ML и 
управлять зависимостями данных и файлов модели отдельно.
2. Для отслеживания изменений и отправки обновлений в файлы, управляемые DVC, 
вы можете использовать такие команды Git, как `git add`, `git commit` и `git push`. 
DVC позаботится об отслеживании и хранении базовых файлов данных.

## Заключение
Поздравляем! Вы успешно установили и внедрили систему DVC в свой ML-проект. 
Теперь вы можете использовать DVC для отслеживания изменений, 
воспроизведения результатов и эффективного управления рабочим процессом ML. 
Обратитесь к документации DVC для получения информации о более продвинутых функциях и 
вариантах конфигурации.

## Рекомендуемые ссылки
1. Get started по DVC: https://dvc.org/doc/start
2. Репозиторий DVC на GitHub: https://github.com/KirillFazi/AgroMnist
3. Видео туториал на YouTube: https://www.youtube.com/watch?v=kLKBcPonMYw&list=PL7WG7YrwYcnDb0qdPl9-KEStsL-3oaEjg
4. Официальная документация DVC: https://dvc.org/doc

## Примечания 
1. Про то как DVC работает с данными.
 - DVC хранит данные в отдельной папке `.dvc/cache`.
 - При первом запуске команды `dvc repro` 
  DVC скачивает данные из удаленного хранилища в папку `.dvc/cache`.
 - При последующих запусках команды `dvc repro` 
  DVC использует данные из папки `.dvc/cache`.
 - При запуске команды `dvc push` DVC отправляет данные из папки `.dvc/cache` 
  в удаленное хранилище.
 - При запуске команды `dvc pull` DVC скачивает данные из удаленного хранилища 
  в папку `.dvc/cache`.
 - При запуске команды `dvc checkout` DVC удаляет данные из папки `.dvc/cache` 
  и скачивает данные из удаленного хранилища в папку `.dvc/cache`.
 - При запуске команды `dvc gc` DVC удаляет данные из папки `.dvc/cache`, 
  которые не используются в текущем проекте.
 - При запуске команды `dvc destroy` DVC удаляет данные из папки `.dvc/cache` 
  и удаляет файлы `.dvc` из проекта.
 - При запуске команды `dvc remove` DVC удаляет данные из папки `.dvc/cache` 
  и удаляет файлы `.dvc` из проекта.
2. Как DVC хранит данные
- Когда DVC сохраняет данные в удаленном хранилище, он использует комбинацию методов 
организации файлов и дедупликации данных для оптимизации хранения и минимизации дублирования. 
Вот как DVC работает с хранением данных:
Организация файлов: DVC организует данные в удаленном хранилище с помощью файловой структуры, 
которая включает следующие компоненты:
  - Файл .dvc: Этот файл создается в каталоге проекта и служит указателем на фактический файл данных 
  в удаленном хранилище. Он содержит метаданные, такие как контрольная сумма файла, 
  размер файла и информация о местоположении удаленного хранилища.
  - Каталог .dvc/cache: Этот каталог содержит фактические файлы данных (или куски), 
  хранящиеся с возможностью адресации по содержимому. Файлы данных именуются на основе контрольной суммы их содержимого для обеспечения уникальности.
- Дедупликация данных: DVC использует хранилище с возможностью адресации содержимого 
и методы дедупликации, чтобы избежать хранения дубликатов данных. Когда вы добавляете файл или 
каталог в DVC с помощью dvc add, он вычисляет контрольную сумму (обычно хэш MD5 или SHA256) данных. 
Если такие же данные уже присутствуют в кэше, DVC распознает их на основе контрольной суммы и 
избегает их дублирования. Вместо этого он создает жесткую ссылку или ссылку 
на существующий файл данных в кэше.

- Сжатие: По умолчанию DVC не выполняет автоматического сжатия данных. 
Он хранит данные как есть в кэше и удаленном хранилище.
Однако вы можете включить сжатие вручную, сжимая файлы данных перед добавлением их в DVC. 
DVC будет хранить и передавать сжатые файлы.

--------

# English
# Manual: Installing and Implementing DVC System in an ML Project

## Introduction
DVC (Data Version Control) is a version control system 
designed specifically for machine learning projects. 
It helps track changes in your data, code, and model files, 
making it easier to collaborate, reproduce results, 
and manage large-scale ML workflows. This manual will guide you through the process 
of installing and implementing the DVC system in your ML project.

## Prerequisites
Make sure you have the following prerequisites:
1. Python 3.6 or higher installed on your system.
2. Pip package manager installed.
3. Git installed (optional but recommended for better collaboration).
4. A working ML project directory.

## Step 1: Install DVC
1. Open your terminal or command prompt.
2. Run the following command to install DVC using pip:

```bash
pip install dvc
```

## Step 2: Initialize DVC in your ML project directory
1. Navigate to your ML project directory in the terminal.
2. Run the following command to initialize DVC:
```bash
dvc init
```


## Step 3: Configure DVC
1. If you have Git installed and want to integrate it with DVC for better collaboration and version control, run the following command:
```bash
dvc remote add -d myremote storage://path/to/remote
```
Replace `myremote` with the name you want to give to your remote storage and `storage://path/to/remote` with the URL or path to your remote storage (e.g., an AWS S3 bucket or a shared network location).

## Step 4: Create DVC stages
1. Open the `dvc.yaml` file provided to you in a text editor.
2. Each stage in the file represents a step in your ML workflow.
3. For each stage, follow the instructions below to create the corresponding DVC stage:

a. Stage: `train`
- Open your terminal and navigate to your ML project directory.
- Run the following command to create the DVC stage:
  ```bash
  dvc run -n train -d configs/config_resunet.yaml -d data/board_detect -d neuroengine/engine_train.py -o models python neuroengine/engine_train.py --config=configs/config_resunet.yaml
  ```
  This command creates a DVC stage named `train` with the specified dependencies and outputs.

b. Stage: `apply`
- Open your terminal and navigate to your ML project directory.
- Run the following command to create the DVC stage:
  ```bash
  dvc run -n apply -d neuroengine/engine_apply.py -d models -o data/apply python neuroengine/engine_apply.py
  ```
  This command creates a DVC stage named `apply` with the specified dependencies and outputs.

## Step 5: Run DVC pipelines
1. To execute the DVC stages and run the associated commands, use the following command:
```bash
dvc repro
```
This command will execute the defined stages and ensure that the outputs are up-to-date.

## Step 6: Collaborate and version control with DVC (optional)
1. If you integrated DVC with Git in Step 3, 
you can now push your project to a Git repository using regular Git commands. 
DVC will handle the versioning of large ML files and manage their data and model file 
dependencies separately.
2. To track changes and push updates to your DVC-managed files, you can use Git commands 
like `git add`, `git commit`, and `git push`. DVC will handle the tracking and storage of 
the underlying data files.

## Conclusion
Congratulations! You have successfully installed and implemented the DVC system in your ML project. 
You can now use DVC to track changes, reproduce results, 
and manage your ML workflow efficiently. Refer to the DVC documentation 
for more advanced features and configuration options.

## Recommended links
1. Get started on DVC: https://dvc.org/doc/start
2. DVC repository on GitHub: https://github.com/KirillFazi/AgroMnist
3. YouTube video tutorial: https://www.youtube.com/watch?v=kLKBcPonMYw&list=PL7WG7YrwYcnDb0qdPl9-KEStsL-3oaEjg
4. official DVC documentation: https://dvc.org/doc