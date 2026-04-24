# GPT-Summarizer

A utility for summarizing long meeting transcripts that exceed the OpenAI API context limit. Splits input text into 2048-character chunks, feeds them to GPT sequentially with a continuation prompt, then triggers summarization on a keyword.

## Files

- `main.py` — Text splitter and GPT summarization logic
- `test openai.py` — API connection tests
- `Summary.txt`, `Summary1.txt` — Example outputs
