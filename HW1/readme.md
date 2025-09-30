# Biostat 915 Homework 1: Analysis of Worldwide Goat Population Genetics

**Student Name:** Xi Chen 

---

## Introduction

This report presents an analysis of genetic data from worldwide goat populations using PLINK format files (.bed, .bim, .fam). The dataset contains 4,653 individuals from 144 populations with 53,347 SNP markers across 31 chromosomes. The analysis includes exploratory data analysis, missingness assessment, principal component analysis for population structure, and genome-wide association study simulation.

---

## Q1: Exploratory Data Analysis

### Dataset Overview

The goat genetic dataset consists of three interconnected files:

**1. FAM File (Individual Information)**
- Contains 4,653 individuals from 144 distinct populations
- Population sizes range from 1 to 413 individuals (mean: 32.3)
- Sex information: 95.9% unknown, 0.7% male, 3.4% female
- Pedigree information largely absent (unrelated individuals)
- Phenotypes intentionally missing for simulation exercise

**2. BIM File (SNP Information)**
- Contains 53,347 SNP markers
- Distributed across 31 chromosomes
- Physical positions: 97% available
- All SNPs have complete allele information

**3. BED File (Genotype Matrix)**
- Matrix dimensions: 4,653 individuals × 53,347 SNPs
- Overall genotype call rate: 96.97%
- Data quality: Excellent (low missingness)

### Missingness Observations

**FAM File:**
- Essential identifiers (population ID, individual ID): 100% complete
- Parental information: Mostly unknown (expected for population study)
- Phenotype data: Intentionally missing (for Q4 simulation)

**BIM File:**
- SNP identifiers and alleles: 100% complete
- Physical positions: 97% complete
- Does not affect analysis as chromosome assignments are complete

**BED File:**
- Overall missing rate: 3.03%
- Individual-level: Mean 3.03%, median 2.34%
- SNP-level: Mean 3.03%, median 0.90%
- 95.0% of individuals have <5% missing genotypes
- 85.6% of SNPs have <2% missing calls
- Missingness is randomly distributed with no systematic patterns

### Exploratory Visualizations

**Figure 1: Population Demographics**
- Shows distribution of individuals across populations
- Top 3 populations: ANG (413 individuals), BOE (333), ALP (279)
- Sex distribution predominantly unknown (95.9%)
- SNP distribution across 31 chromosomes

**Figure 2: Missingness Patterns**
- Individual missingness: Most individuals (95%) have <5% missing
- SNP missingness: Most SNPs (85.6%) have <2% missing
- No concentrated patterns of missingness
- Confirms high data quality

### Interpretation

The dataset demonstrates excellent quality with minimal missingness (3.03%). The low and evenly distributed missing rate indicates successful quality control filtering as mentioned in the original paper. With 144 populations spanning worldwide goat diversity, this dataset is well-suited for population genetics and association analyses.

---

## Q2: Genotype Missingness

### Detailed Missingness Analysis

**Overall Statistics:**
- Total missing genotypes: ~7.5 million out of 248 million total calls
- Missing rate: 3.03%
- Call rate: 96.97%

**Individual-Level Pattern:**
- Mean missing rate: 3.03% per individual
- Range: [0.33%, 76.98%]
- Median: 2.34%
- 95.0% of individuals have <5% missing genotypes

**SNP-Level Pattern:**
- Mean missing rate: 3.03% per SNP
- Range: [0.17%, 100%]
- Median: 0.90%
- 85.6% of SNPs have <2% missing calls

**Distribution by Population:**
Examined top 10 populations - missingness rates are relatively consistent across populations, showing uniform data quality.

### Data Quality Assessment

According to the paper, this data has already been filtered for:
- Individual genotype call rate
- SNP call rate
- Other quality control metrics

Our analysis confirms:
1. Low overall missingness (3.03%)
2. No systematic patterns suggesting technical artifacts
3. Random distribution of missing values
4. Data ready for analysis without additional filtering

### Interpretation

The genotype missingness distribution from the BED file shows the data has been properly quality-controlled. The low and evenly distributed missingness (96.97% call rate) indicates reliable genotyping. A few individuals with higher missingness exist but constitute a small fraction (<5%) of the dataset and do not compromise overall quality.

---

## Q3: PCA to Visualize Ancestry Distribution

### Data Processing Steps

**Step 1: Sample Selection**
- Selected 1,500 individuals randomly from 4,653 total
- Selected 8,000 SNPs systematically from 53,347 total
- Rationale: Computational efficiency while maintaining statistical power

