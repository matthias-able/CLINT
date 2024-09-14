# TITLE: MetaData for the PULS Group

**Internal Identifier:** README-CRW-001  
**Date of creation:** 2024-08-05  
**Creator:** Dr. Christian R. Wick, Orcid: <https://orcid.org/0000-0003-3365-0942>  
**Language:** English  


## Revision History: 

> *Date:* 2024-08-14  
>- Initial Version 
> *Date:* 2024-08-06  
>- Added File types  
>- Corrected Contact information
>
> *Date:* 2024-08-05  
>- Initial Version 


## Contact Information: 

Dr. Christian R. Wick  
*FAU Erlangen Nürnberg  
Professur f. theoretische Physik, (PULS Group)  
CAMP@EAM*  
<https://orcid.org/0000-0003-3365-0942>  
<christian.wick@fau.de>  

Prof. Dr. Ana-Suncana Smith  
*FAU Erlangen Nürnberg  
Professur f. theoretische Physik, (PULS Group)  
Competence Center Engineering of Advanced Materials (FAU EAM)*  
<https://orcid.org/0000-0002-0835-0086>  
<ana-suncana.smith@fau.de>  


## Calculation of RESP charges: 

RESP charges can be used to enhance the force field of the MD simulation.

This project automizes the calculation of RESP charges for the mPEG molecul

So, the MD simulation can be interatively run with updated charges and optimally a convergence of the RESP charges can be achieved.

1. The ionic liquid contains Iodid. Maerz-Kollman radius of Iodid is not preset by Gaussian
2. Directory 'MK_charges' contains a scan for the radius
3. Directory 'ESP' contains Gaussian ESP calculations for only the molecul, pairs of molecul plus Iodid, clusters, and the full environment
4. Directory 'RESP' contains Amber RESP calculations for only the molecul, pairs of molecul plus Iodid, and the full environment
5. main.sh executes a RESP calculation for pairs of molecul plus Iodid



## Content:

| Directory                      | Description                                                                      | 
| :----------------------------- | :------------------------------------------------------------------------------- | 
| ./ESP                          | Gaussian ESP calculations                                                        | 
| ./ESP/cluster                  | raw data                                                                         | 
| ./ESP/full                     | raw data                                                                         | 
| ./ESP/only                     | raw data                                                                         | 
| ./ESP/plusIodid                | raw data                                                                         | 

| ./MK_charges                   | Merz-Kollman radius calculations                                                 | 
| ./MK_charges/1_wide_range_scan/| Scan from 1.5 to 3.5 A                                                           | 
| ./MK_charges/2_scan_6_iodin/   | Scan from 2.10 to 3.00 A for all 6 Iodid in vicinity of mped2                    | 
| ./MK_charges/3_optimization/   | Repeated 2nd scan for optimized structures                                       | 

| ./RESP                         | Amber RESP calculations                                                          | 
| ./RESP/full                    | Amber RESP calculations for resid 701 in full QM/MM calc environment             | 
| ./RESP/only                    | Amber RESP calculations for resid 701 without any environment                    | 
| ./RESP/plus_ion                | Amber RESP calculations for resid 701 + Iodid ion in vicinity                    | 


## Naming Convention: 

None


### Workflow:
Workflow for RESP charge derivation is descriped in pseudo code in ./main.sh


### List of Programs used:

