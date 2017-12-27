Spatiotemporal Domain Decomposition Readme

Relevant literature:
Hohl, A., Delmelle, E. M., & Tang, W. (2015). Spatiotemporal domain decomposition for massive parallel computation of space-time kernel density. ISPRS Annals of the Photogrammetry, Remote Sensing and Spatial Information Sciences, 2(4), 7.
Hohl, A., Delmelle, E., Tang, W., & Casas, I. (2016). Accelerating the discovery of space-time patterns of infectious diseases using parallel computing. Spatial and spatio-temporal epidemiology, 19, 10-20.
Hohl, A., Casas, I., Delmelle, E., & Tang, W. (2016, January). Hybrid Indexing for Parallel Analysis of Spatiotemporal Point Patterns. In International Conference on GIScience Short Paper Proceedings (Vol. 1, No. 1).

Files:
main.py - reads data and parameter files, creates directories, starts decomposition
settings.py - initiates global variables
decomposition.py - performs recursive octree-based decomposition of the spatiotemporal domain
assignment.py - assigns data points to their respective subdomains
files/data.txt - contains 1000 random data points used in this example. Each point has 3 coordinates (2 spatial & 1 temporal)
files/parameterFile.txt - contains 6 parameter values relevant for decomposition

Procedure:
Dump the entire repository in a directory, execute main.py
It creates two directories: 
1) pointFiles - The result of the decomposition is stored here:  Each resulting subdomain corresponds to a textfile that stores the coordinates of data points that lie within.
2) timeFiles - Stores decomposition execution time
