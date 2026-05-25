from QDock.feature_atom_mapping.qdock import FAMDock
import os
fam = FAMDock()

# Prepare receptor
receptor_path = os.path.abspath(
    "data/1y6r_protein.pdb"
)

fam.make_receptor(receptor_path)

# Prepare ligand
ligand_path = os.path.abspath(
    "1y6r_ligand.mol2"
)
fam.make_ligand([ligand_path])

# Define docking box
fam.make_box_ligand(ligand_path)

# Run docking
poses = fam.dock(
    edge_cutoff=1.0,
    K_dist=2.0,
    K_mono=2.0,
    n_pos=30,
    save_qubo=True,
    sim_dock=True,
    save_match=True,
    save_pose=True,
)

print(poses)
