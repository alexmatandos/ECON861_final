# ECON 8610 Final

## Step 1:
Packages needed: 'Pandas', 'sklearn', 'pickle', 'IMAGEIO', 'glob', 'numpy', 'math' and 'os'.
## Step 2:
Run 'run_data_cleaning.py' to clean data. Particularly, "fixing" the 'bathroom' variable, dropping the 'state' variable (since all observations are located in California), getting dummies for the remaining covariates and factorizing the dependent variable 'price_range'. Furthermore, it generates the "RGB" data from each observation .jpg file and merging with the above data, generating 'dataset_clean.csv'.
## Step 3:
The program 'run_machine_1.py' runs Random Forest and Logistic Regression machine learning models, returning accuracy scores and confusion matrices (2 x 2 and for each 'price_range').
## Step 4:
The program 'run_machine_2.py' works the same as the previous step but correcting for the corrupted rows, located between 10000th and 12000th observations.
## Step 5:
If you want to skip steps three and four, simply run 'run_boss_program.py' and it will return the accuracy scores for the Random Forest and Logistic Regression models for both. (In this order.)
## Bonus Question:
Run 'run_machine_3.py' to obtain the R-Squared scores for the Hedonic Pricing Linear Model. When using 'run_boss_program.py', the last array returned is the R-Squared scores.