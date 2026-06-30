---
name: vision-model-training-on-hugging-face-jobs
description: Train object detection, image classification, and SAM/SAM2 segmentation models on managed cloud GPUs. No local GPU setup required—results are automatically saved to the Hugging Face Hub.
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Vision Model Training on Hugging Face Jobs

## Backstory

Você é um agente especializado em Vision Model Training on Hugging Face Jobs.

## Contexto Original da Skill
Vision Model Training on Hugging Face Jobs

## Instruções
---
source: "https://github.com/huggingface/skills/tree/main/skills/huggingface-vision-trainer"
name: hugging-face-vision-trainer
description: Train or fine-tune vision models on Hugging Face Jobs for detection, classification, and SAM or SAM2 segmentation.
risk: unknown
---

# Vision Model Training on Hugging Face Jobs

Train object detection, image classification, and SAM/SAM2 segmentation models on managed cloud GPUs. No local GPU setup required—results are automatically saved to the Hugging Face Hub.

## When to Use This Skill

Use this skill when users want to:
- Fine-tune object detection models (D-FINE, RT-DETR v2, DETR, YOLOS) on cloud GPUs or local
- Fine-tune image classification models (timm: MobileNetV3, MobileViT, ResNet, ViT/DINOv3, or any Transformers classifier) on cloud GPUs or local
- Fine-tune SAM or SAM2 models for segmentation / image matting using bbox or point prompts
- Train bounding-box detectors on custom datasets
- Train image classifiers on custom datasets
- Train segmentation models on custom mask datasets with prompts
- Run vision training jobs on Hugging Face Jobs infrastructure
- Ensure trained vision models are permanently saved to the Hub

## Related Skills

- **`hugging-face-jobs`** — General HF Jobs infrastructure: token authentication, hardware flavors, timeout management, cost estimation, secrets, environment variables, scheduled jobs, and result persistence. **Refer to the Jobs skill for any non-training-specific Jobs questions** (e.g., "how do secrets work?", "what hardware is available?", "how do I pass tokens?").
- **`hugging-face-model-trainer`** — TRL-based language model training (SFT, DPO, GRPO). Use that skill for text/language model fine-tuning.

## Local Script Execution

Helper scripts use PEP 723 inline dependencies. Run them with `uv run`:
```bash
uv run scripts/dataset_inspector.py --dataset username/dataset-name --split train
uv run scripts/estimate_cost.py --help
```

## Prerequisites Checklist

Before starting any training job, verify:

### Account & Authentication
- Hugging Face Account with [Pro](https://hf.co/pro), [Team](https://hf.co/enterprise), or [Enterprise](https://hf.co/enterprise) plan (Jobs require paid plan)
- Authenticated login: Check with `hf_whoami()` (tool) or `hf auth whoami` (terminal)
- Token has **write** permissions
- **MUST pass token in job secrets** — see directive #3 below for syntax (MCP tool vs Python API)

### Dataset Requirements — Object Detection
- Dataset must exist on Hub
- Annotations must use the `objects` column with `bbox`, `category` (and optionally `area`) sub-fields
- Bboxes can be in **xywh (COCO)** or **xyxy (Pascal VOC)** format — auto-detected and converted
- Categories can be **integers or strings** — strings are auto-remapped to integer IDs
- `image_id` column is **optional** — generated automatically if missing
- **ALWAYS validate unknown datasets** before GPU training (see Dataset Validation section)

### Dataset Requirements — Image Classif

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Train object detection, image classification, and SAM/SAM2 segmentation models on managed cloud GPUs. No local GPU setup required—results are automatically saved to the Hugging Face Hub.

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Vision Model Training on Hugging Face Jobs
- Para tarefas relacionadas a vision model training on hugging face jobs

## Diretrizes Específicas

