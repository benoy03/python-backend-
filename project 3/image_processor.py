import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from concurrent.futures import ThreadPoolExecutor

class ImageProcessor:
    def __init__(self, input_dir, output_dir):
        self.input_dir = input_dir
        self.output_dir = output_dir

        # Automatically create input and output directories if they don't exist
        if not os.path.exists(self.input_dir):
            os.makedirs(self.input_dir)
            print(f"Input directory '{self.input_dir}' did not exist. Created it! Please add images there and re-run the script.")
        
        os.makedirs(self.output_dir, exist_ok=True)
        self.supported_formats = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')

    def _get_images(self):
        """Return a list of image file paths in the input directory."""
        images = [os.path.join(self.input_dir, f)
                  for f in os.listdir(self.input_dir)
                  if f.lower().endswith(self.supported_formats)]
        if not images:
            print(f"No images found in '{self.input_dir}'. Please add images and try again.")
        return images

    def resize(self, image_path, width, height):
        with Image.open(image_path) as img:
            img = img.resize((width, height))
            self._save_image(img, image_path, "resized")
    
    def grayscale(self, image_path):
        with Image.open(image_path) as img:
            img = img.convert("L")
            self._save_image(img, image_path, "grayscale")

    def rotate(self, image_path, angle):
        with Image.open(image_path) as img:
            img = img.rotate(angle, expand=True)
            self._save_image(img, image_path, f"rotated_{angle}")

    def watermark(self, image_path, text="Sample Watermark", position=(10,10)):
        with Image.open(image_path) as img:
            drawable = ImageDraw.Draw(img)
            font_size = max(20, img.size[0] // 20)
            try:
                font = ImageFont.truetype("arial.ttf", font_size)
            except:
                font = ImageFont.load_default()
            drawable.text(position, text, font=font, fill=(255,255,255,128))
            self._save_image(img, image_path, "watermarked")

    def blur(self, image_path, radius=2):
        with Image.open(image_path) as img:
            img = img.filter(ImageFilter.GaussianBlur(radius))
            self._save_image(img, image_path, "blurred")

    def _save_image(self, img, original_path, suffix):
        base_name = os.path.basename(original_path)
        name, ext = os.path.splitext(base_name)
        save_path = os.path.join(self.output_dir, f"{name}_{suffix}{ext}")
        img.save(save_path)
        print(f"Saved: {save_path}")

    def process_all(self, operation, *args, use_threads=False):
        images = self._get_images()
        if not images:
            return  # Stop if no images to process
        if use_threads:
            with ThreadPoolExecutor() as executor:
                for img_path in images:
                    executor.submit(getattr(self, operation), img_path, *args)
        else:
            for img_path in images:
                getattr(self, operation)(img_path, *args)


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Batch Image Processing Utility")
    # Default folders and optional positional arguments
    parser.add_argument("input_dir", nargs='?', default="./input", help="Directory containing input images (default: ./input)")
    parser.add_argument("output_dir", nargs='?', default="./output", help="Directory to save processed images (default: ./output)")
    parser.add_argument("--resize", nargs=2, type=int, metavar=('WIDTH','HEIGHT'), help="Resize images")
    parser.add_argument("--grayscale", action='store_true', help="Convert images to grayscale")
    parser.add_argument("--rotate", type=float, help="Rotate images by angle")
    parser.add_argument("--watermark", type=str, help="Add watermark text")
    parser.add_argument("--blur", type=float, help="Apply Gaussian blur with radius")
    parser.add_argument("--threads", action="store_true", help="Enable multithreading for faster processing")
    
    args = parser.parse_args()
    processor = ImageProcessor(args.input_dir, args.output_dir)

    if args.resize:
        processor.process_all("resize", *args.resize, use_threads=args.threads)
    if args.grayscale:
        processor.process_all("grayscale", use_threads=args.threads)
    if args.rotate:
        processor.process_all("rotate", args.rotate, use_threads=args.threads)
    if args.watermark:
        processor.process_all("watermark", args.watermark, use_threads=args.threads)
    if args.blur:
        processor.process_all("blur", args.blur, use_threads=args.threads)

if __name__ == "__main__":
    main()
