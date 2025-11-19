# Starting the main function.
def main():
    """
    The main block. This handles file I/O, the loop, and printing the results.
    """
    
    # Need variables for the total and the count. Starting at zero, obviously.
    total_sales = 0.0
    entry_count = 0

    # Gotta wrap this whole thing in a try/except for robust file handling.
    try:
        # Use 'with open' as a context manager; it closes the file automatically, no matter what!
        with open('sales_totals.txt', 'r') as sales_file:
            print("--- Sales Entries Processed ---")
            
            # Looping line-by-line is the most efficient (Pythonic) way to do this.
            for line in sales_file:
                # Inside the loop, we clean and convert the data.
                try:
                    # Strip the newline char and any whitespace, then force it to a float.
                    sales_amount = float(line.strip())
                    
                    # Print the entry in a nice format for verification.
                    print(f"{sales_amount:,.2f}") 
                    
                    # Tallying up the figures.
                    total_sales += sales_amount
                    entry_count += 1
                
                except ValueError:
                    # If we hit text instead of a number, skip it, but throw a warning.
                    print(f"Warning: Data issue! Skipped non-numeric line: {line.strip()}")

        # Okay, file processed. Time for the final summary.
        print("--- Summary Report ---")
        print(f"Total: {total_sales:,.2f}") 
        print(f"Number of entries: {entry_count}")

        # Big safety check: don't divide by zero if the file was empty! Can't destroy the universe you know?
        if entry_count > 0:
            average_sales = total_sales / entry_count
            print(f"Average: {average_sales:,.2f}") 
        else:
            # Let the user know if we found nothing valid.
            print("Average: N/A. Zero valid entries were processed.")

    except FileNotFoundError:
        # The most common issue. Give a clear error if the file is missing.
        print("Fatal Error: 'sales_totals.txt' was not found.")
        print("Tip: Make sure the file is in the same folder.")
    except Exception as e:
        # Catch anything else unexpected just in case.
        print(f"An unhandled critical error occurred: {e}")

# Call the main function.
main()