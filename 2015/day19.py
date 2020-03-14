from re import findall, finditer

input = open('2015/inputs/day19.txt').read()

def replace(molecule, match, mol_out):
    return molecule[:match.start()] + mol_out + molecule[match.end():]

def part1(s):
    replacements_data = findall(r'(\w+) => (\w+)', s)
    replacements = [(mol_in, mol_out) for mol_in, mol_out in replacements_data]
    molecule = s.split()[-1]

    return len(set(replace(molecule, m, mol_out) 
            for mol_in, mol_out in replacements 
            for m in finditer(mol_in, molecule)))

print(part1(input))
