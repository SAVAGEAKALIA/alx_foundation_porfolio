#!/usr/bin/env python
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch


model = None
tokenizer = None

def load_model():
    """Load the GPT-2 model and tokenizer"""
    global model, tokenizer
    if model is None or tokenizer is None:
        try:
            model = GPT2LMHeadModel.from_pretrained("distilgpt2")
            tokenizer = GPT2Tokenizer.from_pretrained("distilgpt2")
        except Exception as e:
            print(f"Error loading model: {e}")
            return None, None
    return model, tokenizer


def generate_blog_post(prompt, model, tokenizer, max_length=500, temperature=0.7):
    try:
        input_ids = tokenizer.encode(prompt, return_tensors="pt")
        attention_mask = torch.ones(input_ids.shape, dtype=torch.long, device=input_ids.device)
        pad_token_id = tokenizer.eos_token_id

        output = model.generate(
            input_ids,
            max_length=max_length,
            num_return_sequences=1,
            no_repeat_ngram_size=2,
            do_sample=True,
            temperature=temperature,
            attention_mask=attention_mask,
            pad_token_id=pad_token_id
        )

        generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
        return generated_text
    except Exception as e:
        print(f"Error generating text: {e}")
        return "Sorry, there was an error generating the blog post."


