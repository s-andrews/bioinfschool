#!C:/Program Files/Python36/Python
import cgi
import cgitb
cgitb.enable()
import os
import re

def main():
    form = cgi.FieldStorage()
    if ("mutation" in form):
        answer = find_mutation_effect(form["mutation"].value)
        print_answer(answer)
    else:
        print_query_form()

def read_translation_table():
    translation_file = os.path.join(os.path.dirname(__file__),"../../Data/translation_table.txt")

    translation_table = {}

    with open(translation_file) as file:
        for line in file:
            line = line.strip()

            sections = line.split()

            translation_table[sections[0]] = sections[1]

    return(translation_table)


def translate (sequence):
    translation_table = read_translation_table()

    protein = ""

    print("Sequence length is {}".format(len(sequence)//3))

    for i in range(0,len(sequence)//3):
        codon = sequence[i*3:(i*3)+3]
        aa = translation_table[codon]

        if aa == "*":
            return(protein)

        protein += aa

    return(protein)


def read_gene():
    reffile = os.path.join(os.path.dirname(__file__),"../../Data/transcript_sequence.txt")

    sequence = ""

    with open(reffile) as file:
        for line in file:

            line = line.strip()

            if line[0] == ">":
                # It's the header line
                continue
            else:
                sequence += line

    return(sequence)


def find_mutation_effect(mutation):
    transcript_sequence = read_gene()
    protein_sequence = translate(transcript_sequence)

    mut_pattern = re.compile("([GATC])(\d+)([GATC])")

    mut_match = mut_pattern.match(mutation)

    # TODO: Check for a mut_match

    start_base = mut_match.group(1)
    mut_position = int(mut_match.group(2))
    end_base = mut_match.group(3)

    mutable_sequence = list(transcript_sequence)

    mutable_sequence[mut_position] = end_base

    mutated_sequence = "".join(mutable_sequence)

    mutated_protein = translate(mutated_sequence)

    if protein_sequence == mutated_protein:
        return("silent mutation")

    elif len(protein_sequence) != len(mutated_protein):
        return("nonsense mutation")

    else:
        return("protein coding change")

def print_query_form():
    template = os.path.join(os.path.dirname(__file__),"../../Templates/resistance_input.html")

    with open(template) as file:
        for line in file:
            print(line)

def print_answer(answer):
    template = os.path.join(os.path.dirname(__file__),"../../Templates/resistance_answer.html")

    template_text = ""
    with open(template) as file:
        for line in file:
            template_text += line

    print (template_text.format(effect=answer))



if (__name__ == "__main__"):
    main()
