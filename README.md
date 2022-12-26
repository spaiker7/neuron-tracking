## Neuron tracking

This project was born as the final task during the Intro to Computer Vision course at Skoltech.

Studying images from a confocal microscope, acute brain slices have a tendency to fluctuate, which is why the coordinates of ROI (cells) are unstable.
My role was to detect the bodies of neurons and track them throughout the recording time.

### Data source and scientific  reasoning
The images from the confocal microscope have 3 sources, in this case recorded at 420 and 500 nm, which is significant because the protein called Hydrogen peroxide sensor (HyPer) has two maxima in fluorescence at these specific channels. This protein is capable of detecting intracellular hydrogen peroxide and when it is present, HyPer starts to fluorescent. By this fluorescence, we can determine whether our genetic construct containing the HyPer gene is in the neuron cell.

![hyper](https://user-images.githubusercontent.com/70488161/209573360-f0c2f6ba-ae8e-43d7-b144-2fa259477207.png)


### Neurons bodies detection

- Normalizing scale (intensity) of the channel
- Denoizing + adaptive threshold
- Morphology playing
- Watershed segmentation of clumped cells
- Mask extraction


![Initial frame of neurons](https://user-images.githubusercontent.com/70488161/209572605-7a19b012-fd33-454c-96c7-0f0f513b40fd.png) ![Mask](https://user-images.githubusercontent.com/70488161/209572705-83ef2d64-4c40-4962-9b94-4d91a6c6f17a.png)


### Tracking detected ROI through the time

The further problem has the Object Tracking Open CV realization that uses previuos frame in video where the obect has moved. From each cell contour we extracted the bounding boxes and trained the Boosting MultiTracker 
