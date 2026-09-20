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

    This function recieves the magnetisation in emu per cm^3 and uses the
    known volume and number of magnetic atoms in the unit cell to convert
    into the magnetisation in Bohr-magnetons.

    Args:        
        EmuPerVolume (float): Input magnetisation (emu/cm^3).
        Volume (float): Unit cell volume (cm^3).       
        NumberOfAtoms (float): Number of atoms in the unitcell (unitless).        
            
    Returns:
        MagOutput (float): Output magnetisation (J/T).

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
