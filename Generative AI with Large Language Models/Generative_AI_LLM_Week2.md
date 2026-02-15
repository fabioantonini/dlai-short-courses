# Generative AI with Large Language Models -- Week 2 Summary

## 1. Fine-Tuning Strategies

### Full Fine-Tuning

All parameters updated --- expensive but powerful.

### Parameter-Efficient Fine-Tuning (PEFT)

-   LoRA
-   QLoRA
-   Adapters
-   Prefix tuning

Low-rank update:

$$
W' = W + BA
$$

where $B$ and $A$ are low-rank matrices.

## 2. Prompt Engineering

Prompt design impacts performance:

-   Zero-shot
-   Few-shot
-   Chain-of-thought prompting
-   Role-based prompting

### Chain of Thought

Encourages intermediate reasoning steps:

$$
Answer = f(Reasoning Steps(x))
$$

## 3. Evaluation Metrics

-   Perplexity
-   BLEU / ROUGE
-   Human evaluation
-   Task-specific benchmarks

Modern evaluation: - MMLU - HELM - MT-Bench - Arena-based evaluation

## 4. Safety and Alignment

Risks: - Hallucination - Bias - Toxicity - Prompt injection

Mitigation: - RLHF - Red-teaming - Guardrails - Moderation layers

## 5. Deployment Considerations

-   Latency vs throughput trade-offs
-   Quantization (INT8, INT4)
-   GPU memory constraints
-   On-device inference vs cloud APIs
