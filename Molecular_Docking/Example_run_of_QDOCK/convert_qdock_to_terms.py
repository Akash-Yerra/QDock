import numpy as np
import os
# ============================================================
# STEP 1 — LOAD QUBO DATA
# ============================================================

qubo = np.load("workdir_fam/qdock_output/QUBOs/1y6r_ligand.npy", allow_pickle=True).item()

# qubo expected format:
# {
#   ('15_12_0.39000', '15_11_0.39000'): 13.74,
#   ('15_12_0.39000',): -0.78,
#   ...
# }

# ============================================================
# STEP 2 — COLLECT ALL UNIQUE VARIABLES
# ============================================================

all_variables = set()

for key in qubo.keys():

    # quadratic term
    if len(key) == 2:
        all_variables.add(key[0])
        all_variables.add(key[1])

    # linear term
    elif len(key) == 1:
        all_variables.add(key[0])

# ============================================================
# STEP 3 — SORT VARIABLES
# IMPORTANT:
# Sorting ensures deterministic numbering
# ============================================================

sorted_variables = sorted(all_variables)

# ============================================================
# STEP 4 — CREATE VARIABLE → INDEX MAP
# ============================================================

var_to_id = {}

for idx, var in enumerate(sorted_variables):
    var_to_id[var] = idx

# Example:
# {
#   '15_11_0.39000': 152,
#   '15_12_0.39000': 153
# }
# ============================================================
# STEP 5 — WRITE QUBO TERMS FILE
# ============================================================


os.makedirs(
    "workdir_fam/1y6r_Qubo/converted_qubo",
    exist_ok=True
)

with open("workdir_fam/1y6r_Qubo/converted_qubo/qubo_lhs_terms.txt", "w") as f:
    f.write("=== ALL LHS Terms ===\n")
    term_number = 1

    for key, coeff in qubo.items():

        # ----------------------------------------------------
        # QUADRATIC TERM
        # ----------------------------------------------------

        if len(key) == 2:

            v1 = var_to_id[key[0]]
            v2 = var_to_id[key[1]]

            line = (
                f"Term {term_number}: "
                f"{coeff:.3f} * x_{v1} * x_{v2}\n"
            )

        # ----------------------------------------------------
        # LINEAR TERM
        # ----------------------------------------------------

        elif len(key) == 1:

            v1 = var_to_id[key[0]]

            line = (
                f"Term {term_number}: "
                f"{coeff:.3f} * x_{v1}\n"
            )

        f.write(line)

        term_number += 1

# ============================================================
# STEP 6 — WRITE VARIABLE MAPPING FILE
# VERY IMPORTANT
# ============================================================

with open("workdir_fam/1y6r_Qubo/converted_qubo/variable_mapping.txt", "w") as f:

    for var, idx in var_to_id.items():

        f.write(f"x_{idx} -> {var}\n")

print("qubo_lhs_terms.txt generated successfully.")
print("variable_mapping.txt generated successfully.")
