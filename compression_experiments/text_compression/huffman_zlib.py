import zlib
import time

text = "Data compression is essential for reducing storage costs and improving transmission speed in modern systems. The need for efficient compression techniques is growing exponentially."

def compress_text(text):
    return zlib.compress(text.encode())

def decompress_text(compressed):
    return zlib.decompress(compressed).decode()

start = time.time()
compressed = compress_text(text)
compression_time = time.time() - start

start = time.time()
decompressed = decompress_text(compressed)
decompression_time = time.time() - start

original_size = len(text.encode())
compressed_size = len(compressed)
compression_ratio = compressed_size / original_size

print("Original size:", original_size, "bytes")
print("Compressed size:", compressed_size, "bytes")
print("Compression ratio:", compression_ratio)
print("Compression time:", compression_time, "s")
print("Decompression time:", decompression_time, "s")
