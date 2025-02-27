## Purpose of the Script
The point of this script is that it can calculate the Earth's population density while allowing users to interact with it for a more appealing approach to geographics than simply looking at words and numbers. Using a logarithmic scale, this script can visualize data and make it into a 3D model so that one could rotate or zoom in to a specific country and figure out its population density if desired.

## Steps to Success
#### 1. Create a New Project in PyCharm
* Choose "Custom environment" and "Virtualenv" as the interpreter types to make a virtual environment
#### 2. Manually Install Required Packages
* In the terminal, put "pip install geopandas pandas plotly requests numpy"
#### 3. Add Script File
* Name the file "globe.py"
* Copy and paste the script's text from Blackboard into the file
#### 4. Generate a Full Requirements File
* In the terminal, put "pip freeze > all_requirements.txt", "pip install pipdeptree", "pipdeptree > dependency_tree.txt", and "pipdeptree --freeze > requirements.txt"
#### 5. Remove all Installed Packages
* In the terminal, put "pip uninstall -y -r all_requirements.txt" and "pip list"
#### 6. Verify Import Error
* Run "globe.py" to ensure it results in an import error
#### 7. Reinstall from "requirements.txt"
* In the terminal, put "pip install -r requirements.txt"
#### 8. Verify Working Script
* Run "globe.py" to ensure the interactive globe appears
#### 9. Generate and Save The Dependency Tree
* In the terminal, put "pipdeptree > dependency_tree.txt"

---
## Output of pipdeptree
geopandas==1.0.1
  - numpy [required: >=1.22, installed: 2.2.3]
  - packaging [required: Any, installed: 24.2]
  - pandas [required: >=1.4.0, installed: 2.2.3]
    - numpy [required: >=1.26.0, installed: 2.2.3]
    - python-dateutil [required: >=2.8.2, installed: 2.9.0.post0]
      - six [required: >=1.5, installed: 1.17.0]
    - pytz [required: >=2020.1, installed: 2025.1]
    - tzdata [required: >=2022.7, installed: 2025.1]
  - pyogrio [required: >=0.7.2, installed: 0.10.0]
    - certifi [required: Any, installed: 2025.1.31]
    - numpy [required: Any, installed: 2.2.3]
    - packaging [required: Any, installed: 24.2]
  - pyproj [required: >=3.3.0, installed: 3.7.1]
    - certifi [required: Any, installed: 2025.1.31]
  - shapely [required: >=2.0.0, installed: 2.0.7]
    - numpy [required: >=1.14,<3, installed: 2.2.3]
pipdeptree==2.25.0
  - packaging [required: >=24.1, installed: 24.2]
  - pip [required: >=24.2, installed: 25.0.1]
pipreqs==0.4.13
  - docopt [required: Any, installed: 0.6.2]
  - yarg [required: Any, installed: 0.1.10]
    - requests [required: Any, installed: 2.32.3]
      - certifi [required: >=2017.4.17, installed: 2025.1.31]
      - charset-normalizer [required: >=2,<4, installed: 3.4.1]
      - idna [required: >=2.5,<4, installed: 3.10]
      - urllib3 [required: >=1.21.1,<3, installed: 2.3.0]
plotly==6.0.0
  - narwhals [required: >=1.15.1, installed: 1.27.1]
  - packaging [required: Any, installed: 24.2]

---
## Observations or Issues
Completing the "PIP PIP Hooray" assignment was easier said than done as I went through trial and error (literally) trying to get the script to work. Notably, it seemed as if the globe took a while to appear regardless of how the script was handled.

#### Command Prompt
I started off by using Command Prompt and I verified that I was in a virtual environment by seeing "(.venv)" before my path name. Everything was going smoothly until I input "pipreqs . --force", which gave me syntax warnings and Unicode decode errors. After asking AI why, it gave me an alternative command, "pip freeze > requirements.txt", to try and I was able to proceed; however, the farthest I got was testing the script and it only opened up my web browser with a URL similar to an IP address, but it never loaded.

#### PyCharm
I decided to try again by using PyCharm instead. The project was created successfully, but while generating a full requirements file I encountered the same issue with "pipreqs . --force" as before. I tried using pipdeptree instead and input, "pipdeptree --freeze > requirements.txt" with better luck. I proceeded with the instructions, then I finally saw the globe appear in my web browser and I was able to interact with it properly.
