import bibtexparser
from bibtexparser.bwriter import BibTexWriter
import re

def get_first_author_surname(author_str):
    if not author_str:
        return "Unknown"
    # Split by 'and' to get authors, then take the first one
    first_author = author_str.split(' and ')[0].strip()
    # Handle "Last, First" or "First Last"
    if ',' in first_author:
        surname = first_author.split(',')[0].strip()
    else:
        # Assume last word is surname
        surname = first_author.split()[-1].strip()
    return re.sub(r'[^a-zA-Z]', '', surname)

def get_journal_abbrev(entry):
    source = entry.get('journal') or entry.get('booktitle') or "Misc"
    # Simple heuristic
    # Remove common words
    stop_words = {'journal', 'of', 'the', 'and', 'international', 'proceedings', 'transactions', 'conference'}
    words = [w for w in re.split(r'[\s\.\-,]+', source) if w.lower() not in stop_words and w]
    
    if not words:
        return "Misc"
    
    if len(words) == 1:
        # If one word, take up to 4 chars
        return words[0][:4].capitalize()
    else:
        # Take first letter of each word
        return "".join([w[0].upper() for w in words])

def get_short_title(title_str):
    if not title_str:
        return "NoTitle"
    # Remove non-alphanumeric (keep spaces)
    clean_title = re.sub(r'[^a-zA-Z0-9\s]', '', title_str)
    words = clean_title.split()
    stop_words = {'a', 'an', 'the', 'on', 'in', 'of', 'and', 'to', 'for', 'with', 'by', 'at', 'from'}
    
    meaningful_words = [w for w in words if w.lower() not in stop_words]
    
    if not meaningful_words:
        return "NoTitle"
    
    # Take first 2 words
    selected = meaningful_words[:2]
    return "".join([w.capitalize() for w in selected])

def normalize_bib(input_path, output_path, manuscript_path):
    with open(input_path, 'r') as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)
    
    mapping = {}
    new_entries = []
    
    for entry in bib_database.entries:
        old_key = entry['ID']
        
        # Skip generating new keys for purely comment entries if they don't look like citations
        # But our previous step made them @comment{key, ...} so they have fields.
        
        author = get_first_author_surname(entry.get('author', ''))
        year = entry.get('year', '0000').strip()
        journal = get_journal_abbrev(entry)
        title = get_short_title(entry.get('title', ''))
        
        base_new_key = f"{author}{year}_{journal}_{title}"
        
        # Ensure uniqueness
        new_key = base_new_key
        counter = 'a'
        
        # Check if new_key already exists in mapping values (for other entries) 
        # or in existing entries if we were partial (but we are redoing all)
        while new_key in mapping.values():
            new_key = f"{base_new_key}{counter}"
            counter = chr(ord(counter) + 1)
            
        mapping[old_key] = new_key
        entry['ID'] = new_key
        new_entries.append(entry)
        
    bib_database.entries = new_entries
    
    # Write new bib file
    writer = BibTexWriter()
    writer.indent = '  '
    with open(output_path, 'w') as f:
        f.write(writer.write(bib_database))
        
    # Update manuscript
    with open(manuscript_path, 'r') as f:
        content = f.read()
        
    new_content = content
    # Sort mapping by length of old_key descending to avoid partial replacements if any keys are substrings
    # (Not likely for standard keys but good practice)
    sorted_keys = sorted(mapping.keys(), key=len, reverse=True)
    
    for old_k in sorted_keys:
        new_k = mapping[old_k]
        # Replace simple \cite{old_key} and other usages.
        # Just simple string replacement for this task
        new_content = new_content.replace(old_k, new_k)
        
    with open(manuscript_path, 'w') as f:
        f.write(new_content)
        
    return mapping

if __name__ == "__main__":
    mapping = normalize_bib('refs_master.bib', 'refs_master_renamed.bib', 'manuscript.md')
    
    print("### Mapping Table (Old -> New)")
    print("| Old Key | New Key |")
    print("| --- | --- |")
    for old, new in mapping.items():
        print(f"| {old} | {new} |")
        
    print("\n### Updated Manuscript (Preview)")
    with open('manuscript.md', 'r') as f:
        lines = f.readlines()
        for line in lines[:10]: # First 10 lines
            print(line.strip())
