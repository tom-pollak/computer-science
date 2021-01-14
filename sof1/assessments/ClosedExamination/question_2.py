import re


def molecule_to_list(molecule):
    atom_list = []
    # Splits into each element e.g. C or O2
    atom_pattern = re.compile('[A-Z][a-z]*[0-9]*')
    atoms = atom_pattern.findall(molecule)

    # If re dosent use every character then invalid molecule
    if ''.join(atoms) != molecule:
        raise ValueError('Invalid molecule')

    for atom in atoms:
        # Splits characters and number in atom e.g. C10 -> ['C', '10']
        split_atom = re.split('([0-9]+)$', atom)
        if len(split_atom) == 1:
            split_atom.append(1)
        atom_list.append((split_atom[0], int(split_atom[1])))
    return atom_list
