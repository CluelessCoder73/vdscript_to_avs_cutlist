# vdscript_to_avs_cutlist
This script converts VirtualDub or VirtualDub2 "vdscript" files into a simple text file containing an AviSynth cutlist.
This script was tested and works with:
- Python 3.12.5    
- VirtualDub2 (build 44282) .vdscript files
- AviSynth+ 3.7.3

Usage:
1. Specify the .vdscript file path and output .txt file path.
2. Run the script.

Example:
VirtualDub.subset.AddRange(100,101);
VirtualDub.subset.AddRange(400,101);

Will be converted to:
Trim(100, 200) ++ Trim(400, 500)