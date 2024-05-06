# MODULE 8. Homework. Functional Programming and Built-in Python Modules

## Task 1

Closure in programming is a function that retains references to variables from its lexical scope, i.e., from the area where it was declared.

Implement the caching_fibonacci function, which creates and uses a cache to store and reuse already computed Fibonacci numbers.

**The Fibonacci sequence** is a sequence of numbers like: 0, 1, 1, 2, 3, 5, 8, ..., where each subsequent number in the sequence is obtained by adding the two previous members of the sequence.

In general, to calculate the nth member of the Fibonacci sequence, you need to calculate the expression: Fn = Fn-1 + Fn-2.

This task can be solved recursively by calling a function that computes the sequence until the call reaches members of the sequence less than n, where the sequence is defined.

### Requirements:

1. The caching_fibonacci() function should return an inner fibonacci(n) function.
2. fibonacci(n) computes the nth Fibonacci number. If the number is already in the cache, the function should return the value from the cache.
3. If the number is not in the cache, the function should compute it, save it in the cache, and return the result.
4. Using recursion to calculate Fibonacci numbers.

### Recommendations for implementation:

As a recommendation, we will provide pseudo-code for the task.

> ☝ Pseudo-code is a way of writing an algorithm or piece of code that is used to describe an idea or process in a form understandable to humans. It is not intended for direct execution on a computer, but helps developers clearly understand and plan how the program or algorithm will work. Its main purpose is to convey the idea of the algorithm clearly and simply.

Here's the pseudo-code for the caching_fibonacci function, which calculates Fibonacci numbers using caching:

```
FUNCTION caching_fibonacci
Create an empty dictionary cache

FUNCTION fibonacci(n)
If n <= 0, return 0
If n == 1, return 1
If n is in cache, return cache[n]

    cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
    Return cache[n]

Return the fibonacci function
END FUNCTION caching_fibonacci
```

The **caching_fibonacci** function creates an inner **fibonacci** function and a **cache** dictionary to store the results of Fibonacci number computations. Each time **fibonacci(n)** is called, it first checks if the value for \***\*n** is already stored in the **cache**. If the value is in the cache, it returns it immediately, significantly reducing the number of recursive calls. If the value is not in the cache, it computes it recursively and stores it in the **cache**. The **caching_fibonacci** function returns the inner **fibonacci** function, which can now be used to calculate Fibonacci numbers using caching.

### Evaluation criteria:

1. Correct implementation of the fibonacci(n) function considering the use of caching.
2. Effective use of recursion and caching to optimize calculations.
3. Code cleanliness, including readability and presence of comments.

### Example of usage:

```
Get the fibonacci function
fib = caching_fibonacci()

Use the fibonacci function to compute Fibonacci numbers
print(fib(10)) # Outputs 55
print(fib(15)) # Outputs 610
```

## Task 2

You need to create a function named **generator_numbers**, which will analyze the text, identify all real numbers considered as parts of income, and return them as a generator. Real numbers in the text are written without errors and are clearly separated by spaces on both sides. Additionally, you need to implement a function named **sum_profit**, which will use **generator_numbers** to sum up these numbers and calculate the total profit.

### Requirements:

1. The function **generator_numbers(text: str)** should take a string as an argument and return a generator that iterates over all real numbers in the text. Real numbers in the text are considered to be written without errors and are clearly separated by spaces on both sides.
2. The function **sum_profit(text: str, func: Callable)** should use the generator **generator_numbers** to calculate the total sum of numbers in the input string and accept it as an argument when called.

### Recommendations for implementation:

Use regular expressions to identify real numbers in the text, considering that the numbers are clearly separated by spaces.
Apply the yield statement in the generator_numbers function to create a generator.
Ensure that sum_profit correctly processes the data from generator_numbers and sums up all the numbers.

### Evaluation criteria:

1. Correct identification and return of real numbers by the generator_numbers function.
2. Correct calculation of the total sum in sum_profit.
3. Code cleanliness, presence of comments, and compliance with PEP8 coding style.

### Example of usage:

```
text = "The employee's total income consists of several parts: $1000.01 as the main income, supplemented by additional receipts of $27.45 and $324.00."
total_income = sum_profit(text, generator_numbers)
print(f"Total income: {total_income}")

# Expected output:

Total income: $1351.46
```

## Task 3 (optional)

Develop a Python script for analyzing log files. The script should be able to read a log file passed as a command-line argument and output statistics for log levels such as INFO, ERROR, DEBUG. Additionally, the user can specify a log level as the second command-line argument to get all entries of that level.

Log files are files containing records of events that occurred in an operating system, software, or other systems. They help track and analyze system behavior, detect and diagnose issues.

To accomplish the task, take the following example log file:

```
2024-01-22 08:30:01 INFO User logged in successfully.
2024-01-22 08:45:23 DEBUG Attempting to connect to the database.
2024-01-22 09:00:45 ERROR Database connection failed.
2024-01-22 09:15:10 INFO Data export completed.
2024-01-22 10:30:55 WARNING Disk usage above 80%.
2024-01-22 11:05:00 DEBUG Starting data backup process.
2024-01-22 11:30:15 ERROR Backup process failed.
2024-01-22 12:00:00 INFO User logged out.
2024-01-22 12:45:05 DEBUG Checking system health.
2024-01-22 13:30:30 INFO Scheduled maintenance.
```

