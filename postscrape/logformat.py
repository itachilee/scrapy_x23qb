import logging

logging.basicConfig(filename="config.log", filemode="w", format="%(asctime)s-%(name)s-%(levelname)s-%(message)s",
                    level=logging.INFO)

logger = logging.getLogger(__name__)

