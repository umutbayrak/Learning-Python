# Learning-Python---Isomers
An exercise from Python class

In chemistry, isomers are compounds that have the same number of atoms of each element, but that differ in the way these atoms are interconnected and arranged. In other words, isomers are compounds with the same molecular formula but different structural formulas (a compound is also an isomer of itself). Isomers usually have different chemical properties.

Ethanol (an alcohol) and dimethyl ether, for example, each consist of 6 hydrogen atoms, two carbon atoms, and an oxygen atom. Only the order of the chemical bonds is different. Both compounds share the same molecular formula (C2H6O) but have different structural formulas.

There are various standards that represent the structural formula of a compound as a string. You may assume that the atoms in such a string representation are symbolically named by an uppercase letter, possibly followed by a number of lowercase letters. The difference between uppercase and lowercase letters is important: the string PB represents one phosphorus atom (P) and one boron atom (B), while the string Pb represents one atom of lead. In addition, in between symbolic names of different atoms there might be other characters, such as in Na-OH or (CHHH)CO(CHHH). No other characters may occur in between the uppercase letter and the lowercase letters of the symbolic name of an atom.

Assignment

Write a function molecularFormula that takes the string representation of a structural formula of a particular compound. The function must return a dictionary, whose keys are the symbolic names of all atoms occurring in the given structural formula. The value that corresponds with a key indicates the number of occurrences of the atom in the given structural formula. For example, if the string (CHHH)CO(CHHH) is passed, the function must return the dictionary {'H': 6, 'C': 3, 'O': 1}. Note that this dictionary actually represents the molecular formula that corresponds to the given structural formula, hence the name of the function.

Use the function molecularFormula to write a function isomers. This function takes two string representations of structural formulas. The function must return a Boolean value that indicates whether the compounds that correspond with the given structural formulas are isomers.
