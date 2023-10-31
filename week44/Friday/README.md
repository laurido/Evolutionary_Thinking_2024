# Friday Week44

## Population structure of Goats and an introduction to the PCA

We will recreate this research paper to some extend [goat research paper](https://gsejournal.biomedcentral.com/counter/pdf/10.1186/s12711-018-0422-x.pdf) you don't have to read it

Introduction to a PCA by some generative AI (you know of whom I speak)

Principal Component Analysis (PCA) is a versatile statistical technique that finds its utility in a wide array of fields, including genetics, by effectively simplifying complex high-dimensional data while preserving its essential variance. PCA operates by transforming the original data into a new coordinate system, comprised of orthogonal axes known as principal components, which are the linchpin for unraveling significant patterns within the data.

The PCA process commences with standardizing the data to ensure no single variable dominates the analysis. Subsequently, it hinges on the computation of the covariance matrix, which uncovers the interrelationships between variables, reflecting how they co-vary and their linear associations. Eigenvalue decomposition follows, extracting eigenvalues and eigenvectors from the covariance matrix. Eigenvalues unveil the amount of variance that each principal component explains, while eigenvectors define the principal components' directions.

Researchers typically choose a subset of the principal components, ranked by their corresponding eigenvalues, capturing a substantial portion of the variance in the data. This selection can be predicated on predetermined criteria, such as a desired percentage of explained variance. The chosen principal components are then employed to project the original data onto this reduced dimensionality space, resulting in a more compact dataset.

In the realm of population genetics, PCA serves as a powerful tool for diverse applications. It aids in unveiling the genetic structure of populations, effectively visualizing clusters and patterns indicative of different geographic regions or subpopulations. Moreover, PCA plays a pivotal role in quality control, identifying outliers and mixed-ancestry individuals to maintain the integrity of genetic datasets. Additionally, it is instrumental in correcting for population stratification in genome-wide association studies, ensuring more accurate results. Genetic clustering, evolutionary studies, and the elucidation of genetic relatedness among species or subspecies are also well-served by PCA.

In essence, PCA simplifies the complexity of high-dimensional genetic data and empowers researchers to visualize and interpret genetic diversity, evolutionary relationships, and population structures, making it an indispensable tool in the field of population genetics.

## This exercise requires a program called plink, which can be downloaded either in conda or as a standalone program, if you have time download it beforehand 




