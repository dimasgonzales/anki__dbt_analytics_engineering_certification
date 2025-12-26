# /// script
# dependencies = [
#   "genanki",
#   "pyyaml",
#   "markdown",
#   "Pygments",
#   "requests",
# ]
# ///

import genanki
import os
import re
import yaml
import random
import glob
import markdown
import requests
import json

# 1. Define a Model (Note Type)
# Models require a unique ID
MODEL_ID = 1607392319
DECK_ID = 2059400110

# CSS for the card, including syntax highlighting
CSS = """
.card {
 font-family: arial;
 font-size: 20px;
 text-align: center;
 color: black;
 background-color: white;
}

/* Code block styling */
pre {
 text-align: left;
 background-color: #f4f4f4;
 padding: 10px;
 border-radius: 5px;
 overflow-x: auto;
}

code {
 font-family: monospace;
 background-color: #f4f4f4;
 padding: 2px 4px;
 border-radius: 3px;
}

/* Pygments (codehilite) default styles - simplified */
.codehilite .hll { background-color: #ffffcc }
.codehilite .c { color: #408080; font-style: italic } /* Comment */
.codehilite .err { border: 1px solid #FF0000 } /* Error */
.codehilite .k { color: #008000; font-weight: bold } /* Keyword */
.codehilite .o { color: #666666 } /* Operator */
.codehilite .ch { color: #408080; font-style: italic } /* Comment.Hashbang */
.codehilite .cm { color: #408080; font-style: italic } /* Comment.Multiline */
.codehilite .cp { color: #BC7A00 } /* Comment.Preproc */
.codehilite .cpf { color: #408080; font-style: italic } /* Comment.PreprocFile */
.codehilite .c1 { color: #408080; font-style: italic } /* Comment.Single */
.codehilite .cs { color: #408080; font-style: italic } /* Comment.Special */
.codehilite .gd { color: #A00000 } /* Generic.Deleted */
.codehilite .ge { font-style: italic } /* Generic.Emph */
.codehilite .gr { color: #FF0000 } /* Generic.Error */
.codehilite .gh { color: #000080; font-weight: bold } /* Generic.Heading */
.codehilite .gi { color: #00A000 } /* Generic.Inserted */
.codehilite .go { color: #888888 } /* Generic.Output */
.codehilite .gp { color: #000080; font-weight: bold } /* Generic.Prompt */
.codehilite .gs { font-weight: bold } /* Generic.Strong */
.codehilite .gu { color: #800080; font-weight: bold } /* Generic.Subheading */
.codehilite .gt { color: #0044DD } /* Generic.Traceback */
.codehilite .kc { color: #008000; font-weight: bold } /* Keyword.Constant */
.codehilite .kd { color: #008000; font-weight: bold } /* Keyword.Declaration */
.codehilite .kn { color: #008000; font-weight: bold } /* Keyword.Namespace */
.codehilite .kp { color: #008000 } /* Keyword.Pseudo */
.codehilite .kr { color: #008000; font-weight: bold } /* Keyword.Reserved */
.codehilite .kt { color: #B00040 } /* Keyword.Type */
.codehilite .m { color: #666666 } /* Literal.Number */
.codehilite .s { color: #BA2121 } /* Literal.String */
.codehilite .na { color: #7D9029 } /* Name.Attribute */
.codehilite .nb { color: #008000 } /* Name.Builtin */
.codehilite .nc { color: #0000FF; font-weight: bold } /* Name.Class */
.codehilite .no { color: #880000 } /* Name.Constant */
.codehilite .nd { color: #AA22FF } /* Name.Decorator */
.codehilite .ni { color: #999999; font-weight: bold } /* Name.Entity */
.codehilite .ne { color: #D2413A; font-weight: bold } /* Name.Exception */
.codehilite .nf { color: #0000FF } /* Name.Function */
.codehilite .nl { color: #A0A000 } /* Name.Label */
.codehilite .nn { color: #0000FF; font-weight: bold } /* Name.Namespace */
.codehilite .nt { color: #008000; font-weight: bold } /* Name.Tag */
.codehilite .nv { color: #19177C } /* Name.Variable */
.codehilite .ow { color: #AA22FF; font-weight: bold } /* Operator.Word */
.codehilite .w { color: #bbbbbb } /* Text.Whitespace */
.codehilite .mb { color: #666666 } /* Literal.Number.Bin */
.codehilite .mf { color: #666666 } /* Literal.Number.Float */
.codehilite .mh { color: #666666 } /* Literal.Number.Hex */
.codehilite .mi { color: #666666 } /* Literal.Number.Integer */
.codehilite .mo { color: #666666 } /* Literal.Number.Oct */
.codehilite .sa { color: #BA2121 } /* Literal.String.Affix */
.codehilite .sb { color: #BA2121 } /* Literal.String.Backtick */
.codehilite .sc { color: #BA2121 } /* Literal.String.Char */
.codehilite .dl { color: #BA2121 } /* Literal.String.Delimiter */
.codehilite .sd { color: #BA2121; font-style: italic } /* Literal.String.Doc */
.codehilite .s2 { color: #BA2121 } /* Literal.String.Double */
.codehilite .se { color: #BB6622; font-weight: bold } /* Literal.String.Escape */
.codehilite .sh { color: #BA2121 } /* Literal.String.Heredoc */
.codehilite .si { color: #BB6688; font-weight: bold } /* Literal.String.Interpol */
.codehilite .sx { color: #008000 } /* Literal.String.Other */
.codehilite .sr { color: #BB6688 } /* Literal.String.Regex */
.codehilite .s1 { color: #BA2121 } /* Literal.String.Single */
.codehilite .ss { color: #19177C } /* Literal.String.Symbol */
.codehilite .bp { color: #008000 } /* Name.Builtin.Pseudo */
.codehilite .fm { color: #0000FF } /* Name.Function.Magic */
.codehilite .vc { color: #19177C } /* Name.Variable.Class */
.codehilite .vg { color: #19177C } /* Name.Variable.Global */
.codehilite .vi { color: #19177C } /* Name.Variable.Instance */
.codehilite .vm { color: #19177C } /* Name.Variable.Magic */
.codehilite .il { color: #666666 } /* Literal.Number.Integer.Long */

/* Table styling */
table {
 border-collapse: collapse;
 width: 100%;
 margin: 10px 0;
}
th, td {
 border: 1px solid #ddd;
 padding: 8px;
}
th {
 background-color: #f2f2f2;
 font-weight: bold;
}

/* Admonition styling */
.admonition {
 border: 1px solid #ddd;
 border-radius: 4px;
 margin: 10px 0;
 padding: 10px;
 text-align: left;
 background-color: #fafafa;
}
.admonition-title {
 font-weight: bold;
 margin-bottom: 5px;
}
.admonition.note { border-left: 5px solid #448aff; }
.admonition.warning { border-left: 5px solid #ff9100; }
.admonition.danger { border-left: 5px solid #ff1744; }
.admonition.tip { border-left: 5px solid #00c853; }
"""

