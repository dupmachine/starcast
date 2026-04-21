# Starcast Core Framework

Это репа самого фреймворка, публикуется как `your-org/starcast`.

## Публичный API (breaking changes = v bump)

- `actions/*/action.yml` — inputs/outputs это контракт
- `.github/workflows/*.yml` с `on: workflow_call` — сигнатура это контракт
- Output contracts в `cast/*.md` продакшенов — их парсят downstream роли

## Версионирование

- `@main` — development, нестабильно
- `@v1` — текущий stable тег
- Breaking → `@v2`
- При merge в main обновляй CHANGELOG.md

## Конвенции

- Playbooks: `playbooks/<category>/<name>.md` — в репе фреймворка
- Cast roles: `cast/<role>.md` — в репе каждого продакшена
- Playbook говорит ЧТО делать; role говорит КТО это делает
- Финальный system prompt собирается `actions/assemble-prompt` в runtime:
  framework AGENTS.md + production AGENTS.md + cast/<role>.md + playbook

## Локальное тестирование

`../scripts/dry-run-agent.sh <edition> <role> <playbook>` — превью 
собранного system prompt без запуска Claude API.

## Перед breaking changes

1. Проверь, какие продакшены используют изменяемый контракт (grep в workspace)
2. Обнови CHANGELOG.md с migration notes
3. Не пуши breaking в `@v1` — делай `@v2`
