# VVV_parser
Takes large viva view file sets and pushes them around.
This script takes files from the Olympus VivaView using MetaMorph and organizes them into subfolders based on filter (GFP, RFP, and DIC) as well as stage position (ie, you'll get folders like GFP_S1 as the output). You should calculate the number of stage positions as the number of stage positions per plate, times the number of plates. So if you have 3 stage positions and 4 plates, the number of stage positions is 12 (i.e., does not work if you have checked "Break up into multiple files based on sample loader position". Don't blame me, blame the way MetaMorph names things. It only works for windows right now, sorry. 
