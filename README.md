# Junior_Paper
## Code for Junior Independent Work "Investigating the Effects of Racial/Ancestral Bias in The Cancer Genome Atlas Breast Cancer Dataset on Classification and Survival Prediction"
### TCGA2STAT package adapted from Wan et al's work ([https://github.com/zhandong/TCGA2STAT](https://doi.org/10.1093/bioinformatics/btv677). See "Implementation" section of paper for full details.
It is imperative that we understand the effects of White/European biased data on machine learning
(ML) models. Using the The Cancer Genome Atlas (TCGA) breast cancer dataset, I create a variety
of machine learning tumor classifiers and survival predictors in R, trained and tested on the genomic
data of different subsets of the population based on patients’ genetic ancestry, and evaluate the
predictive power of the models on a number of performance metrics. Specifically, I try to answer
whether ancestry-specific models outperform others. Genetic ancestry appears to have little to
no impact on classifier performance, and ancestry-specificity seems to lowers survival prediction
performance. More research is needed to assess the feasibility of “-omics”-based, ancestry-specific
ML models.
