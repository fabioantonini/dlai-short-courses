# Generative AI with Large Language Models -- Week 1 Summary

## 1. Introduction to Generative AI

Generative AI refers to models capable of generating new content such as
text, code, images, and audio. Large Language Models (LLMs) are based on
deep neural networks trained on massive text corpora.

### Discriminative vs Generative Models

-   **Discriminative models** learn $P(y|x)$.
-   **Generative models** learn $P(x)$ or $P(x,y)$.

LLMs model the probability of token sequences:

$$
P(x_1, x_2, ..., x_n) = \prod_{t=1}^{n} P(x_t | x_{<t})
$$

## 2. Transformer Architecture

The Transformer is based on self-attention mechanisms.

### Self-Attention

Given queries $Q$, keys $K$, and values $V$:

$$
Attention(Q,K,V) = softmax\left(rac{QK^T}{\sqrt{d_k}}ight)V
$$

Key components: - Multi-head attention - Positional encoding - Layer
normalization - Feed-forward networks

## 3. Training LLMs

Training is typically divided into:

1.  Pretraining (self-supervised next-token prediction)
2.  Supervised Fine-Tuning (SFT)
3.  Reinforcement Learning from Human Feedback (RLHF)

Recent updates include: - Direct Preference Optimization (DPO) -
Constitutional AI - Scalable alignment techniques

## 4. Scaling Laws

Performance improves predictably with: - Model size - Dataset size -
Compute budget

Scaling laws often follow power-law behavior.

## 5. Foundation Models

Foundation models: - Trained on broad datasets - Adaptable to multiple
tasks - Fine-tunable or promptable

Recent trends (2024--2026): - Mixture of Experts (MoE) - Efficient
fine-tuning (LoRA, QLoRA) - Multimodal models (text + image + audio)
