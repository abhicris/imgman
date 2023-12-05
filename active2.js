// Assuming you have already loaded the PSD.js library and have access to the parsed PSD object
// psd is the parsed PSD object

// Function to recursively iterate through layers and find layers with active pixels

var PSD = require('psd');
var psd = PSD.fromFile("Untitled_Artwork-0-0.psd");
psd.parse();
// Assuming you have already loaded the PSD.js library and have access to the parsed PSD object
// psd is the parsed PSD object


#target photoshop

var doc = app.activeDocument;
var certainLayer = doc.artLayers[0];

var isLayerEmpty = isLayerEmptyCheck(certainLayer);

alert(isLayerEmpty);

function isLayerEmptyCheck(layer) {

    var isLayerEmpty = new Boolean;

    var LayerBounds = layer.bounds;
    if (LayerBounds[0] === "0 px" && LayerBounds[1] === "0 px" && LayerBounds[2] === "0 px" && LayerBounds[3] === "0 px") {
        return isLayerEmpty = true;
    } else {
        return isLayerEmpty = false;
    }

}