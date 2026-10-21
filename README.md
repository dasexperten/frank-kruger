# Frank Kruger — ассистент диссертационного исследования

Главный постоянный проект Фрэнка — диссертация Людмилы Олеговны Адамян. Начинай с [паспорта исследования](research/dissertation/BRIEF.md), [состояния работы](research/PROJECT_STATE.md) и [открытых вопросов](research/dissertation/OPEN_QUESTIONS.md).

## Как работает память

Текущая модель читает инструкции и извлекает доказательства из файлов. После работы она дистиллирует проверяемые уроки, записывает кандидатов, проверяет поддержку источниками и обновляет память. Это файловая память с историей, а не обучение весов модели или непрерывно работающий сервис.

```sh
python tools/memory.py cycle
python tools/memory.py search 'Гипотеза исследования' --limit 6 --budget 12000
python -m unittest discover -s tests -v
```

Поиск локальный, лексический, без внешнего API. Он возвращает пути, строки и выдержки. Цикл исключает неподтверждённые, спорные, просроченные и изменившиеся карточки из актуальной памяти. Дистилляция выполняется моделью по [протоколу](memory/PROTOCOL.md) и [заданию](memory/DISTILL_PROMPT.md); код проверяет происхождение и переходы статусов, но не истинность научных утверждений.

Без выполнения кода: открой [индекс документов](indexes/README.md), выбери релевантные разделы, прочитай исходник и проверь статус/даты карточек вручную. Не объявляй устаревший снимок проверенной памятью. [Инструкция запуска](START_HERE.md) объясняет передачу контекста ассистенту.

## Навигация

| Раздел | Назначение |
|---|---|
| [AGENTS.md](AGENTS.md), [CLAUDE.md](CLAUDE.md) | Обязательный старт с главного проекта и извлечения доказательств |
| [CHARTER.md](CHARTER.md), [VOICE.md](VOICE.md) | Миссия, независимость, манера работы |
| [RESEARCH_PROGRAM.md](RESEARCH_PROGRAM.md) | Последовательность исследования |
| [MEMORY.md](MEMORY.md), [LEARNING.md](LEARNING.md) | Решения и методические уроки |
| [memory/PROTOCOL.md](memory/PROTOCOL.md) | Поиск, дистилляция, проверки и цикл памяти |
| [memory/cards.json](memory/cards.json) | Карточки с источниками, статусами и историей |
| [indexes/MEMORY.md](indexes/MEMORY.md), [indexes/memory.json](indexes/memory.json) | Снимок актуальных карточек после cycle |
| [indexes/README.md](indexes/README.md), [indexes/search.json](indexes/search.json) | Индекс источников и поисковые фрагменты |
| [research/dissertation/BRIEF.md](research/dissertation/BRIEF.md) | Тема, цель, гипотеза, главы и приоритеты |
| [research/dissertation/manifest.json](research/dissertation/manifest.json) | Происхождение, исходные имена и SHA-256 шести материалов |
| [research/dissertation/originals/](research/dissertation/originals/) | Неизменённые DOCX/PDF; требуют разрешения на распространение |
| [research/dissertation/sources/](research/dissertation/sources/) | Текстовые производные для поиска, с ограничениями извлечения |
| [methods/INDEX.md](methods/INDEX.md) | Финансы, эмпирика, литература и письмо |
| [templates/SESSION.md](templates/SESSION.md) | Запись результатов и передача следующей сессии |
| [templates/RESEARCH_PACKET.md](templates/RESEARCH_PACKET.md) | Матрицы литературы, утверждений и рецензирования |
| [tools/memory.py](tools/memory.py) | Исполняемый механизм поиска и памяти, Python 3.10+ |
| [tools/extract_sources.py](tools/extract_sources.py) | Повторное извлечение текста; PDF требует pdftotext |
| [tests/test_memory.py](tests/test_memory.py) | Регрессионные проверки жизненного цикла и поиска |

## Границы

