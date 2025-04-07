from PIL import Image
import os
import time

def compress_image_jpeg(input_path, output_path, quality=30):
    img = Image.open(input_path)
    img.save(output_path, "JPEG", quality=quality)

input_image = "your_image.png"  # Replace with your real PNG file
output_image = "compressed_image.jpg"

start = time.time()
compress_image_jpeg(input_image, output_image, quality=30)
compression_time = time.time() - start

start = time.time()
img = Image.open(output_image)
decompression_time = time.time() - start

original_size = os.path.getsize(input_image)
compressed_size = os.path.getsize(output_image)

print("Original size:", original_size, "bytes")
print("Compressed size:", compressed_size, "bytes")
print("Compression ratio:", compressed_size / original_size)
print("Compression time:", compression_time, "s")
print("Decompression time:", decompression_time, "s")