### Requirements:

1. The script should take the path to the log file as a command-line argument.
2. The script should take an optional command-line argument after the log file path. It is responsible for outputting all entries of a specific log level. It accepts values corresponding to the log level of the log file. For example, the argument error will output all ERROR level entries from the log file.
3. The script should read and analyze the log file, counting the number of entries for each logging level (INFO, ERROR, DEBUG, WARNING).
4. Implement the function **parse_log_line(line: str) -> dict** for parsing log lines.
5. Implement the function **load_logs(file_path: str) -> list** to load logs from the file.
6. Implement the function **filter_logs_by_level(logs: list, level: str) -> list** to filter logs by level.
7. Implement the function **count_logs_by_level(logs: list) -> dict** to count entries by logging level.
8. The results should be presented in the form of a table with the number of entries for each level. For this purpose, implement the function **display_log_counts(counts: dict)**, which formats and outputs the results. It takes the results of the **count_logs_by_level** function execution.

### Recommendations for implementation:

1. Before starting, familiarize yourself with the structure of your log file. Pay attention to the date and time format, logging levels INFO, ERROR, DEBUG, WARNING, and message structure.
2. Understand how different components of the log are separated, typically by spaces or special characters.
3. Divide your task into logical blocks and functions for better readability and further extension.
4. Parsing log lines is performed by the function **parse_log_line(line: str) -> dict**, which takes a log line as input and returns a dictionary with parsed components: date, time, level, message. Use string methods like **split()** to split the line into parts.
5. Loading log files is done by the function **load_logs(file_path: str) -> list**, which opens the file, reads each line, and applies the **parse_log_line** function to it, storing the results in a list.
6. Filtering by logging level is done by the function **filter_logs_by_level(logs: list, level: str) -> list**. It allows you to get all log entries for a specific logging level.
7. Counting entries by logging level is done by the function **count_logs_by_level(logs: list) -> dict**, which iterates through all entries and counts the number of entries for each logging level.
8. Output the results using the function **display_log_counts(counts: dict)**, which formats and outputs the counting results in a readable form.
9. Your script should handle different types of errors, such as missing files or errors in reading them. Use try/except blocks to handle exceptional situations.

### Evaluation criteria:

- The script meets all the specified requirements, correctly analyzing log files and outputting information.
- The script handles errors correctly, such as incorrect log file format or missing files.
- One of the elements of functional programming was used in the development: lambda function, list comprehension, filter function, etc.
- The code is well-structured, understandable, and contains comments where necessary.

### Example of usage:

When running the script

```
python main.py /path/to/logfile.log
```

We should expect the following output:

```
Logging Level| Count
---------------------
INFO         |   4
DEBUG        |   3
ERROR        |   2
WARNING      |   1
```

If the user wants to view all entries of a specific logging level, they can run the script with an additional argument, for example:

```
python main.py path/to/logfile.log error
```

This will output the overall statistics by levels and detailed information for all entries with the ERROR level.

```
Logging Level    |  Count
-----------------|----------
INFO             |    4
DEBUG            |    3
ERROR            |    2
WARNING          |    1

Log details for level 'ERROR':
2024-01-22 09:00:45 - Database connection failed.
2024-01-22 11:30:15 - Backup process failed.
```

## Task 4

Enhance the console assistant bot from the previous homework and add error handling using decorators.

### Requirements:

1. All user input errors should be handled using the input_error decorator. This decorator is responsible for returning messages to the user such as "Enter user name", "Give me name and phone please", and so on.
2. The input_error decorator should handle exceptions that occur in handler functions, specifically KeyError, ValueError, and IndexError. When an exception occurs, the decorator should return the corresponding message to the user. The program execution should not stop.

### Recommendations for implementation:

As an example, let's add the input_error decorator to handle the ValueError:

```
def input_error(func):
     def inner(*args, \*\*kwargs):
        try:
           return func(*args, \*\*kwargs)
        except ValueError:
           return "Give me name and phone please."

     return inner
```

And wrap the add_contact function of our bot with this decorator to start handling the ValueError:

```
@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."
```

You need to add handlers to other commands (functions) and add exception handling for different types with corresponding messages in the decorator.

### Evaluation criteria:

1. The presence of the input_error decorator that handles user input errors for all commands.
2. Handling of KeyError, ValueError, IndexError errors in functions using the input_error decorator.
3. Each command processing function has its own input_error decorator that handles the corresponding errors and returns the appropriate error messages.
4. The bot reacts correctly to different commands and handles input errors without terminating the program.

### Example usage:

When running the script, the dialog with the bot should be similar to this:

```
Enter a command: add
Enter the argument for the command
Enter a command: add Bob
Enter the argument for the command
Enter a command: add Jime 0501234356
Contact added.
Enter a command: phone
Enter the argument for the command
Enter a command: all
Jime: 0501234356
Enter a command:
```
