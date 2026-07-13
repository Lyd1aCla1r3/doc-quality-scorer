# Document Quality Scorer Demonstrations

This folder contains example files designed to showcase the advanced multi-signal analysis capabilities of the Document Quality Scorer.

## The Challenge

Standard documentation linters typically only evaluate structural elements (like ensuring headings are present) or perform simple word counts. They fail to catch poorly written, confusing documentation that uses overly complex language or inconsistent terminology across different sections.

## Our Solution

This tool moves beyond simple linting by employing:
1. **Structural Parsing:** Ensuring the markdown is valid.
2. **Readability Metrics:** Using Flesch-Kincaid to penalize passive, overly complex sentence structures.
3. **Semantic Fidelity:** Using TF-IDF vectorization to identify "semantic drift" where terminology changes unexpectedly (e.g., swapping between "server", "instance", and "node").

## Step-by-Step Reproduction

1. **Ensure the tool is installed.** If you haven't already, install the scorer from the root directory:
   ```bash
   cd ..
   pip install .
   cd examples
   ```

2. **Examine the test files.** 
   - `cohesive_guide.md`: Uses short, active sentences and consistently uses the term "compute node".
   - `subtle_degradation_guide.md`: Appears structurally identical to the naked eye. However, it uses passive, convoluted language and drifts terminology between "Virtual Machine", "instance", "server", and "node".

3. **Run the demonstration script.** Execute the provided shell script to run the scorer against both documents and compare the results:
   ```bash
   ./run_demo.sh
   ```

4. **Observe the output.** The terminal will clearly show that while both documents might pass a basic linter, the `subtle_degradation_guide.md` receives a heavily penalized score due to its poor readability and lack of semantic consistency.

## Expected Output

When you run the demonstration script, you should see the following comparative output in your terminal:

```
======================================================
 Running Document Quality Scorer - Subtlety Demo      
======================================================

Evaluating: cohesive_guide.md
(Expected: High readability, high semantic consistency)
------------------------------------------------------
# Quality Report: cohesive_guide.md

## Overall Score: 48.14/100

### Structure
- Headings: 4
- Paragraphs: 3
- Code Blocks: 0

**Analysis**: Document is properly partitioned with structural elements.

### Readability
- Flesch-Kincaid Reading Ease: 61.64
- Word Count: 116

**Analysis**: Readability is within the optimal range (60-80) for technical documentation.

### Fidelity & Consistency
- Semantic Consistency: 0.1805

**Analysis**: High semantic consistency. Terminology remains cohesive and focused across sections.


Evaluating: subtle_degradation_guide.md
(Expected: Poor readability, high semantic drift)
------------------------------------------------------
# Quality Report: subtle_degradation_guide.md

## Overall Score: 15.05/100

### Structure
- Headings: 4
- Paragraphs: 3
- Code Blocks: 0

**Analysis**: Document is properly partitioned with structural elements.

### Readability
- Flesch-Kincaid Reading Ease: 29.77
- Word Count: 134

**Analysis**: Score is penalized due to overly complex sentence structures.

**Action:** Simplify the following flagged sentences:
> "The virtual server typically necessitates approximately five minutes for complete initialization."

> "Prerequisites Prior to the initiation of the creation process for an EC2 instance, the verification of appropriate administrative authorizations is fundamentally required."

> "Next Steps Following the successful startup phase of the allocated hardware, the monitoring of its operational integrity can be achieved via the administrative dashboard."


### Fidelity & Consistency
- Semantic Consistency: 0.0539

**Analysis**: Score is heavily penalized due to high semantic drift.

**Action:** Unify your terminology. The following terms are used inconsistently across different sections:

> `provisioning`, `machine`, `select`, `virtual`, `workloads`



======================================================
 Demonstration Summary                                
======================================================
Notice how the tool explicitly caught the subtle degradation:
1. The Flesch-Kincaid metric heavily penalized the convoluted,
   passive sentences in the second guide.
2. The TF-IDF vectorization flagged the semantic drift
   (switching between VM, instance, server, and node).
======================================================
```
