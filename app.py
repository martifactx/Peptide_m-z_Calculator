import streamlit as st
from pyopenms import AASequence

# Define the proton mass (in Daltons)
PROTON_MASS = 1.007276466812

def calculate_mz(sequence: str, charge: int) -> float:
    """
    Calculate the m/z ratio for a given peptide sequence and charge.
    
    Args:
        sequence (str): The peptide sequence (e.g., "ACDEFGHIK").
        charge (int): The charge state.
    
    Returns:
        float: The computed m/z value.
    """
    # Create an AASequence object from the sequence string
    try:
        aa_seq = AASequence.fromString(sequence)
    except Exception as e:
        raise ValueError(f"Invalid peptide sequence: {sequence}") from e
    
    # Get the monoisotopic mass of the peptide
    peptide_mass = aa_seq.getMonoWeight()
    
    # Calculate m/z using the formula:
    # m/z = (peptide_mass + (charge * proton_mass)) / charge
    mz = (peptide_mass + charge * PROTON_MASS) / charge
    return mz

# Streamlit UI

st.title("Peptide m/z Calculator")

st.markdown("""
This tool calculates the mass-to-charge (m/z) ratio for a peptide based on its sequence and charge state.
Enter your peptide sequence (e.g., **ACDEFGHIK**) and select the charge state.
""")

# User input: peptide sequence
peptide_sequence = st.text_input("Peptide Sequence", value="ACDEFGHIK")

# User input: charge state
charge_state = st.number_input("Charge State", min_value=1, step=1, value=1)

if st.button("Calculate m/z"):
    try:
        mz_value = calculate_mz(peptide_sequence, int(charge_state))
        st.success(f"Calculated m/z: **{mz_value:.4f}**")
    except Exception as e:
        st.error(f"Error: {e}")
 

 

    
 
    
    




