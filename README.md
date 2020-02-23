# Image Comparison Tool. 

### Directory structure for this project

    ├── lib                         # common libraries for different helper functions
        ├── helper 
           |── image_operations.py  # Image operations related library     
    ├── README.md                   # Project information guide
    ├── requirements.txt            # Python library config file
    └── ImageComparisonTool.py      # Main workflow file 
    ├── test_data                   # Contains the sample images, input and output csv generated with this tool



### Steps to run the ImageComparisonTool and how to fetch the latest code

1. Clone this git repo at a specified path on your filesystem
2. Change the directory to the path where code is cloned.
3. Install the dependencies  \
   `$ pip install -r requirements.txt`
4. Run the tool \
   `$ python imageComparisonTool.py  imagecompare -i input_csv_path -o output_csv_path`  
 
5. If the project is already cloned, run the below command to get the latest code and then run Step 4 \
   `$ git pull`   
  

****NOTE****: With  the sample test_data provided with this project, this tool can simply be run with command \
   `$ python imageComparisonTool.py  imagecompare`  
   This would generate the output csv file at path testdata/output.csv
        


### Design Specifications

1. A modular approach to use object oriented programming so that the project can be extended later to incorporate new use cases
2. The directory structure of the project uses a lib folder where more helper methods can be created in the future
3. Tool uses argparser with default values set, the parser is quite handy and intuitive for the user of the tool
4. Since this would be run on different systems, where all the python packages requirements are not met, so a requirements.txt file is provided with instructions to create the images.
5. To compare images, python community provides a library names Pillow to compare images and get the difference, it has been used to get the diff.

#### Important Considerations

1. **Proof that the Code Works** \
   A snapshot that the ImageComparisonTool works by running locally is provided at path testdata with name Snaphot_Successfull_Project_Execution_Locally.png
2. Project is well documented so that: \
  a. Bjorn as a user can read the instructions and run it. \
  b. Ferris the new maintainer doesn't have issues with maintaining as directory structure and design is well documented. 

3. ****How to get the latest version of the code**** \
 a. Steps have been provided in the readme to clone the repo to get the latest code. \
 b. Assumption is that user is using git so steps have been added to always run git pull, before executing the tool from this project.

4. For more enhanced experience, Jenkins can be further used  so that user just provides the CSV and image path and doesn't look at the code, but that is not the scope of this project and hence, not included.

