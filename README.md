# FlyAi

Ссылка на скачивание .feather датасета необходимого для работы программы (после установки обязательно положите его в папку src: https://storage.googleapis.com/flyem-male-cns/v1.0/connectome-data/flat-connectome/connectome-weights-male-cns-v1.0-minconf-0.5.feather
Перечень необходимого ПО:
Python3
Git
Перечень необходимых библиотек:
pandas
pyarrow
numpy
matplotlib
scikit-learn
jupyter


Пошаговая инструкция по установке и запуску:

Откройте командную строку (терминал) на своем компьютере
Склонируйте репозиторий и перейдите в папку проекта:
	git clone https://github.com/314ver2d43/FlyAi.git
	cd FlyAi
Создайте и активируйте виртуальное окружение:
    Для Windows:
		python -m venv venv
		venv\Scripts\activate
    Для Linux / macOS:
		python3 -m venv venv
		source venv/bin/activate

Установите необходимые библиотеки одной командой:
	pip install -r src/requirements.txt

Запустите обработку данных:
	python src/dataoptimize.py

Откройте файл с анализом:
	jupyter notebook src/flybrainproject.ipynb
Примеры входных и выходных данных

Входные данные (.feather)
Таблица синаптических связей в формате Feather со следующими ключевыми колонками:
bodyid_pre / bodyid_post — ID пресинаптических и постсинаптических нейронов.
weight — сила связи (фильтруются связи с силой < 3).


Выходные данные (brain.bin)
Сжатый бинарный файл структуры:
    Header (8 байт): num_nodes (uint32), num_edges (uint32).
    Edges List (10 байт на ребро): pre_node_idx (uint32), post_node_idx (uint32), weight (uint16).
