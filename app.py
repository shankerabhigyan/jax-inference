import torch
import transformers
from transformers import AutoTokenizer, GPTJForCausalLM
from flask import Flask, request, jsonify

num_gpus = torch.cuda.device_count()
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

model_path = config.json["model_path"]
tokenizer = config.json["tokenizer"]

model = GPTJForCausalLM.from_pretrained(model_path).to(device)