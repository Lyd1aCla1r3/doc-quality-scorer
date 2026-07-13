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
