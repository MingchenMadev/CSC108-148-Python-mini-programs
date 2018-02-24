"""
A pronunciation dictionary: dict of {str: list of str}
  - each key is a word (a str)
  - each value is a list of phonemes for that word (a list of str)
"""


def read_pronunciation(pronunciation_file):
    """ (file open for reading) -> pronunciation dictionary

    Read pronunciation_file, which is in the format of the CMU Pronouncing
    Dictionary, and return the pronunciation dictionary.
    """

    d = {}
    for line in pronunciation_file:
        if line.strip() != '':
            ls = line.split()
            if ls[0] != ';;;' 
                d[ls[0]] = [ls[1:]]
    return d

def read_poetry_form_description(poetry_forms_file):
    """ (file open for reading) -> poetry pattern

    Precondition: we have just read a poetry form name from poetry_forms_file.

    Return the next poetry pattern from poetry_forms_file.
    """

    result1 = []
    result2 = []
    for line in poetry_forms_file:
        if line.strip() == '':
            result = (result1, result2)
            return result
        else:
            ls = line.split()
            result1.append(ls[0])
            result2.append(ls[1])

def read_poetry_form_descriptions(poetry_forms_file):
    """ (file open for reading) -> dict of {str: poetry pattern}

    Return a dictionary of poetry form name to poetry pattern for the
    poetry forms in poetry_forms_file.
    """

    d = {}
    name = ''
    for line in poetry_forms_file:
        if line.strip() != '':
            name = line.split()[0]
        if name != '':
            d[name] = read_poetry_form_description(poetry_forms_file)
            name = ''
    return d
        


