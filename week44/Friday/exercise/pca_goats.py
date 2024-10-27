import os
import zipfile

import pandas as pd
import requests
from sklearn.impute import SimpleImputer
from tqdm import tqdm
from pandas_plink import read_plink
import dask.array as da
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA


def download_file(url: str, dest: str):
    """
    Download a file from a url and save it to a destination

    :param url: URL to download from
    :param dest: Destination to save the file to
    """
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    with open(dest, 'wb') as f:
        for chunk in tqdm(response.iter_content(chunk_size=8192), total=total_size / 8192,
                          unit='MB', unit_scale=8192 / (1024 * 1024)):
            f.write(chunk)


def unzip(zip_file: str):
    """
    Unzip a file to a destination

    :param zip_file: Path to the zip file
    """
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall()

url = ("https://github.com/Bjarke-M/Evolutionary_Thinking_2024/blob/"
       "fb17582a10b81c6b8ef9641222eb012a69c227fb/week44/Friday/data.zip?raw=true")

dest = os.getcwd() + "/goats.zip"
download_file(url, dest)
unzip(dest)

(bim, fam, bed) = read_plink(os.getcwd() + "/data/snps")

# Drop mitochondrial and sex chromosome SNPs based on your data’s chromosome annotations
# Filter chromosomes in bim DataFrame
autosomal_snps = bim['chrom'].astype(int) <= 29
bed_filtered = bed[autosomal_snps]

# Filter individuals (axis=1) with >5% missing SNPs
bed_filtered = bed[:, da.isnan(bed).mean(axis=0) <= 0.05]

# Filter SNPs (axis=0) with >5% missing genotypes
bed_filtered = bed_filtered[da.isnan(bed_filtered).mean(axis=1) <= 0.05, :]

# Filter SNPs with MAF < 0.05
maf = da.nanmean(bed_filtered, axis=1) / 2
bed_filtered = bed_filtered[(maf >= 0.05) & (maf <= 0.95), :]

# perform computation and obtain numpy array
bed_filtered = bed_filtered.compute()

# Fit and transform the data to fill NaNs
# You can change the strategy to 'median', 'most_frequent', or 'constant'
bed_imputed = SimpleImputer(strategy='mean').fit_transform(bed_filtered)

pca = PCA(n_components=2)  # Number of components to keep
pca_result = pca.fit_transform(bed_imputed.T)

# Convert PCA result to DataFrame for better handling
pca_df = pd.DataFrame(data=pca_result, columns=['PC1', 'PC2'])

# Get explained variance
explained_variance = pca.explained_variance_ratio_ * 100

# Add sample IDs for plotting
#pca_df['SampleID'] = fam['id'].values

# Plot PCA
plt.figure(figsize=(10, 6))
plt.scatter(pca_df['PC1'], pca_df['PC2'], alpha=0.5)
#for i, txt in enumerate(pca_df['SampleID']):
#    plt.annotate(txt, (pca_df['PC1'][i], pca_df['PC2'][i]), fontsize=8, alpha=0.7)

plt.title('PCA of SNP Data')
plt.xlabel(f'PC1 ({explained_variance[0]:.2f}% variance explained)')
plt.ylabel(f'PC2 ({explained_variance[1]:.2f}% variance explained)')
plt.grid()
plt.show()

pass