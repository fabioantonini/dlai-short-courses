# Generative AI with Large Language Models -- Week 3 Summary

## 1. Retrieval-Augmented Generation (RAG)

RAG enhances LLMs with external knowledge retrieval.

Pipeline:

1.  Embed query
2.  Retrieve relevant chunks
3.  Inject context into prompt
4.  Generate answer

Embedding similarity:

$$
sim(x,y) = rac{x \cdot y}{||x|| ||y||}
$$

Vector databases: - FAISS - ChromaDB - Pinecone - Milvus

## 2. Agents and Tool Use

Modern LLM systems integrate: - Tools - APIs - Function calling -
Multi-step planning

Agent loop: 1. Plan 2. Act 3. Observe 4. Reflect

## 3. Multimodal Models

Text + Image (e.g., GPT-4o, Gemini) Text + Audio Text + Code

Cross-attention integrates modalities.

## 4. Efficiency and Optimization

-   Quantization
-   Distillation
-   Sparse attention
-   KV-cache optimization

## 5. Future Directions (2025--2026)

-   Smaller high-performance models
-   Open-weight ecosystems
-   Edge inference (Jetson-class devices)
-   Long-context models (1M+ tokens)
-   Agentic AI workflows
