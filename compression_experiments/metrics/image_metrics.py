from skimage.metrics import structural_similarity as ssim
import cv2

input_image = "your_image.png"  
output_image = "compressed_image.jpg"

original = cv2.imread(input_image)
compressed = cv2.imread(output_image)

original_gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
compressed_gray = cv2.cvtColor(compressed, cv2.COLOR_BGR2GRAY)

psnr_value = cv2.PSNR(original, compressed)
ssim_value, _ = ssim(original_gray, compressed_gray, full=True)

print("PSNR:", psnr_value)
print("SSIM:", ssim_value)
