https://ambermd.org/antechamber/ac.html#espgen
https://ambermd.org/doc12/Amber23.pdf


step		description

1			create esp input
2			create respin input
3			perfrom RESP calc
4			create evaluation plot, which shows the difference to the full structure


step 1
Espgen reads in a gaussian (92,94,98,03) output file and extract the electrostatic potential information and output a esp file to be read by resp program. 

Usage:
espgen 	-i   input_file_name 
		-o   output_file_name
log -> esp
		espgen -i  *.log -o only.esp 				for only structure
		use python script (CLINT/1ESP directory) 	for pairs and full structure


step 2
Respgen generates the input files for two-stage resp fitting. The current version only support single molecule fitting. Atom equivalence is recognized automatically.

Usage: 
respgen -i inputfile (ac)
	-o output file 
	-f format (resp1 or resp2) 
	   resp1 - first stage resp fitting 
	   resp2 - second stage resp fitting
ac -> respin1  	use the only respin files or manipulate them manually
ac -> respin2


step 3
resp perfomes the 2 stage fitting 

Usage:
respin1, esp -> respout1, qout_stage1
		resp -O -i *.respin1 -o *.respout1 -e *.esp -t qout_stage1
respin2, esp, qout_stage1 -> respout2, qout_stage2
		resp -O -i *.respin2 -o *.respout2 -e *.esp -q qout_stage1 -t qout_stage2
ac -> ac
		antechamber -i only_new.ac -fi ac -o sustiva_resp.ac -fo ac -c rc -cf qout_stage2
		
The above commands first generate the input files (sustiva.respin1 and sustiva.respin2) for resp fitting, then do two-stage resp fitting and finally use antechamber to read in the resp charges and write out an ac file-sustiva_resp.ac


step 4
python plot_diff.py (manually put data of qout_stage2 in array)