# double = lambda x:x*2
# print(double(5))
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

addition = lambda x, y: x + y
logging.info(addition(3, 4))  # Output: 7

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
logging.info(squared_numbers)  # Output: [1, 4, 9, 16, 25]
