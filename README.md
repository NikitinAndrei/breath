# Breath classification and Segmentation
## Classification
Initial plan was to see if a matching filter with an reference signal is comparable with similar working filter based on a neuronet  
Neuroner was showing decent results that are better than a matching filter, but was completely failing segmentation task.

But anyway, augmentation funcitons have been developed and with a little modifications were implemented in segmentation tasks

## Segmentation
I cannot share any of successful models due to the agreement with previous employer, but the code and archtecture is here. The architecture is a little bit messy, because I was constantly checking, how such factors as amount of layers and levels of U-Net were affecting the resulting models.
Some of them were quite successful, but was not implemented due to political situation and financing issues.