my_model = genanki.Model(
  MODEL_ID,
  'Simple Model',
  fields=[
    {'name': 'Question'},
    {'name': 'Answer'},
  ],
  templates=[
    {
      'name': 'Card 1',
      'qfmt': '{{Question}}',
      'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
    },
  ],
  css=CSS,
)

# 3. Define a Deck
my_deck = genanki.Deck(
  DECK_ID,
  'dbt flashcards', # You might want to change this name
)

def parse_flashcard(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split frontmatter and content
    # Assuming frontmatter is between first two ---
    parts = re.split(r'^---\s*$', content, maxsplit=2, flags=re.MULTILINE)
    
    tags = []
    if len(parts) >= 3:
        frontmatter_str = parts[1]
        body = parts[2]
        try:
            frontmatter = yaml.safe_load(frontmatter_str)
            if frontmatter and 'tags' in frontmatter:
                tags = frontmatter['tags']
                # Convert hierarchical tags
                tags = [tag.replace('/', '::') for tag in tags]
            
            # Check verdict
            if frontmatter and 'claim_meta' in frontmatter:
                verdict = frontmatter['claim_meta'].get('verdict')
                if verdict != 'SUPPORTED':
                    # return None early if not supported
                    return None

        except yaml.YAMLError as e:
            print(f"Error parsing YAML in {filepath}: {e}")
    else:
        body = content

    # Extract Front and Back
    # Looking for <front>...</front> and <back>...</back>
    front_match = re.search(r'<front>(.*?)</front>', body, re.DOTALL)
    back_match = re.search(r'<back>(.*?)</back>', body, re.DOTALL)

    if front_match and back_match:
        question = front_match.group(1).strip()
        answer = back_match.group(1).strip()
        
        if 'claim_meta' in frontmatter:
            verdict = frontmatter['claim_meta'].get('verdict')
            if verdict != 'SUPPORTED':
                print(f"Skipping {filepath}: Verdict is {verdict}")
                return None
        
        # Convert markdown to HTML with extensions
        question_html = markdown.markdown(
            question, 
            extensions=['fenced_code', 'codehilite', 'nl2br', 'tables', 'admonition']
        )
        answer_html = markdown.markdown(
            answer, 
            extensions=['fenced_code', 'codehilite', 'nl2br', 'tables', 'admonition']
        )

        return {
            'question': question_html,
            'answer': answer_html,
            'tags': tags
        }
    else:
        print(f"Skipping {filepath}: Could not find <front> and <back> tags.")
        return None

def sync_with_anki(apkg_path):
    """Notifies local Anki instance to import the generated package."""
    try:
        # AnkiConnect default URL
        url = "http://localhost:8765"
        
        payload = {
            "action": "importPackage",
            "version": 6,
            "params": {
                "path": os.path.abspath(apkg_path)
            }
        }
        
        response = requests.post(url, json=payload)
        result = response.json()
        
        if result.get("error"):
            print(f"AnkiConnect Error: {result['error']}")
        else:
            print(f"Successfully synced {apkg_path} to Anki!")
            
    except requests.exceptions.ConnectionError:
        print("Could not connect to Anki. Is it running and is AnkiConnect installed?")

def main():
    deck_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'deck')
    output_file = 'output_deck.apkg'
    
    print(f"Scanning directory: {deck_dir}")

    files = glob.glob(os.path.join(deck_dir, '*.md'))
    
    count = 0
    for filepath in files:
        card_data = parse_flashcard(filepath)
        if card_data:
            my_note = genanki.Note(
                model=my_model,
                fields=[card_data['question'], card_data['answer']],
                tags=card_data['tags']
            )
            my_deck.add_note(my_note)
            count += 1

    print(f"Added {count} notes to deck.")
    
    genanki.Package(my_deck).write_to_file(output_file)
    print(f"Deck generated: {output_file}")

    sync_with_anki(output_file)

if __name__ == '__main__':
    main()
