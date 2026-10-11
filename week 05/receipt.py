# Creativity: I added a return-by date that is 30 days after the purchase date.

import csv
from datetime import datetime, timedelta


def read_dictionary(filename, key_column_index):
    """Read a CSV file into a compound dictionary."""
    dictionary = {}

    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)

        # Skip the header row.
        next(reader)

        for row in reader:
            if len(row) != 0:
                key = row[key_column_index]
                dictionary[key] = row

    return dictionary


def main():
    try:
        # Read the products.csv file into a dictionary.
        products_dict = read_dictionary("products.csv", 0)

        # Open the request.csv file.
        with open("request.csv", "rt") as request_file:
            reader = csv.reader(request_file)

            # Skip the header row.
            next(reader)

            print("Mira's Grocery Store")
            print()

            total_items = 0
            subtotal = 0

            # Read each item in the customer's order.
            for row in reader:
                product_number = row[0]
                quantity = int(row[1])

                product = products_dict[product_number]

                product_name = product[1]
                price = float(product[2])

                print(f"{product_name}: {quantity} @ {price:.2f}")

                total_items += quantity
                subtotal += quantity * price

        # Calculate sales tax and total.
        sales_tax = subtotal * 0.06
        total = subtotal + sales_tax

        print()
        print(f"Number of Items: {total_items}")
        print(f"Subtotal: ${subtotal:.2f}")
        print(f"Sales Tax: ${sales_tax:.2f}")
        print(f"Total: ${total:.2f}")
        print()

        print("Thank you for shopping at Mira's Grocery Store.")

        # Print the current date and time.
        current_date_and_time = datetime.now()
        print(f"{current_date_and_time:%a %b %d %I:%M:%S %p %Y}")

        # Creativity: print a return-by date 30 days in the future at 9:00 PM.
        return_date = current_date_and_time + timedelta(days=30)
        return_date = return_date.replace(
            hour=21, minute=0, second=0, microsecond=0
        )
        print(f"Return by: {return_date:%a %b %d %I:%M %p %Y}")

    except FileNotFoundError as error:
        print("Error: missing file")
        print(error)

    except PermissionError as error:
        print("Error: permission denied")
        print(error)

    except KeyError as error:
        print("Error: unknown product ID in the request.csv file")
        print(error)


if __name__ == "__main__":
    main()