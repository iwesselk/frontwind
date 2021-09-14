import _genstupid
import requests

font_families = ["font-sans", "font-serif", "font-mono"]

font_sizes = ["text-xs", "text-sm", "text-base", "text-lg", "text-xl", "text-2xl", "text-3xl", "text-4xl", "text-5xl", "text-6xl", "text-7xl", "text-8xl", "text-9xl"]
fontsize = _genstupid.gen_from_list("FontSize", font_sizes)
#print(_genstupid.gen_from_list("FontSize", ["text-xs", "text-sm"]))

font_smoothing = ["antialiased", "subpixel_antialiased"]
fontsmoothing = _genstupid.gen_from_list("FontSmoothing", font_smoothing)



print(fontsize)
print(fontsmoothing)