// Assuming you have already loaded the PSD.js library and have access to the parsed PSD object
// psd is the parsed PSD object
var PSD = require('psd');
var psd = PSD.fromFile("Untitled_Artwork-0-0.psd");
psd.parse();

// Traverse through the layers to find layers with active pixels
var layersWithPixels = [];
psd.tree()
  if (layer.visible && layer.isPixelLayer) {
    layersWithPixels.push(layer);
  }
});





console.log(psd.tree().export());
//console.log(layer.children)
console.log(layersWithPixels)
// Now you have an array, layersWithPixels, which contains all layers with active pixels
// You can access the properties and perform actions on these layers as needed
layersWithPixels.forEach((layer) => {
  console.log('Layer Name:', layer.name);
  // ... perform other actions
});
