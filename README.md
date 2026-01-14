# document-max-number

## What this repo does

This repository provides code that scans a PDF file and outputs the largest number value that appears in the document. Additionally, it attempts to fulfill a bonus requirement that takes natural language guidance into consideration such as units 'like $ in millions'.

## Requirements

This repo makes use of the following libraries:

- PyMuPDF
- re
- sys

Download the requirements by pasting the following line into your terminal:
pip install -r requirements.txt

## Instructions

To use this yourself, place your pdf document into the docs directory. To run the script, paste the following line into your terminal:
python main.py <filename.pdf>
Note that in you filename, only write the name of the file and do not include the filepath 'doc/...'.

## Sample output and decisions

After running this file against the FY25 Air Force Working Capital Fund.pdf, I got that the largest value in the document is 6,000,000 on page 89. The largest number I found taking into account the natural language of the text was 20923900000 which can be found on page 12.

When I began implementing the bonus functionality, I noticed that there were a few formats in the pdf where natural language should be taken into account: Either when the top-left most entry in a table says a scaling unit, row-wise where the left most entry of a row specifies a unit, or a comment near the top of the page. With the time constraint I chose to only consider the first edge case. I had two function main: The first was my main() function that iterated by page finding numbers in the text, the second was called bonus_tables() which iterated the pdf by table (rather than text) checking the top left most entry for a scaling specification. I chose to only check for scaling in the millions.
