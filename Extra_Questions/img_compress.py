import os
import shutil

def compress_images(directory_path, output_path, archive_format='zip'):
    """
    Compresses images in a directory into a compressed archive.

    Args:
        directory_path (str): Path to the directory containing images.
        output_path (str): Path to the output compressed archive.
        archive_format (str): Format of the compressed archive (default is 'zip').
    """
    try:
        # Create a temporary directory to store compressed images
        temp_directory = 'temp_images'
        os.makedirs(temp_directory, exist_ok=True)

        # Copy images to the temporary directory
        for filename in os.listdir(directory_path):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                src_file = os.path.join(directory_path, filename)
                dest_file = os.path.join(temp_directory, filename)
                shutil.copy(src_file, dest_file)

        # Create the compressed archive
        shutil.make_archive(output_path, archive_format, temp_directory)

        print(f"Compression successful. Archive created at: {output_path}.{archive_format}")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Clean up the temporary directory
        shutil.rmtree(temp_directory, ignore_errors=True)

if __name__ == "__main__":
    # Specify the path to the directory containing images
    image_directory = '/path/to/your/image/directory'

    # Specify the output path and format for the compressed archive
    output_archive_path = '/path/to/your/output/folder/compressed_images'
    archive_format = 'zip'

    # Call the compress_images function
    compress_images(image_directory, output_archive_path, archive_format)
