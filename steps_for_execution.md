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
   - 
4. Using Jupyter Notebook

## References

- OmniParser official site
  -- https://github.com/microsoft/OmniParser
- Hugging Face (for models)
  -- https://huggingface.co/microsoft/OmniParser
- Video Reference
  -- https://youtu.be/a19DDOlukgc
- Download script for building the model
  -- https://mer.vin/2024/10/omni-parser/
