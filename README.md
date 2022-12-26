## Neuron tracking

This project was born as the final task during the Intro to Computer Vision course at Skoltech.

Studying images from a confocal microscope, acute brain slices have a tendency to fluctuate, which is why the coordinates of ROI (cells) are unstable.
My role was to detect the bodies of neurons and track them throughout the recording time.

### Data source and scientific  reasoning
The images from the confocal microscope have 3 sources, in this case recorded at 420 and 500 nm, which is significant because the protein called Hydrogen peroxide sensor (HyPer) has two maxima in fluorescence at these specific channels. This protein is capable of detecting intracellular hydrogen peroxide and when it is present, HyPer starts to fluorescent. By this fluorescence, we can determine whether our genetic construct containing the HyPer gene is in the neuron cell.

### Neurons bodies detection


![Initial frame of neurons](https://user-images.githubusercontent.com/70488161/209572605-7a19b012-fd33-454c-96c7-0f0f513b40fd.png)

