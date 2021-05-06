# Gensim_utility
***
A project to get measures of similarity between two timeseries datasets using 8 similarity measures.
---
Prerequisites:
* Conda/Pip 
* Any latest Web Browser
---

Steps to run the project:
* Clone the project.

* If using Conda:
  1. Open Conda Command Prompt.
  2. cd into Gensim_utility\
  3. Create the project env and install dependencies with ``` conda env create -f projectgs.yml ```
  4. Activate the env with ```activate projectgs```
  5. cd into myproject\
  6. Run the project with ``` python3 manage.py runserver ```
  7. Open your preferred web browser
  8. Go to http://127.0.0.1:8000
  9. Explore and use Gensim Utility
  
* If using Pip:
  1. Open cmd.
  2. cd into Gensim_utility\
  3. Create a env called 'projectgs' with ``` python3 -m venv projectgs ```
  4. Activate the env with ``` source projectgs/bin/activate ```
  5. Install the dependencies with ``` pip install -r requirements.txt ```
  6. cd into myproject\
  7. Run the project with ``` python3 manage.py runserver ```
  8. Open your preferred web browser
  9. Go to http://127.0.0.1:8000
  10. Explore and use Gensim Utility

***

# How to use the project:
  1. Open the sidebar by clicking on Menu button.
  2. Click on Similarity Generation option.
  3. Choose a dataset each from the preloaded datasets from each dropdown menu on the screen.
  4. Click Submit button under both menus to confirm your selection.
  5. You can also import time series datasets by clicking on the Import dataset radio button and pasting the URLs in the text boxes that appear.
  6. Click Submit button to confirm your URLs.
  7. Click on the generate button and wait for the results to be generated. It may take a while depending on the datasets chosen.
  8. A new page Visualisation appears. Explore the steps taken and the graphs generated for both datasets during the process.
  9. At the bottom of the screen it shows the 8 similarity measures calculated for the chosen datasets. 
  10. Click on the Download report button and wait for a few seconds to get the onscreen results in a pdf format.
  
***
Visit a demo on https://demo-gensimutility.herokuapp.com/
