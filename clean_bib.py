import bibtexparser
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase
import re

def normalize_string(s):
    if not s:
        return ""
    # Remove non-alphanumeric characters and convert to lower case
    return re.sub(r'[^a-z0-9]', '', s.lower())

def clean_bib_file(input_path, output_path):
    with open(input_path, 'r') as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)

    seen_dois = {}
    seen_title_year = {}
    
    report = []
    processed_entries = []

    # Iterate over a copy of entries to safely modify
    for entry in bib_database.entries:
        entry_key = entry['ID']
        entry_doi = entry.get('doi', '').strip()
        entry_title = entry.get('title', '').strip()
        entry_year = entry.get('year', '').strip()
        
        # Check required fields
        required_fields = ['author', 'title', 'year']
        missing_fields = [f for f in required_fields if f not in entry]
        
        # Check journal or booktitle
        if 'journal' not in entry and 'booktitle' not in entry:
             missing_fields.append('journal/booktitle')

        if missing_fields:
            report.append(f"- **[Warning]** Entry `{entry_key}` missing fields: {', '.join(missing_fields)}")

        is_duplicate = False
        
        # 1. DOI Check
        if entry_doi:
            if entry_doi in seen_dois:
                # Found duplicate DOI
                original_key = seen_dois[entry_doi]
                report.append(f"- **[Duplicate]** Entry `{entry_key}` is a duplicate of `{original_key}` (Matching DOI: `{entry_doi}`). marked as COMMENT.")
                
                # Mark as comment
                entry['ENTRYTYPE'] = 'comment'
                entry['note'] = f"Duplicate of {original_key} based on DOI"
                is_duplicate = True
            else:
                seen_dois[entry_doi] = entry_key
        else:
            # No DOI, add note
            current_note = entry.get('note', '')
            if 'DOI_MISSING' not in current_note:
                entry['note'] = (current_note + " {DOI_MISSING}").strip()
            
            # Check Title + Year duplicate candidate
            norm_key = (normalize_string(entry_title), normalize_string(entry_year))
            if norm_key[0] and norm_key[1]: # Only check if both exist
                if norm_key in seen_title_year:
                    original_key = seen_title_year[norm_key]
                    report.append(f"- **[Candidate]** Entry `{entry_key}` might be a duplicate of `{original_key}` (Matching Title+Year). Added note.")
                    entry['note'] += f", Duplicate Candidate of {original_key}"
                else:
                    seen_title_year[norm_key] = entry_key

        processed_entries.append(entry)

    bib_database.entries = processed_entries
    
    writer = BibTexWriter()
    writer.indent = '  '
    
    with open(output_path, 'w') as bibtex_file:
        bibtex_file.write(writer.write(bib_database))
        
    return report

if __name__ == "__main__":
    input_file = 'references.bib'
    output_file = 'cleaned_references.bib'
    
    try:
        report_lines = clean_bib_file(input_file, output_file)
        
        print("### Cleaned BibTeX Content")
        with open(output_file, 'r') as f:
            print(f.read())
            
        print("\n### Cleanup Report")
        for line in report_lines:
            print(line)
            
    except FileNotFoundError:
        print(f"Error: {input_file} not found. Please ensure the file exists.")
