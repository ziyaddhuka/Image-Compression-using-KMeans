## Image compression using KMeans

# If you are getting errors or not getting the output in PART 1 then try PART 2

## IMP: Please give the path till the dataset folder. The code takes the data from the train and test folder inside the path

> pip install -r requirements.txt

# -------------PART 1 c-------------
## Run third part of Image compression using k , input_file, output_folder as parameters
> python k_means.py 20 data/hw3_part2_data/Koala.jpg output_folder/
> python k_means.py 5 data/hw3_part2_data/Penguins.jpg output_folder/



# -------------PART 2-------------
# Steps to run the code... commands are tested in linux.. you can apply alternative commands for windows/MacOS
## Step 1 creating a virtual environment to run the code so that it does not conflicts with other instaled packages on the machine
> python3 -m venv my_env
## Step 2 if the above gives error then make sure your python version is 3.6 or above and install the venv package. If no error move to Step 3
	### for linux and MacOS
	> python3 -m pip install --user virtualenv
	### for windows
	> py -m pip install --user virtualenv

## Step 3 activate the environment
> source my_env/bin/activate
> pip install --upgrade pip

## Step 2 use requirements.txt file to install required packages
> pip install -r requirements.txt

After this you are good to use the python files and can run using the above commands specified

### once done with grading of the code you can deactivate the environment and delete it
> deactivate
> rm -r my_env