**Step 2: Missing Data Handling**
- Method: Mean imputation
- Replaced missing genotypes with column (SNP) means
- Standard approach for PCA on genetic data

**Step 3: Standardization**
- Applied StandardScaler to normalize features
- Essential for PCA to prevent scale-dependent bias

**Step 4: PCA Computation**
- Computed 10 principal components
- Used sklearn.decomposition.PCA

### Results

**Variance Explained:**
- PC1: 5.40% of genetic variance
- PC2: 3.75% of genetic variance
- PC3: 2.53% of genetic variance
- First 2 PCs: 9.15% cumulative variance
- First 5 PCs: 13.99% cumulative variance

**Figure 3: PCA Analysis**
[Insert your PCA plots]

**Left panel (PC1 vs PC2):**
- Shows clear population clustering
- Top 20 populations displayed with distinct colors
- Genetic structure reflects geographic origins
- First two PCs capture 9.15% of total genetic variance

**Right panel (PC2 vs PC3):**
- Reveals finer population structure
- Additional genetic variation patterns
- PC2 vs PC3 captures an additional layer of population differentiation

### Component Selection Method

Based on variance explained:
- First 2 components capture major population structure (9.15%)
- First 5 components capture 13.99% of variance
- Diminishing returns after PC5
- For GWAS correction, using top 3-5 PCs would be appropriate

### Interpretation

The PCA successfully captures population genetic structure among 144 worldwide goat populations. Clear clustering in PC space indicates:
1. Genetic differentiation among worldwide goat populations
2. Population stratification that must be accounted for in association studies
3. Geographic/ancestral patterns in genetic variation

The analysis validates the use of PCA for:
- Population structure visualization
- Selecting population subsets for GWAS
- Providing covariates for association analysis

---

## Q4: Simulate Phenotypes and Run Simple GWAS

### Data Subset Selection

**Based on Q3 PCA analysis, selected:**
- 3 largest populations: ANG, BOE, ALP
- Total individuals: 1,025 from these populations
- Rationale: Computational efficiency and largest sample sizes

### Data Processing Steps

**Step 1: Phenotype Simulation**
- Randomly assigned case/control status
- Cases: 501 individuals (48.9%)
- Controls: 524 individuals (51.1%)
- Random seed: 123 (for reproducibility)
- Note: Random assignment means no true genetic associations expected

**Step 2: SNP Selection**
- Tested 5,000 SNPs randomly selected from 53,347 total
- Rationale: Demonstrate GWAS workflow with manageable computation

**Step 3: Association Testing**
- Method: Chi-square test of independence
- Null hypothesis: No association between genotype and phenotype
- Significance threshold: p < 0.05
- Quality filter: Excluded SNPs with <10 valid genotypes

### Results

**Association Statistics:**
- SNPs tested: 5,000
- Significant SNPs (p<0.05): 231 (4.62%)
- Expected false positives: ~250 (5% of 5,000)
- Minimum p-value: 1.05×10⁻⁴
- Maximum -log10(p): 3.98



**Manhattan Plot (Top panel):**
- Shows -log10(p-values) across SNPs
- Red line indicates significance threshold (p=0.05, -log10(p)=1.3)
- 231 SNPs cross threshold
- Maximum -log10(p) = 3.98, no extreme outliers
- Distribution consistent with null hypothesis

**Q-Q Plot (Bottom panel):**
- Observed vs expected p-value distribution
- Points follow expected line closely
- Slight deviation at tail representing 231 significant SNPs
- No evidence of population stratification or systematic inflation

### Interpretation

**Key Findings:**
1. Observed 231 significant SNPs vs ~250 expected under null (4.62% vs 5%)
2. Very close to expected false positive rate
3. Q-Q plot shows excellent adherence to null distribution
4. No evidence of systematic bias or true associations

**Conclusions:**
- Random phenotype assignment resulted in no true associations (as expected)
- Significant SNPs (4.62%) are consistent with false positive expectations
- GWAS workflow successfully implemented and validated
- Analysis framework ready for real phenotype data

**Limitations:**
- Subset of 3 populations (1,025 of 4,653 individuals)
- Random phenotypes (no biological signal)
- Limited SNP coverage (5,000 of 53,347)
- No population structure correction applied

**Real-World Application:**
With actual phenotype data, this framework would:
1. Include population structure correction (PC-based covariates)
2. Apply multiple testing correction (Bonferroni: p<9.4×10⁻⁷, or FDR)
3. Test all quality-controlled SNPs
4. Validate findings in independent cohorts

The observed/expected ratio of 0.92 (231/250) demonstrates excellent calibration and no inflation.
