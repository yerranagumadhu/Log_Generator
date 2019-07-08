# Log_Generator
Fake_Log_Generaor
#Created by Madhusudhan Reddy Yerranagu
#Connect me on  Linkedin: https://www.linkedin.com/in/madhusudhan-reddy-yerranagu-034253ab/

#To create the Virtual Environment in python if you already installed the virtual environment 
virtualenv -p python2.7 venv

#Now to activate the Virtual Environment go into the bin folder or point into the bin folder and give the below command
source  activate
or
source current_folder/bin/activate

#once you activate the Virtual environment you need to install the requirements specified in the requirements.txt file
pip install -r requirements.txt


#And the run the apache-fake-log-gen_v3.py file to create the log files if you want to create the log files at 
# a specific location by passing the rguments -l followed by the path 
EX : python apache-fake-log-gen_v3.py -l /home/yerranagumadhu9623/Fake-Apache-Log-Generator/log
or
#If you want to create the log file at current location
EX: python apache-fake-log-gen_v3.py 
