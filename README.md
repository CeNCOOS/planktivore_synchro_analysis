# Planktivore Image Analysis #

Images collected from a Synchrom LRAUV campaign equipped with the Planktivore imaging instrument.

Dataset contains 70k+ images

<span style='vertical-align:middle; display:inline;'>
<img src="example_images/LRAH12_20240418T081447.781425Z_PTVR02HM_570788_4_634_346_0_88_172_0_rawcolor.png">
<img src="example_images/LRAH12_20240418T073550.737041Z_PTVR02HM_547415_10_1670_1182_0_228_328_0_rawcolor.png">
<img src="example_images/LRAH12_20240419T090730.687888Z_PTVR02HM_554802_23_806_418_0_188_340_0_rawcolor.png">
<img src="example_images/LRAH12_20240418T063546.737099Z_PTVR02HM_511371_2_1780_1148_0_164_148_0_rawcolor.png">
</span>

---
## Content ##

- `planktivore_unzip_pngs.py`: Unzips .zip achives to remove the .png, jpg, or image masks.
- `planktivore_mean_color.ipynb`: Analyzes the mean color for the datasets.
- `planktivore_train_clusters.py`: This script will generate and save clusters based on the conditions set in the `main()` function
- `planktivore_custerImage.ipynb`: Using the ClusterImage package to analyze the different unsupervised clustering methods and feature extractions on the images

## Results ##
__Mean Color__  
(R=0.1350966  G=0.12162398 B=0.12369811)  
<img src="./figures/mean_color.png" width=300px>  

<img src="./figures/PCA_explained_var.png">
