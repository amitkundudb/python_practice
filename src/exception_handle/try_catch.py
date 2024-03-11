import logging

logging.basicConfig(filename='error.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def main():
    try:
        number1 = int(input("Enter a number: "))
        number2 = int(input("Enter another number: "))

        result = number1 / number2
        logging.info(f"Result of division: {result}")
        logging.info("This line will only be executed if no exception occurs.")

    except ValueError as e:
        logging.error(f"ValueError: {e}")
        logging.error("Please enter valid integers.")

    except ZeroDivisionError as e:
        logging.error(f"ZeroDivisionError: {e}")
        logging.error("Cannot divide by zero.")

    finally:
        logging.info("End of program.")


if __name__ == "__main__":
    main()
