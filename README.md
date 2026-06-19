# Habit Tracker — Telegram Bot
A Telegram bot for tracking daily habits — add a habit, mark it done, and watch your streak grow. Built as a backend learning project in Python.

## Demo

![Demo](Screenshot_commands.png)

## Tech Stack

- **Python 3.12**
- **python-telegram-bot** — Telegram Bot API
- **SQLAlchemy** (ORM) + **PostgreSQL** (psycopg2 driver)
- **python-dotenv** — configuration via environment variables
- **pytest** — repository-layer tests
- **Docker** — containerization
- **GitHub Actions** — CI: runs tests on every push
- **Railway** — deployment, the bot runs 24/7

## Architecture

Layered structure:

```
main.py              entry point: registers commands, starts polling
bot/handlers.py      Telegram command handlers, manage the DB session
db/repository.py     pure data-access functions (receive a session)
db/models.py         SQLAlchemy table models
db/connection.py     engine + SessionLocal (DB connection)
```

The repository layer uses dependency injection — functions take a `session` as a parameter, which makes them easy to test against a separate test database.

## Database Schema

- **users** — `telegram_id` (PK) `name` `created_at`
- **habits** — `id` (PK), `telegram_id` (FK → users), `name` `description` `times_a_day`
- **completions** — `id` (PK), `habit_id` (FK → habits), `completed_at`

## Commands

- `/start` — Сreates your account and its ID
- `/help` — Show list of all commands
- `/add <name>` — Adds a new habit
- `/list` — Shows a list of all your habits
- `/delete <id>` — Deletes a habit
- `/done <id>` — Marks a habit as completed
- `/streak <id>` — Shows the streak

## Running Locally

```bash
git clone https://github.com/Fluxxion88/telegram-bot-dailyk.git
cd telegram-bot-dailyk

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# create a .env file with your values:
# TELEGRAM_BOT=your_token_from_BotFather
# DATABASE_URL=postgresql://user:pass@localhost:5432/dbname

python main.py
```

### With Docker

```bash
docker build -t habit-tracker .
docker run --env-file .env habit-tracker
```

## Tests

```bash
pip install pytest
pytest
```

7 repository-layer tests running on in-memory SQLite. They run automatically in CI on every push.