>- *Name:* **Gaussian16**,
>- *Subject:* QM calculations,
>- *Version:* 16 Rev. A03 
>- *Reference:* Frisch, M. J.; Trucks, G. W.; Schlegel, H. B.; Scuseria, G. E.; Robb, M. A.; Cheeseman, J. R.; Scalmani, G.; Barone, V.; Petersson, G. A.; Nakatsuji, H.; Li, X.; Caricato, M.; Marenich, A. V.; Bloino, J.; Janesko, B. G.; Gomperts, R.; Mennucci, B.; Hratchian, H. P.; Ortiz, J. V.; Izmaylov, A. F.; Sonnenberg, J. L.; Williams; Ding, F.; Lipparini, F.; Egidi, F.; Goings, J.; Peng, B.; Petrone, A.; Henderson, T.; Ranasinghe, D.; Zakrzewski, V. G.; Gao, J.; Rega, N.; Zheng, G.; Liang, W.; Hada, M.; Ehara, M.; Toyota, K.; Fukuda, R.; Hasegawa, J.; Ishida, M.; Nakajima, T.; Honda, Y.; Kitao, O.; Nakai, H.; Vreven, T.; Throssell, K.; Montgomery Jr., J. A.; Peralta, J. E.; Ogliaro, F.; Bearpark, M. J.; Heyd, J. J.; Brothers, E. N.; Kudin, K. N.; Staroverov, V. N.; Keith, T. A.; Kobayashi, R.; Normand, J.; Raghavachari, K.; Rendell, A. P.; Burant, J. C.; Iyengar, S. S.; Tomasi, J.; Cossi, M.; Millam, J. M.; Klene, M.; Adamo, C.; Cammi, R.; Ochterski, J. W.; Martin, R. L.; Morokuma, K.; Farkas, O.; Foresman, J. B.; Fox, D. J. Gaussian 16 Rev. A.03, 2016. 
>- *Url:* <https://www.gaussian.com> 


>- *Name:* **Amber**,
>- *Subject:* MD simulations,
>- *Version:* 2022 
>- *Reference:* Case, D. A.; Betz, R. M.; Cerutti, D. S.; Cheatham, III, T. E.; Darden, T. A.; Duke, R. E.; Giese, T. J.; Gohlke, H.; Goetz, A. W.; Homeyer, N.; Izadi, S.; Janowski, P.; Kaus, J.; Kovalenko, A.; Lee, T. S.; LeGrand, S.; Li, P.; Lin, C.; Luchko, T.; Luo, R.; Madej, B.; Merz, K. M.; Monard, G.; Nguyen, H.; Nguyen, H. T.; Omelyan, I.; Onufriev, A.; Roe, D. R.; Roitberg, A.; Sagui, C.; Simmerling, C. L.; Botello-Smith, W. M.; Swails, J.; Walker, R. C.; Wang, J.; Wolf, R. M.; Wu, X.; Xiao, L.; Kollman, P. A. AMBER 2016, 2016. 
>- *Url:* <https://www.ambermd.org> 


### List of FileTypes used:

| Extension  | Description                                                  | 
| :--------- | :----------------------------------------------------------- | 
| '.png'     | PNG image format                                             | 
| '.py'      | Python script                                                | 
| '.sh'      | Shell script                                                 | 
| '.xyz'     | xyz molecular format                                         | 
| '.mol2'    | mol2 molecular format                                        | 
| '.pdb'     | PDB (Protein Data Bank) molecular format                     | 
| '.log'     | Gaussian / Amber log file                                    | 
| '.out'     | Orca / Gaussian log file                                     | 
| '.com'     | Gaussian input file                                          | 
| '.chk'     | Gaussian checkpoint file                                     | 
| '.top'     | Gromacs Topology                                             | 
| '.gro'     | Gromacs Gro file                                             | 
| '.prmtop'  | Amber Topology file                                          | 


## DATA-SPECIFIC information for: 'CRW-RhCO2X_1minus-001.com'
the inital structure was taken from [mPEG][I] simulation 17conf charge fitting, iodide parameters from li-merz-iod set.



## Funders:

> Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) - 377472739/GRK 2423/2-2023 FRASCAL.    
> Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – Project-ID 431791331 – SFB 1452 (CLINT Catalysis at Liquid Interfaces)    
> Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – Project-ID 416229255 – SFB 1411 (Design of Particulate Products)   


## Licence: 

Creative Commons Attribution 4.0 International 


## Refernces

1. Zhai, Z.; Hantal, G.; Cherian, A.; Bergen, A.; Chu, J.; Wick, C. R.; Meyer, K.; Smith, A.-S.; Koller, T. M. Influence of Molecular Hydrogen on Bulk and Interfacial Properties of Three Imidazolium-Based Ionic Liquids by Experiments and Molecular Dynamics Simulations. International Journal of Hydrogen Energy 2024, 72, 1091–1104. https://doi.org/10.1016/j.ijhydene.2024.05.249.

