# Starcast Core Framework

Это репа самого фреймворка, публикуется как `your-org/starcast`.

## Публичный API (breaking changes = v bump)

- `actions/*/action.yml` — inputs/outputs это контракт
- `.github/workflows/*.yml` с `on: workflow_call` — сигнатура это контракт
- Output contracts в `agents/*.md` — их парсят downstream агенты

## Версионирование

- `@main` — development, нестабильно
- `@v1` — текущий stable тег
- Breaking → `@v2`
- При merge в main обновляй CHANGELOG.md

## Конвенции

- Playbooks: `playbooks/<category>/<name>.md`
- Agents: `agents/<role>.md`
- Playbook говорит ЧТО делать; agent говорит КТО это делает
- Финальный system prompt собирается `actions/assemble-prompt` в runtime

## Локальное тестирование

`../scripts/dry-run-agent.sh <edition> <role> <playbook>` — превью 
собранного system prompt без запуска Claude API.

## Перед breaking changes

1. Проверь, какие редакции используют изменяемый контракт (grep в workspace)
2. Обнови CHANGELOG.md с migration notes
3. Не пуши breaking в `@v1` — делай `@v2`
