#!C:/Program Files/Python36/Python
import cgi
import cgitb
cgitb.enable()
import os

def main():
    form = cgi.FieldStorage()
    if ("sequence" in form):
        answer = search_sequence(form["sequence"].value)
        print_answer(answer)
    else:
        print_query_form()

def read_references():
    reffile = os.path.join(os.path.dirname(__file__),"../../Data/reference_sequences.txt")

    references = []

    current_reference = {"name":"","sequence":""}

    with open(reffile) as file:
        for line in file:

            line = line.strip()

            if line == "--":
                # We're at the end of an entry
                references.append(current_reference)
                current_reference = {"name":"","sequence":""}
            elif line[0] == ">":
                # We have the header line
                current_reference["name"] = line[1:]
            else:
                current_reference["sequence"] += line

    return(references)

def search_sequence(sequence):
    references = read_references()

    for reference in references:
        if sequence in reference["sequence"]:
            return(reference)

    return None

def print_query_form():
    template = os.path.join(os.path.dirname(__file__),"../../Templates/beefburger_input.html")

    with open(template) as file:
        for line in file:
            print(line)

def print_answer(answer):
    template = os.path.join(os.path.dirname(__file__),"../../Templates/beefburger_answer.html")

    template_text = ""
    with open(template) as file:
        for line in file:
            template_text += line

    print (template_text.format(animal=answer["name"]))



if (__name__ == "__main__"):
    main()
