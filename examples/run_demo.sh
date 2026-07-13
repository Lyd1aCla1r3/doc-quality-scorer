#!/usr/bin/env bash

echo "======================================================"
echo " Running Document Quality Scorer - Subtlety Demo      "
echo "======================================================"
echo ""
echo "Evaluating: cohesive_guide.md"
echo "(Expected: High readability, high semantic consistency)"
echo "------------------------------------------------------"
doc-quality-scorer cohesive_guide.md --format markdown
echo ""

echo "Evaluating: subtle_degradation_guide.md"
echo "(Expected: Poor readability, high semantic drift)"
echo "------------------------------------------------------"
doc-quality-scorer subtle_degradation_guide.md --format markdown
echo ""

echo "======================================================"
echo " Demonstration Summary                                "
echo "======================================================"
echo "Notice how the tool explicitly caught the subtle degradation:"
echo "1. The Flesch-Kincaid metric heavily penalized the convoluted,"
echo "   passive sentences in the second guide."
echo "2. The TF-IDF vectorization flagged the semantic drift"
echo "   (switching between VM, instance, server, and node)."
echo "======================================================"
