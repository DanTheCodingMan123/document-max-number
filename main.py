import pymupdf
import sys
from re import findall

def str_to_number(s):
     '''
     Transforms a string representation of a number into an actual number (int or float).
     This function handles numbers with commas and decimal points.
     If the input is an int or float, it returns it as a float.
     '''
     if isinstance(s, (int, float)):
        return float(s)
     
     s = s.replace(',', '')
     if '.' in s:
          return float(s)
     else:
          return int(s)

def find_numbers_from_text(text):
     '''
     Returns a list of string representations of numbers found in the input text.
     It uses regular expressions to find numbers, which may include commas and decimal points.
     Returns an empty list if no numbers are found.
     '''
     numbers = []
     number_strings = findall(r'-?\d[\d,]*\.?\d*', text)

     for num_str in number_strings:
          numbers.append(str_to_number(num_str))
     return numbers


def main(filepath = "test.pdf"):
     '''
     Main function that opens a PDF, extracts the text, finds all numbers in the text, and returns the largest number found.
     the function takes a filepath as an argument with a default value of 'text.pdf'.
     '''
     filepath = 'docs/' + filepath
     doc = pymupdf.open(filepath)

     largest = 0

     for page in doc:
          text = page.get_text('text')
          numbers = find_numbers_from_text(text)
          if numbers:
               numbers.append(largest)
               largest = max(numbers)
     print(f"The largest number found in the document is: {largest}")
     return largest

def bonus_table(filepath = "test.pdf", largest = 0):
     '''
     Bonus function which iterates through the pdf by table and considers the natural language guidance in the document 
     for a specific table format.
     It looks for tables with 'million' or '$m' in the top left cell and scales all the numbers in the table accordingly.
     Returns the largest number found in the table.
     '''
     filepath = 'docs/' + filepath
     doc = pymupdf.open(filepath)

     for page in doc:
          tablelist = page.find_tables()
          for t in tablelist.tables:
               table = t.extract()
               nrows = len(table)
               ncols = len(table[0])

               if (table[0][0] is not None and 'million' in table[0][0].lower() or "$m" in table[0][0].lower()):
                    for i in range(1,nrows):
                         for j in range(1, ncols):
                              if table[i][j] is not None:
                                   num_string = find_numbers_from_text(table[i][j])
                                   number = str_to_number(num_string[0]) if num_string else 0
                                   largest = max(largest, number * 1000000)
     print(f"The largest number found in the document taking natural language guidance into consideration is: {largest}")
     return largest
                         
                              

               
    
if __name__ == "__main__":
     if len(sys.argv) < 2:
          largest = main()
          bonus_table(largest = largest)

     elif len(sys.argv)==2:
          try:
              largest = main(sys.argv[1])
              bonus_table(sys.argv[1], largest = largest)
          except Exception as e:
              print(f"File {sys.argv[1]} not found. Make sure the file exists in the 'docs' folder.")
              sys.exit(1)
     else:
          print("Please provide a single pdf file as an argument: python main.py test.py")
          sys.exit(1)
    
    