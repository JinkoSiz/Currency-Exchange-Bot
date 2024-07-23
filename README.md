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

2. **Add your Telegram bot token:**
   ```bash
   Replace 'YOUR_API_TOKEN' in bot.py with your actual Telegram bot token.
   
3. **Build and start the services:**
   ```bash
   docker-compose up --build

## Usage

1. **Get Exchange Rates:**
   This command returns a list of all available currencies and their rates against the Russian Ruble (RUB).
   ```bash
   /rates
   
2. **Convert Currency:**
   The bot supports both uppercase and lowercase currency codes.
   ```bash
   /exchange <from_currency> <to_currency> <amount>
