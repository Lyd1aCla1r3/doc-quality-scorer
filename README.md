# Document Quality Scorer

A comprehensive, deterministic engine designed to evaluate the structural integrity and readability of markdown documentation. Built from the ground up to provide actionable, multi-signal quality scoring.

## Overview

The Document Quality Scorer acts as an automated editorial assistant. Rather than relying on simple word counts or arbitrary checks, it employs a multi-stage pipeline to analyze documentation on several fronts:

- **Structural Parsing**: The engine natively understands markdown, extracting the core architectural elements of a document (headings, lists, code blocks, and paragraphs).
- **Readability Metrics**: Utilizing established Natural Language Processing (NLP) techniques, the scorer calculates sophisticated reading-ease formulas (such as Flesch-Kincaid) to ensure your documentation remains accessible to its intended audience.
- **Semantic Fidelity**: By applying advanced machine learning vectorization (TF-IDF) and cosine similarity comparisons, the scorer evaluates the semantic consistency across different sections of your document, flagging areas that may lack cohesive terminology or focus.

These signals are then synthesized into a comprehensive composite score, giving technical writers and engineers immediate feedback on the health of their documentation.

## Features

- **Multi-Stage Analysis**: Combines structural, readability, and semantic metrics into a single unified score.
- **Empirical NLP**: Leverages the `nltk` library to handle complex grammatical parsing and syllable tokenization.
- **Consistency Checking**: Uses `scikit-learn` to measure internal variance and semantic drift.
- **Structured Reporting**: Generates immediate, easy-to-read markdown reports or structured JSON for automated pipeline integration.
- **Zero Proprietary Overlap**: A clean-room implementation strictly adhering to general text processing principles.

## Installation

Ensure you have Python installed, then build and install the engine locally:

```bash
pip install .
```

This will automatically register the `doc-quality-scorer` command-line interface.

## Usage

Run the scorer against any markdown file to receive an immediate quality report:

```bash
doc-quality-scorer path/to/your/document.md --format markdown
```

For automated pipelines or CI/CD integration, use the default JSON format:

```bash
doc-quality-scorer path/to/your/document.md
```

## Development & Testing

To run the comprehensive unit testing suite, install the development dependencies:

```bash
pip install .[dev]
pytest tests/
```
