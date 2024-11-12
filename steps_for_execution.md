## Prepare the playground

### Creating the environment

- On a shell prompt issue the following command to create a Python Virtual Environment.
  `conda create -n pravash python=3.12`
- Now, activate the newly created environment.
  `conda activate pravash`
- Verify that the newly created environment is active.
  `conda env list`

### Install the prerequisites

- Clone the Omniparser repo from github
  `git clone https://github.com/microsoft/OmniParser.git`
- Now, navigate inside the newly cloned repo and issue the following command
  `pip install -r requirements.txt`

### Build the model

- From the Reference section below download the `download.sh` file and store it inside the OmniParser root folder.
- execute the download.sh file (Make sure that your VE is activated)
- upon execution of the above download script all the required models are downloaded and a `best.pt` file is generated which will be required to run the scripts in the next steps.

## Play with the model

- There are 3 ways to play with the code. And here they are.

1. Using Gradio
   From within the OmniParser folder issue the following command.
   `python gradio_demo.py`

- The above command will fire the gradio server. Open a browser and type http://localhost:7861 to see the interface.
- In the UI interface you can enter your input image to extract structured data.
- Note: This process took about a minute for an amazon listing page.

2. Using Vanila Python
   - Open the app.py present inside the OmniParser folder and run with the following command.
   - `python app.py`
   - Ensure that the required Conda environment is set up otherwise you will see failures.
  
3. Using Jupyter Notebook
   - You need to run `demo.ipynb` notebook present inside OmniParser folder.
   - Caution/Note
     > Navigate to OmniParser folder, activate the conda environment and run the Jupyter notebook present in the required conda env.
     > For example, `conda activate pravash` and then list all available jupyter notebooks
   > `conda env list`
     - `/home/akasmajhi/.local/bin/jupyter`
     - `/home/akasmajhi/anaconda3/envs/pravash/bin/jupyter`
   - As you can see there are 2 Jupyter notebook instances in different locations.
   - Run the notebook present in the required conda environment.
    `/home/akasmajhi/anaconda3/envs/pravash/bin/jupyter notebook`


## References

- OmniParser official site
  -- https://github.com/microsoft/OmniParser
- Hugging Face (for models)
  -- https://huggingface.co/microsoft/OmniParser
- Video Reference
  -- https://youtu.be/a19DDOlukgc
- Download script for building the model
  -- https://mer.vin/2024/10/omni-parser/
