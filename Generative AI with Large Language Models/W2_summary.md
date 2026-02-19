# Generative AI with Large Language Models -- Week 2 Summary

## 1. Fine-Tuning LLMs

After pretraining, models are adapted via fine-tuning.

Types: - Supervised Fine-Tuning (SFT) - Reinforcement Learning from
Human Feedback (RLHF)

## 2. Reinforcement Learning from Human Feedback

RLHF pipeline: 1. Supervised fine-tuning 2. Reward model training 3.
Policy optimization (e.g., PPO)

The objective becomes:

$$
\max_{\theta} \mathbb{E}_{x \sim D} [R(x)]
$$

## 3. Prompt Engineering

Prompt design significantly affects output quality. Key techniques: -
Few-shot prompting - Chain-of-thought prompting - Role prompting

## 4. Evaluation of LLMs

Evaluation methods include: - Perplexity - Human evaluation -
Task-specific benchmarks

Perplexity:

$$
PP = 2^{-\frac{1}{N} \sum \log_2 P(w_i)}
$$

## 5. Figures and Diagrams (Analysis)

Figures show: - RLHF training pipeline - Comparison between supervised
learning and RL optimization - Prompt-response flow structure These
visuals clarify the alignment process and human-in-the-loop training.

------------------------------------------------------------------------
