# app.py is a chatbot integrated with ChatGPT API
## LLM model: text-ada-001
Login to your OpenAI id and generate a key. Using the Open AI key is crucial for API calls.
As we construct a chatbot, set the input parameters: input size, text tokenization, chunk size.
Then, it becomes crucial to specify the OpenAI LLM model to be used in your code and properly specify the path to load learning data.
Create vector indexing so as to establish communication between the LLM predictor and the learning data (here I have used a .pdf file).
## GUI interface: gradio
Gradio provides interfacing between your newly constructed OpenAI powered chatbot and the human user, so as to form a channel for communication.

Feed documents of your choice and enjoy hassle free text reference!
