#This code was made with generous help from ChatGPT, I am not a programmer.

import re

def sanitize_monplain(monplain):
    # Replace everything after a '#' with "_1", and remove other special characters
    monplain = re.sub(r'#.*', '_1', monplain)
    monplain = re.sub(r'[^a-zA-Z0-9]', '', monplain)
    return monplain

def generate_html_entry(number, mon, monplain, type1, type2=None):
    # Create the HTML entry
    if type2:
        types_html = f'<p class="Types"><span class="{type1}">{type1} <img src="assets/Types/{type1}.png"></span> / <span class="{type2}">{type2} <img src="assets/Types/{type2}.png"></span></p>'
    else:
        types_html = f'<p class="Types"><span class="{type1}">{type1} <img src="assets/Types/{type1}.png"></span></p>'

    return f'''
<div class="entry">
    <p class="number">#{number:03d}</p>
    <a href="Pokemon/{mon}.html"><img src="assets/Pokemon/Front/{monplain}.png" class="sprite"></a>
    <a class="Name" href="Pokemon/{mon}.html">{mon}</a>
    {types_html}
</div>
'''

def process_file(input_file, output_file):
    number = 0
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            # Skip empty lines
            if not line.strip():
                continue

            parts = line.strip().split()
            if len(parts) < 2:
                continue  # Skip lines that don't have at least two words

            mon = parts[0]
            monplain = sanitize_monplain(mon)
            type1 = parts[1].split('/')[0]  # Only take the text before the first '/'
            type2 = parts[1].split('/')[1].strip() if '/' in parts[1] else None

            if '#' not in line:
                number += 1

            # Write the HTML entry to the output file
            html_entry = generate_html_entry(number, mon, monplain, type1, type2)
            outfile.write(html_entry)

            # Debug prints to trace values
            print(f"Processed line: {line.strip()}")
            print(f"mon: {mon}, monplain: {monplain}, type1: {type1}, type2: {type2}, number: {number}")

# Define the input and output file names
input_file = 'typeindex.txt'
output_file = 'output.html'

# Process the file
process_file(input_file, output_file)
