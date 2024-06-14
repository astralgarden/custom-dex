import re
import os

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

    html_content = f'''
<div class="entry">
    <p class="number">#{number:03d}</p>
    <a href="../{mon}.html"><img src="../assets/Pokemon/Front/{monplain}.png" class="sprite"></a>
    <a class="Name" href="../{mon}.html">{mon}</a>
    {types_html}
</div>
'''

    # Write HTML content to a file in Pokemon_HTML folder
    file_path = os.path.join('Pokemon_HTML', f'{mon}.html')
    with open(file_path, 'w') as html_file:
        html_file.write(html_content)

def process_file(input_file):
    number = 0
    with open(input_file, 'r') as infile:
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

            # Generate HTML entry for the current Pokemon
            generate_html_entry(number, mon, monplain, type1, type2)

            # Increment number unless line contains '#'
            if '#' not in line:
                number += 1

            # Debug prints to trace values
            print(f"Processed line: {line.strip()}")
            print(f"mon: {mon}, monplain: {monplain}, type1: {type1}, type2: {type2}, number: {number}")

# Define the input file name
input_file = 'typeindex.txt'

# Ensure Pokemon_HTML folder exists, create it if necessary
if not os.path.exists('Pokemon_HTML'):
    os.makedirs('Pokemon_HTML')

# Process the file
process_file(input_file)
