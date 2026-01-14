import pymupdf
import sys
from re import findall

def str_to_number(s):
     s = s.replace(',', '')
     if '.' in s:
          return float(s)
     else:
          return int(s)

def find_numbers_from_text(text):
     numbers = []
     number_strings = findall(r'-?\d[\d,]*\.?\d*', text)

     for num_str in number_strings:
          numbers.append(str_to_number(num_str))
     return numbers


def main(filepath = "test.pdf"):
     filepath = 'docs/' + filepath
     doc = pymupdf.open(filepath)

     largest = 0

     for page in doc:
          text = page.get_text('text')
          numbers = find_numbers_from_text(text)
          if numbers:
               numbers.append(largest)
               largest = max(numbers)
          if 'millions' in text:
               print(text)
     print(f"The largest number found in the document is: {largest}")

def bonus(filepath = "test.pdf", largest = 0):
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
                                   num_string = str(find_numbers_from_text(table[i][j]))
                                   number = str_to_number(num_string[0]) if num_string else 0
                                   largest = max(largest, number * 1000000)

     print(f"The largest number found in the document is: {largest}")
                         
                              

               
    
if __name__ == "__main__":
     bonus()
#     if len(sys.argv) < 2:
#          main()
#     elif len(sys.argv)==2:
#          try:
#               main(sys.argv[1])
#          except Exception as e:
#               print(f"File {sys.argv[1]} not found. Make sure the file exists in the 'docs' folder.")
#               sys.exit(1)
#     else:
#           print("Usage: python main.py [filename]")
#           sys.exit(1)
    
    