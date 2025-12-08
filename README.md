In Silico Optimization of Fendiline Derivatives targeting A549 Cancer Cells

Project Overview
The Challenge: During my MSc research, I synthesized a novel Fendiline derivative designed to target KRAS-driven lung cancer (A549 cells). Despite successful synthesis (53% yield), the compound showed poor cytotoxicity (IC50 > 100 muM) compared to the positive control, Cisplatin (IC50 ~ 11.5 muM).

The Hypothesis: Based on literature review and structural analysis, I hypothesized the failure was due to:
1.  High Lipophilicity: Leading to poor solubility in aqueous cell media.
2.  Reduced Basicity: Preventing the "lysosomal trapping" mechanism required for Fendiline-like drugs (CAD mechanism).

The Solution: Instead of abandoning the project, I built a Python pipeline using RDKit to computationally analyze the failed scaffold and design optimized analogues.

Methodology & Tools
Language: Python 3.12
Libraries: RDKit (Cheminformatics), Pandas (Data Analysis)
Workflow:
    1.  Digitized 2D structures of the synthesized derivative and parent drug (Fendiline).
    2.  Calculated physicochemical descriptors (LogP, TPSA, H-bond donors/acceptors) using Lipinski's Rule of 5.
    3.  Performed In Silico SAR (Structure-Activity Relationship) optimization to generate new candidates.


Key Findings

1. Diagnosis of Failure
My computational analysis confirmed the hypothesis.
Synthesized Derivative: LogP ~ 3.63. While lipophilic, the electron-withdrawing Fluorine substituent likely reduced the pKa of the amine, preventing lysosomal accumulation.
Fendiline (Parent): LogP ~ 5.56. Highly lipophilic but possesses the necessary basic nitrogen for trapping.

2. Optimization Strategy
I designed three new analogues to improve water solubility and basicity while retaining the core scaffold.

| Candidate ID | Modification | Predicted LogP | Outcome |
| Original | Fluorobenzyl | 3.63 | Failed (Insoluble/Low Activity) |
| Idea 1 | Hydroxyl | 3.19 | Improved Solubility (Best LogP) |
| Idea 3 | Morpholine | 3.32 | Top Candidate (Balanced Solubility + High pKa) |

Conclusion: The Morpholine-substituted analogue is the recommended lead for the next synthesis cycle. It restores the basic nitrogen required for the mechanism of action while improving predicted solubility by ~10%.


Contact
Sarona Jacob Anderson
linkedin.com/in/sarona-jacob-anderson-757218232  
Open to roles in Drug Discovery, Cheminformatics, and Computational Biology.
