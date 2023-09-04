## How To Create Your Own Chat GPT4 Using Python3 And Open AI's API

## Prerequisites
If You Dont Have Python3 Installed, [Install It Here](https://www.python.org/downloads/) 

If You Dont Have An Api Key From Opean Ai Get One [Here](https://openai.com/)

If You Have Not Completed The Open AI Quickstart Guide Do So [Here](https://platform.openai.com/docs/quickstart/build-your-application). This Will Aid You On This Tutorial.

### Step 1)

Download The Open Ai Library. To Do This Open A Window In Terminal And Type The Following 
```
pip3 install openai
``` 
If You Already Have The Open Ai Library Installed Make Sure You Are On The Most Recent Version. To Do This, In Terminal Type
```
pip3 install --upgrade openai
```
### Step 2)

Open The IDE Of Your Choice And Create Two Different Python Files. For Either File Do Not Name Them "Openai". In The First File You Will Create This Code
```
import openai
from gptkey import OPENAI_API_KEY
openai.api_key = OPENAI_API_KEY
output = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[{"role": "user",
    "content":
                "Write prompt here!"}]
)
print(output)
```
### Step 3)

According To Step 2 Your Second File Name Has To Be "gptkey". If You Want To Name Your Second File Something Different You May Just Make The According Edits To The Code. In This Second File We Will Store That Api Key That You Got From [Open AI](https://openai.com/). The Code Will Look Like This
```
OPENAI_API_KEY = "your api key"
# Inside of the qoutation marks you can paste your api key that should have been
# obtained from the Opean Ai website! :)
```
### Step 4)

The Next Step Will Be To Add Your Own Prompt On lIne 8 Where You See The Code Below. This Prompt Is What Chat GPT Will Be Respond To. 
```
"Write prompt here!"}]
```

### Step 5)

The Last Step Is To Simply Run The Code, Enjoy Having Your Own Chat GPT :)
