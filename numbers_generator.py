
'''need to create a function generator_numbers that will parse the text, identify all real numbers that are considered parts of the revenue, and return them as a generator. The real numbers in the text are written without errors, clearly separated by spaces on both sides. You also need to implement a function sum_profit that will use generator_numbers to sum these numbers and calculate the total profit.'''



import re

def generator_numbers(text):
    # Use regular expression to find all real numbers in the text
    salary_parts = re.findall(r'\b\d+\.\d+\b', text)

    if not salary_parts:
        raise ValueError("No real numbers found in the text.")
    
    else:

    
        for numbers in salary_parts:
            yield float(numbers)


if __name__ == "__main__":

    text = "The company's revenue for the last quarter was 150000.50 dollars, and the profit was 50000.75 dollars."
    
    total_profit = sum(generator_numbers(text))
    print(f"Total profit test1: {total_profit}")


    text_2 = """We expect to increase salary to our employees by ten percent next year. The current average salary is 60000.00 dollars, and we have and additional 20000.00 dollars allocated for bonuses."""

    total_profit_2 = sum(generator_numbers(text_2))
    print(f"Total profit test2: {total_profit_2}")