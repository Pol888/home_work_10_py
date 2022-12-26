import bot
import logging

def main():
    bot.executor.start_polling(dispatcher=bot.dp, skip_updates=True, on_startup=bot.on_start)


if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )
    main()
