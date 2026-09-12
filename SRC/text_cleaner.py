# clean the text 

import re

def clean_text(text):

    # Remove the multiples lines 

    text = re.sub(r'\n+','\n',text)

    # Remove the extra spaces 
    
    text = re.sub(r' +',' ',text)

    # Remove the spaces at the begining and end

    text = text.strip()

    return text