# Currency Exchange Bot

This project is a Telegram bot that provides up-to-date currency exchange rates and allows users to convert amounts between different currencies. The bot fetches the latest exchange rates from the Central Bank of Russia and stores them in a Redis database. Users can interact with the bot to get exchange rates and perform currency conversions.

## Features

- Fetches daily exchange rates from the Central Bank of Russia.
- Stores exchange rates in a Redis database.
- Responds to user commands to provide exchange rates and convert currency amounts.
- Handles both uppercase and lowercase currency codes.

## Prerequisites

- Docker
- Docker Compose
- A Telegram bot token (create a bot using [BotFather](https://core.telegram.org/bots#botfather))

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/currency_bot.git
   cd currency_bot
