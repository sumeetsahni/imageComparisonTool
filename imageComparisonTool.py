#!/usr/bin/python

import csv
import time
import argparse
import logging

logging.basicConfig(level=logging.getLevelName('INFO'))
logger = logging.getLogger(__name__)
from lib.helper.image_operations import ImageOperations

def read_from_input_csv(input_csv_path):
    logger.info("Path of Input CSV is  {}". format(input_csv_path))
    image_comparison = ImageOperations()
    with open(input_csv_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        output_csv_list = [['image1', 'image2', 'similar', 'elapsed']]
        for row in csv_reader:
            if row[0] != 'image1':
              start_time = time.time()
              imagediff = image_comparison.compareimages(row[0], row[1])
              elapsed_time = (time.time() - start_time)
              if imagediff == 0.0:
                  row.append(0)
                  row.append(elapsed_time)
                  output_csv_list.append(row)
              else:
                  row.append(imagediff)
                  row.append(elapsed_time)
                  output_csv_list.append(row)
    return  output_csv_list

def create_output_csv(output_csv_list, output_csv_path):
    with open(output_csv_path, 'w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in output_csv_list:
           csv_writer.writerow(row)
    logger.info("Output CSV has been created at path {}". format(output_csv_path))


if __name__ == '__main__':
    """
    Initializing function
    """

    parser = argparse.ArgumentParser(description = 'Run the Image Comparison tool')
    sub_parser = parser.add_subparsers()

    image_comparison = sub_parser.add_parser('imagecompare', help = "Compares the image from the input csv")
    image_comparison.set_defaults(function='imagecompare')
    image_comparison.add_argument('-i', '--input_csv', help = "Provide the input csv", default='test_data/input.csv')
    image_comparison.add_argument('-o', '--output_csv', help = "Provide the ouput csv path", default='test_data/output.csv')

    args = parser.parse_args()

    if args.function == 'imagecompare':
        comparison_output = read_from_input_csv(args.input_csv)
        create_output_csv(comparison_output, args.output_csv)
