# %%
from wand.image import Image as Wand

# %%
def resize_gif(path, save_as, width=155, height=155):
    try:
        with open(path, 'rb') as gif:
            bytes = gif.read()
            with Wand(blob=bytes, format='GIF') as img:
                print(img.format, img.compression_quality, img.compression, img.width, img.height, img.type, img.animation, img.colors)
                img.compression_quality = 0
                img.compression = 'lzw'
                img.resize(width, height)
                img.format = 'GIF'
                img.save(filename=save_as)
    except Exception as ex:
        print(ex)

# %%
resize_gif(r'image/fish.gif', r'image/fishresize.gif',600,467)

# %%
resize_gif(r'image/happy.gif', r'image/happy.gif',500,500)
resize_gif(r'image/happytwo.gif', r'image/happytwo.gif',520,520)

# %%
resize_gif(r'image/sad.gif', r'image/sad.gif',500,500)
resize_gif(r'image/sadtwo.gif', r'image/sadtwo.gif',520,520)

# %%
resize_gif(r'image/notbad.gif', r'image/notbad.gif',500,500)
resize_gif(r'image/notbadtwo.gif', r'image/notbadtwo.gif',520,520)

# %%
resize_gif(r'image/touchfish.gif', r'image/touchfish.gif',520,520)
resize_gif(r'image/wa.gif', r'image/wa.gif',520,520)
resize_gif(r'image/catmouse.gif', r'image/catmouse.gif',500,500)
resize_gif(r'image/cutedog.gif', r'image/cutedog.gif',520,520)
# %%