GitHub-only: нет Cloudflare, внешнего хранилища памяти или автономного процесса. Права GitHub определяют доступ; инструкции не заменяют их. Конфиденциальные рукописи и email-материалы нельзя публиковать без отдельного решения. Поиск не проверяет научную истинность; оригинал имеет приоритет перед производным текстом, особенно для таблиц, формул и цитат.

## Полный индекс файлов

- [.gitignore](.gitignore)
- [ACCESS_POLICY.md](ACCESS_POLICY.md)
- [AGENTS.md](AGENTS.md)
- [CHARTER.md](CHARTER.md)
- [CLAUDE.md](CLAUDE.md)
- [LEARNING.md](LEARNING.md)
- [MEMORY.md](MEMORY.md)
- [README.md](README.md)
- [RESEARCH_PROGRAM.md](RESEARCH_PROGRAM.md)
- [START_HERE.md](START_HERE.md)
- [VOICE.md](VOICE.md)
- [data/README.md](data/README.md)
- [drafts/README.md](drafts/README.md)
- [evaluation/SCENARIOS.md](evaluation/SCENARIOS.md)
- [indexes/MEMORY.md](indexes/MEMORY.md)
- [indexes/README.md](indexes/README.md)
- [indexes/memory.json](indexes/memory.json)
- [indexes/search.json](indexes/search.json)
- [memory/DISTILL_PROMPT.md](memory/DISTILL_PROMPT.md)
- [memory/PROTOCOL.md](memory/PROTOCOL.md)
- [memory/cards.json](memory/cards.json)
- [methods/EMPIRICAL.md](methods/EMPIRICAL.md)
- [methods/FINANCE.md](methods/FINANCE.md)
- [methods/INDEX.md](methods/INDEX.md)
- [methods/LEARNING_CYCLE.md](methods/LEARNING_CYCLE.md)
- [methods/LITERATURE.md](methods/LITERATURE.md)
- [methods/WRITING.md](methods/WRITING.md)
- [research/INDEX.md](research/INDEX.md)
- [research/PROJECT_STATE.md](research/PROJECT_STATE.md)
- [research/README.md](research/README.md)
- [research/dissertation/BRIEF.md](research/dissertation/BRIEF.md)
- [research/dissertation/CORRESPONDENCE.md](research/dissertation/CORRESPONDENCE.md)
- [research/dissertation/OPEN_QUESTIONS.md](research/dissertation/OPEN_QUESTIONS.md)
- [research/dissertation/manifest.json](research/dissertation/manifest.json)
- [research/dissertation/originals/academic-writing.pdf](research/dissertation/originals/academic-writing.pdf)
- [research/dissertation/originals/article-example.pdf](research/dissertation/originals/article-example.pdf)
- [research/dissertation/originals/article-plan.docx](research/dissertation/originals/article-plan.docx)
- [research/dissertation/originals/article-structure.docx](research/dissertation/originals/article-structure.docx)
- [research/dissertation/originals/article-writing.docx](research/dissertation/originals/article-writing.docx)
- [research/dissertation/originals/dissertation-concept-2026-09-07.docx](research/dissertation/originals/dissertation-concept-2026-09-07.docx)
- [research/dissertation/sources/academic-writing.txt](research/dissertation/sources/academic-writing.txt)
- [research/dissertation/sources/article-example.txt](research/dissertation/sources/article-example.txt)
- [research/dissertation/sources/article-plan.txt](research/dissertation/sources/article-plan.txt)
- [research/dissertation/sources/article-structure.txt](research/dissertation/sources/article-structure.txt)
- [research/dissertation/sources/article-writing.txt](research/dissertation/sources/article-writing.txt)
- [research/dissertation/sources/dissertation-concept-2026-09-07.txt](research/dissertation/sources/dissertation-concept-2026-09-07.txt)
- [templates/RESEARCH_PACKET.md](templates/RESEARCH_PACKET.md)
- [templates/SESSION.md](templates/SESSION.md)
- [tests/test_memory.py](tests/test_memory.py)
- [tools/extract_sources.py](tools/extract_sources.py)
- [tools/memory.py](tools/memory.py)
