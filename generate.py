#!/usr/bin/env python

import json
from string import Template
import logging

logging.basicConfig(level=logging.INFO)

TEMPLATE_FILE = "templates/image.md"
DEST_DIR = "./content/gallery"

def generate_image_page(gallery, width, height, title, text, src):
    # We need to shell-substitute the template file into {DEST_DIR}/{src}.md with the given parameters
    with open(TEMPLATE_FILE, 'r') as tf:
        template = Template(tf.read())
        # escape any apostrophes in the text and title
        # text = text.replace("'", "\\'")
        result = template.substitute(gallery=gallery, width=width, height=height, title=title, text=text, src=src)
        with open(f"{DEST_DIR}/{src}.md", 'w') as df:
            df.write(result)

def generate(gallery):
    images = None
    with open(f"data/{gallery}.json", 'r') as df:
        images = json.load(df)

    for image in images:
        logging.info(f'Gallery: {gallery} Image: {image["title"]}')
        generate_image_page(gallery, width=image["width"], height=image["height"], title=image["title"], text=image["text"], src=image["src"])

def main():
    generate("my")
    generate("other")

if __name__ == "__main__":
    main()