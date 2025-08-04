import logging

# logging.info("Hello World!")
# logging.warning("Hello World!")
# logging.error("Hello World!")
# logging.critical("Hello World!")
# logging.debug("Hello World!")
# logging.exception("Hello World!")

logging.basicConfig(
    level=logging.DEBUG,
    filename="log.txt",
    filemode="w",
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    total = num1 + num2
    print(f"Sum is: {total}")

    logging.info(f"User entered numbers: {num1} and {num2}")
    logging.warning(f"User entered numbers: {num1} and {num2}")
    logging.error(f"User entered numbers: {num1} and {num2}")
    logging.critical(f"User entered numbers: {num1} and {num2}")
    logging.debug(f"Sum calculated: {total}")

except Exception as e:
    logging.exception(f"Exception occurred: {e}")

