import static qupath.lib.gui.scripting.QPEx.*

// run script for multiple images in project
// select whole image
// get mean intensity value for DAPI

setImageType('FLUORESCENCE');
createSelectAllObject(true);
selectAnnotations();
runPlugin('qupath.lib.algorithms.IntensityFeaturesPlugin', '{"pixelSizeMicrons": 2.0,  "region": "ROI",  "tileSizeMicrons": 25.0,  "channel1": true,  "channel2": false,  "channel3": false,  "channel4": false,  "channel5": false,  "channel6": false,  "channel7": false,  "doMean": true,  "doStdDev": false,  "doMinMax": false,  "doHaralick": false,  "haralickMin": NaN,  "haralickMax": NaN,  "haralickDistance": 1,  "haralickBins": 32}');
//def entry = getProjectEntry()
//def name = entry.getImageName() + '.txt'
//def path = buildFilePath(PROJECT_BASE_DIR, 'tables')
//mkdirs(path)
//path = buildFilePath(path, name)
//saveAnnotationMeasurements(path)

getProjectEntry().saveImageData(getCurrentImageData())
