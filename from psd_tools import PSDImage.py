from psd_tools import PSDImage

psd = PSDImage.open('example.psd')
image = psd.compose()

for layer in psd:
    layer_image = layer.compose()


has_pixels()