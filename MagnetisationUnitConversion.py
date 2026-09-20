# -*- coding: utf-8 -*-
"""
@author: pycbr
"""
#Lines 31 or 34 need to be uncommented depending on desired conversion

NumberOfAtoms = 1  #Number of magnetic atoms in unit cell
Volume = 600 #Volume of unit cell in A^3 
muB = 9.274E-24 #Bohr Magneton in J/T

MomentPerAtom = 2.1 #In units of Bohr Magnetons
EmuPerVolume = 700 #In units of emu/cm^3

def emu2bohr(EmuPerVolume, Volume, NumberOfAtoms):
     """Convert from magnetisation in Emu/cm^3 to magnetisation in Bohr-
     magnetons per atom.

    This function calculates the critical voltage, IcRn, as a function of 
    ferromagnetic thickness of the weak link as presented in the Eq A10 of the 
    paper by Buzdin et al: https://link.aps.org/doi/10.1103/RevModPhys.77.935.

    Args:
        d_F (numpy.ndarray): List of (float) thicknesses of the ferromagnetic junction (nm).            
        Temperature (float): Temperature of the system (K).
        T_c (float): Critical temperature of the superconductor (K).       
        H (float): Exchange energy in the ferromagnet (eV).        
        SC_gap (float): Superconducting gap (eV).       
        alpha (float): Magnetic scattering parameter defined as 1/(h*tau_s) (unitless).        
        CoherenceLength (float): Coherence length in the ferromagnet (nm).      
        DeadLayer (float): Thickness of dead (non-magnetic) material in the ferromagnet. 
            Negative values indicate increased effective ferromagnetic thickness 
            due to proximity magnetisation in the normal metal (nm).         
        Amplitude (float): If provided, can be used to set an arbitrary scaled
            amplitude for the output (unitless).
            
    Returns:
        IcRn (float): Critical voltage of the Josephson junction (uV).

    Notes:
    """
    
    MagOutput = (EmuPerVolume*Volume*1E-24*1E-3)/(muB*NumberOfAtoms)

    return MagOutput
    

def bohr2emu(MomentPerAtom, Volume, NumberOfAtoms):
    
    MagOutput = (NumberOfAtoms*MomentPerAtom*muB*1E3)/(Volume*1E-24)
    
    return MagOutput


#####  Uncomment whichever conversion you want to use:   #####

#emu/cm^3 to bohr magneton's per atom:
#Output = [emu2bohr(EmuPerVolume, Volume, NumberOfAtoms),'muB/atom']

#bohr magneton's per atom to emu/cm^3:
#Output = [bohr2emu(MomentPerAtom, Volume, NumberOfAtoms),'emu/cm^3']

##############################################################

print("The magnetisation is", Output[0],Output[1])
