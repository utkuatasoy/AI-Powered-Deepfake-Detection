import cv2
import os
import matplotlib.pyplot as plt
import pandas as pd

# Define directories for input and output
input_dir = r"C:\Users\Utku\Desktop\BIL462 PROJE\runs\detect\predict2\crops\FACE"
output_dir = r"C:\Users\Utku\Desktop\BIL462 PROJE\preprocessed_faces"
os.makedirs(output_dir, exist_ok=True)

# Preprocessing function
def preprocess_image(image_path, output_path):
    # Load image
    image = cv2.imread(image_path)
    # Resize to 299x299
    resized_image = cv2.resize(image, (299, 299))
    # Normalize (scale pixel values to 0-1)
    normalized_image = resized_image / 255.0
    # Convert back to 8-bit for saving
    preprocessed_image = (normalized_image * 255).astype("uint8")
    # Save the preprocessed image
    cv2.imwrite(output_path, preprocessed_image)
    return resized_image, preprocessed_image

# Calculate the overall original mean
original_means = []
for filename in os.listdir(input_dir):
    if filename.endswith((".png", ".jpg", ".jpeg")):
        input_path = os.path.join(input_dir, filename)
        image = cv2.imread(input_path)
        original_means.append(image.mean())
overall_original_mean = sum(original_means) / len(original_means) if original_means else 0

# Process all images and calculate preprocess means
image_differences = []
for filename in os.listdir(input_dir):
    if filename.endswith((".png", ".jpg", ".jpeg")):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)
        # Preprocess the image
        _, preprocessed = preprocess_image(input_path, output_path)
        preprocessed_mean = preprocessed.mean()
        difference = abs(overall_original_mean - preprocessed_mean)
        image_differences.append({
            "Image Name": filename,
            "Overall Original Mean": overall_original_mean,
            "Preprocessed Mean": preprocessed_mean,
            "Difference Mean": difference
        })

# Create a DataFrame for differences
df = pd.DataFrame(image_differences)


# Visualize one sample
if os.listdir(input_dir):
    sample_image = os.listdir(input_dir)[0]
    input_sample_path = os.path.join(input_dir, sample_image)
    output_sample_path = os.path.join(output_dir, sample_image)
    original_sample = cv2.imread(input_sample_path)
    preprocessed_sample = cv2.imread(output_sample_path)
    # Resize and ensure both images are in the same shape
    original_sample = cv2.resize(original_sample, (299, 299))
    preprocessed_sample = cv2.resize(preprocessed_sample, (299, 299))
    # Ensure same number of channels (convert to RGB)
    if len(original_sample.shape) != len(preprocessed_sample.shape):
        original_sample = cv2.cvtColor(original_sample, cv2.COLOR_BGR2RGB)
        preprocessed_sample = cv2.cvtColor(preprocessed_sample, cv2.COLOR_BGR2RGB)
    # Calculate the difference
    diff_sample = cv2.absdiff(original_sample, preprocessed_sample)
    # Enhance the difference visualization by adjusting contrast and brightness
    diff_sample_visual = cv2.convertScaleAbs(diff_sample, alpha=20, beta=50)  # alpha increases contrast, beta adjusts brightness

    # Plot the enhanced difference with other images
    plt.figure(figsize=(15, 5))
    plt.subplot(1, 3, 1)
    plt.imshow(cv2.cvtColor(original_sample, cv2.COLOR_BGR2RGB))
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(1, 3, 2)
    plt.imshow(cv2.cvtColor(preprocessed_sample, cv2.COLOR_BGR2RGB))
    plt.title("Preprocessed Image")
    plt.axis("off")

    plt.subplot(1, 3, 3)
    plt.imshow(cv2.cvtColor(diff_sample_visual, cv2.COLOR_BGR2RGB))
    plt.title("Enhanced Difference")
    plt.axis("off")

    plt.show()

# Plot the updated data
plt.figure(figsize=(10, 6))

# Plot Preprocessed Mean
plt.plot(df["Preprocessed Mean"], label="Preprocessed Mean", marker='s', linestyle='-', markersize=5)

# Plot Difference Mean
plt.plot(df["Difference Mean"], label="Difference Mean", marker='^', linestyle='-', markersize=5)

# Add labels and title
plt.axhline(y=overall_original_mean, color='r', linestyle='--', label="Overall Original Mean")
plt.xlabel("Image Index", fontsize=12)
plt.ylabel("Mean Pixel Value", fontsize=12)
plt.title("Preprocessed Mean and Difference Comparison", fontsize=14)
plt.legend()
plt.grid(True)

# Save the plot as an image
plot_image_path = r"C:\Users\Utku\Desktop\BIL462 PROJE\updated_pixel_value_means_plot.png"
plt.savefig(plot_image_path, bbox_inches='tight', dpi=300)

# Show the plot
plt.show()

print("Updated processing complete. Overall Original Mean calculated, and plot saved!")
