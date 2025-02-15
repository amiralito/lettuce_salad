# Supporting scripts and material for "A hierarchical immune receptor network in lettuce reveals contrasting patterns of evolution in sensor and helper NLRs"

Hsuan Pai, Toshiyuki Sakai, Andres Posbeyikian, Raoul Frijters, Hiroaki Adachi, Sophien Kamoun, AmirAli Toghani


Resources:
Software                            | Source
------------------------------------| ------------------------------------
*FAMSA v2.2.2*                      | ([https://github.com/refresh-bio/FAMSA](https://github.com/refresh-bio/FAMSA))
*FastTree v2.1.10*                  | ([http://www.microbesonline.org/fasttree/](http://www.microbesonline.org/fasttree/))
*IQtree v2.3.0*                    | ([http://www.iqtree.org/](http://www.iqtree.org/))
*Dendroscope v3.8.8*                | (https://software-ab.cs.uni-tuebingen.de/download/dendroscope3/welcome.html)
*R v4.4.2*                          | ([https://cran.r-project.org/](https://cran.r-project.org/))
*NLRtracker*                        | ([https://github.com/slt666666/NLRtracker](https://github.com/slt666666/NLRtracker))



R packages:
```R
install.packages("tidyverse")
install.packages("ggseqlogo")
install.packages("entropy")
install.packages("svglite")
install.packages("pheatmap")
install.packages("reshape2")
install.packages("jsonlite")


if (!require("BiocManager", quietly = TRUE))
    install.packages("BiocManager")
BiocManager::install("Biostrings")
BiocManager::install("ggtree")
BiocManager::install("rtracklayer")
BiocManager::install("GenomicFeatures")
BiocManager::install("GenomicRanges")

```


Access the remaining supplementary data here:
[Supporting material for "A hierarchical immune receptor network in lettuce reveals contrasting patterns of evolution in sensor and helper NLRs"](https://doi.org/10.5281/zenodo.14544899)
[Deep-learning-based annotation of 230 superasterid genomes reveals a harmonized dataset of 91,366 NLRs (v250214_91366)](https://doi.org/10.5061/dryad.sxksn03d6)
