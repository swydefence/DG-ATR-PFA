import os

def write_image_list(root_dir, output_file):
    with open(output_file, 'w') as f:
        label_mapping = {}
        label_counter = 0

        for dirpath, dirnames, filenames in os.walk(root_dir):
            for filename in filenames:
                if filename.endswith('.jpeg') or filename.endswith('.png'):
                    image_path = os.path.join(dirpath, filename)
                    label = os.path.basename(dirpath)

                    if label not in label_mapping:
                        label_mapping[label] = label_counter
                        label_counter += 1

                    f.write(f"{image_path} {label_mapping[label]}\n")

    print("Image list generated successfully!")

# Usage example
root_directory = 'data\S2M\/sample_qpm'
output_txt = 'data\S2M\image_list\/sample_qpm.txt'

write_image_list(root_directory, output_txt)