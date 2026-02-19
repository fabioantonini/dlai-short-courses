# Generative AI with Large Language Models -- Week 1 Summary

## 1. Introduction to Generative AI

Generative AI refers to models capable of producing new content such as
text, images, audio, or code. Large Language Models (LLMs) are a central
technology in modern Generative AI systems.

## 2. What is a Large Language Model?

An LLM is a neural network trained on massive text corpora to predict
the next token in a sequence. The core training objective is next-token
prediction:

$$
P(w_t | w_{1}, w_{2}, ..., w_{t-1})
$$

This autoregressive modeling enables coherent long-form text generation.

## 3. Transformer Architecture

The Transformer is based on self-attention mechanisms. Key components: -
Token embeddings - Positional encoding - Multi-head self-attention -
Feed-forward layers - Residual connections and layer normalization

Self-attention computes:

$$
Attention(Q, K, V) = softmax\left(\frac{QK^T}{\sqrt{d_k}}\right)V
$$

## 4. Pretraining Phase

Models are pretrained on large-scale corpora using unsupervised
learning. This phase builds general language understanding.

## 5. Figures and Diagrams (Analysis)

The figures illustrate: - Transformer block structure - Flow of tokens
through encoder/decoder layers - The attention mechanism showing query,
key, and value interactions These diagrams emphasize parallelism and
long-range dependency modeling.

------------------------------------------------------------------------
