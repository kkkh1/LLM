import torch
device=torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"\n!!! current device is {device} !!!\n")
import llama_cpp
import ctypes
llm = llama_cpp.Llama(model_path="llama-2-7b-chat.ggmlv3.q4_0.gguf",n_gpu_layers=40,
n_batch=512, 
n_ctx=2048,)
output = llm("Q:What is universe A: ", max_tokens=32, stop=["Q:", "\n"], echo=True)

print(output["choices"][0]["text"])