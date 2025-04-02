import logging

user_logger = logging.getLogger('user_logger')
user_logger.setLevel(level=logging.INFO)

system_logger = logging.getLogger('system_logger')
system_logger.setLevel(level=logging.DEBUG)

user_handler = logging.FileHandler('user.log')
system_handler = logging.FileHandler('system.log')

formatter = logging.Formatter('%(asctime)s - %(name)s - %(message)s')
user_handler.setFormatter(formatter)
system_handler.setFormatter(formatter)

user_logger.addHandler(user_handler)
system_logger.addHandler(system_handler)

user_logger.info("This is an INFO mssg")
system_logger.info("This is an ERROR mssg")