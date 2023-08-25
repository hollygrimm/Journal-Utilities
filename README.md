# Journal-Utilities
Utilities and Documentation for creating contents for the Active Inference Journal
https://github.com/ActiveInferenceInstitute/ActiveInferenceJournal

(A) The Python scripts

(1) invoke OpenAI Whisper Cloud service, and reformat the output to CSV.
Invocation from local Linux command line. (The suffixed "&" makes each python invocation run in background. Each instance of the process polls OpenAI every two minutes, and kicks off the four steps of the Extract-and-save phase of processing when main processing of its request has completed or failed.)  
```
python3 "/mnt/d/Documents/FEP-AI/Active Inference Podcast/SubmitToCloudWhisper.py" "ls039-0" "http://crisiscenter.us/AILab01/2022Livestreams" "ActInf Livestream 039.0 ~ 'Morphogenesis as Bayesian inference'.m4a" | tee mass_ls039-0.m4a.json &
python3 "/mnt/d/Documents/FEP-AI/Active Inference Podcast/SubmitToCloudWhisper.py" "ls039-1" "http://crisiscenter.us/AILab01/2022Livestreams" "ActInf Livestream 039.1 ~ 'Morphogenesis as Bayesian inference'.m4a" | tee mass_ls039-1.m4a.json &
python3 "/mnt/d/Documents/FEP-AI/Active Inference Podcast/SubmitToCloudWhisper.py" "ls039-2" "http://crisiscenter.us/AILab01/2022Livestreams" "ActInf Livestream 039.2 ~ 'Morphogenesis as Bayesian inference'.m4a" | tee mass_ls039-2.m4a.json &
```
(2) extracts speech and context data from the new local CSVs, and create a simple text file that can be manually imported into a word processor and formatted with Title, Heading 1 (session), Heading 2 (speakers, contents, transcript).


(B) The CSV should be filled out manually using any spreadsheet program.

These data are read by sentencesToTranscripts script, so the latter can convert Whisper-generated speaker labels "A" "B"... into "Daniel" "Bleu"...
Even if AllSpeakers.csv is correct, the raw, editable .txt file may still have to have Speaker adjusted - this happens when Whisper gets confused about accents or prosody.


--------

Initial Scripts 1 & 2, and initial README contributed by Dave Douglass, November 2022. 



## Create Virtual Environment
1. Create a new venv environment
```
python3 -m venv journal-utilities
```

2. Activate the environment in macOS or Linux:
```
source journal-utilities/bin/activate
```
OR for Windows
```
journal-utilities\Scripts\activate
```

3. Install packages
```
pip install -r requirements.txt
```

4. Set your intepreter path
```
which python
```
OR for Windows
```
where python
```

## Setup environment variables
copy `.env.sample` to `.env`

### Add Github token
Navigate to https://github.com/settings/tokens and click `Generate new token (classic)` For scope, select `repo` (to allow all of the repo items) and click `Generate Token`
add the token to the .env file as GITHUB_TOKEN

## Run format
```
black .
```

## Run Pylint
```
pylint src/time_utils.py
```


