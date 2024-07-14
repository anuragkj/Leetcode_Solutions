class Solution:
    def countOfAtoms(self, formula: str) -> str:
        # Length of the formula
        n = len(formula)

        # Current index. It should be global as needs
        # to be updated in the recursive function
        self.index = 0

        # Recursively parse the formula
        def parse_formula():
            # Local variable
            curr_map = defaultdict(int)
            curr_atom = ""
            curr_count = ""

            # Iterate until the end of the formula
            while self.index < n:
                # UPPERCASE LETTER
                if formula[self.index].isupper():
                    # Save the previous atom and count
                    if curr_atom:
                        if curr_count == "":
                            curr_map[curr_atom] += 1
                        else:
                            curr_map[curr_atom] += int(curr_count)

                    curr_atom = formula[self.index]
                    curr_count = ""
                    self.index += 1

                # lowercase letter
                elif formula[self.index].islower():
                    curr_atom += formula[self.index]
                    self.index += 1

                # Digit. Concatenate the count
                elif formula[self.index].isdigit():
                    curr_count += formula[self.index]
                    self.index += 1

                # Left Parenthesis
                elif formula[self.index] == "(":
                    self.index += 1
                    nested_map = parse_formula()
                    for atom in nested_map:
                        curr_map[atom] += nested_map[atom]

                # Right Parenthesis
                elif formula[self.index] == ")":
                    # Save the last atom and count of nested formula
                    if curr_atom:
                        if curr_count == "":
                            curr_map[curr_atom] += 1
                        else:
                            curr_map[curr_atom] += int(curr_count)

                    self.index += 1
                    multiplier = ""
                    while self.index < n and formula[self.index].isdigit():
                        multiplier += formula[self.index]
                        self.index += 1
                    if multiplier:
                        multiplier = int(multiplier)
                        for atom in curr_map:
                            curr_map[atom] *= multiplier

                    return curr_map

            # Save the last atom and count
            if curr_atom:
                if curr_count == "":
                    curr_map[curr_atom] += 1
                else:
                    curr_map[curr_atom] += int(curr_count)

            return curr_map

        # Parse the formula
        final_map = parse_formula()

        # Sort the final map
        final_map = dict(sorted(final_map.items()))

        # Generate the answer string
        ans = ""
        for atom in final_map:
            ans += atom
            if final_map[atom] > 1:
                ans += str(final_map[atom])

        return ans
