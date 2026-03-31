# Victorian Poetry GPT

A character-level GPT decoder trained on Victorian poetry.

The model generates text one character at a time in the style of late 19th-century verse (Hilaire Belloc, Lewis Carroll, W.S. Gilbert, and others), trained on a corpus collected from Project Gutenberg.

## Files

- `preprocess.py`: cleans the raw corpus (removes Project Gutenberg headers, filters non-poetry lines)
- `poetry_GPT.ipynb`: model definition, training loop and hyperparameter experiments
- `test_final_model.ipynb`: text generation and stylometric analysis
- `cautionary_tales.txt` / `victorian_poetry.txt`: raw corpora
- `corpus.txt`: combined cleaned corpus used for training

## Model

A GPT decoder with Pre-LayerNorm, GELU activation, learned positional embeddings and AdamW with linear warmup. Supports both flash attention and an explicit causal mask. Best results were obtained with model dimension 512, trained for 40000 steps.

## Generation

Temperature controls output style: lower values produce more repetitive but coherent text, higher values produce more creative and chaotic output.

### Example output (temperature = 0.8)
```
So now, like the singing year ago,
        The pumpkin's sins they slips on their terror,
      So expansively selected in the hill;
        She answered him if she found him, it bound them loud
        mounting the wild, haunted things at last,
            As if he had been quite prevailed.
```
