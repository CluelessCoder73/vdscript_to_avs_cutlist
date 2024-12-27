import re

# ----------------------------------------------------------------------
# Script: vdscript_to_avs_cutlist.py
# Description:
# This script converts VirtualDub or VirtualDub2 .vdscript files into a 
# simple text file containing an AviSynth cutlist.
# This script was tested and works with:
# - Python 3.12.5    
# - VirtualDub2 (build 44282) .vdscript files
# - AviSynth+ 3.7.3
#
# Usage:
# 1. Specify the .vdscript file path and output .txt file path.
# 2. Run the script.
#
# Example:
# VirtualDub.subset.AddRange(100,101);
# VirtualDub.subset.AddRange(400,101);
#
# Will be converted to:
# Trim(100, 200) ++ Trim(400, 500)
# ----------------------------------------------------------------------

def parse_vdscript_to_avs(vdscript_filepath, output_filepath):
    """
    Converts a .vdscript file into an AviSynth cutlist.

    Args:
        vdscript_filepath (str): Path to the .vdscript file.
        output_filepath (str): Path to save the output .txt file.
    """
    avs_cutlist = []

    with open(vdscript_filepath, 'r') as file:
        lines = file.readlines()
    
    # Regex to match VirtualDub subset lines (e.g., VirtualDub.subset.AddRange(100,101);)
    subset_pattern = re.compile(r'VirtualDub\.subset\.AddRange\((\d+),(\d+)\);')

    for line in lines:
        match = subset_pattern.match(line)
        if match:
            start_frame = int(match.group(1))
            frame_count = int(match.group(2))
            
            # Calculate AviSynth start and end frames
            avs_start = start_frame
            avs_end = start_frame + frame_count - 1  # inclusive end frame
            
            # Append to the cutlist
            avs_cutlist.append(f"Trim({avs_start}, {avs_end})")
    
    # Join the cuts with ' ++ ' to form the final AviSynth script line
    avs_script = " ++ ".join(avs_cutlist)
    
    # Write the output to a text file
    with open(output_filepath, 'w') as output_file:
        output_file.write(avs_script)
    
    print(f"AviSynth cutlist saved as {output_filepath}")

# Usage example - EDIT THESE VALUES
if __name__ == "__main__":
    vdscript_filepath = r"C:\New folder\test.vdscript"  # Path to the .vdscript file
    output_filepath = r"C:\New folder\cutlist.txt"  # Path to save the output .txt file
    
    parse_vdscript_to_avs(vdscript_filepath, output_filepath)
