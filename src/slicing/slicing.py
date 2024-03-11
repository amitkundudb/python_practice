import logging

logging.basicConfig(filename='slicing.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Add this line to set the logging level for console output
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

def perform_slicing(input_list, start, end):
    try:
        sliced_list = input_list[start:end]
        logging.info(f"Sliced list: {sliced_list}")
        return sliced_list
    except Exception as e:
        logging.error(f"Error occurred during slicing: {e}")
        return None

def main():
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    start = int(input("Enter the start index for slicing: "))
    end = int(input("Enter the end index for slicing: "))

    result = perform_slicing(input_list, start, end)
    if result:
        logging.info("Slicing operation completed successfully.")
    else:
        logging.error("Slicing operation failed.")

if __name__ == "__main__":
    main()