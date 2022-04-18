"""Logging framework for python."""
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s',
                    handlers=[
                        logging.FileHandler("scraper.log"),
                        logging.StreamHandler()
                    ])

class Logger:
    """Logger class for all of the py files."""
    def debug(message):
        """Debug."""
        logging.debug(message)

    def info(message):
        """Info."""
        logging.info(message)

    def warning(message):
        """Warning."""
        logging.warning(message)

    def error(message):
        """Error."""
        logging.error(message)

    def critical(message):
        """Critical."""
        logging.critical(message)
