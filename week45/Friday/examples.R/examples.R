#### load data
genes <- read.table("/Users/au612643/Desktop/friday/genes.txt", sep = "\t", head=T)
variants <- read.table("/Users/au612643/Desktop/friday/variants.txt", sep = "\t", head=T)
copyNumbers <- read.table("/Users/au612643/Desktop/friday/copyNumbers.txt", sep = "\t", head=T)

############################################################################################
########---- subset function example: Extracting variants found in the gene ZFY ----########
############################################################################################

## information about the ZFY gene is in the third row of the genes data.frame
## to extract variants for ZFY we must subset the data.frame "variants" to positions within the ZFY coordinates
variantsZFY <- subset(variants, (Position>=genes$coorStart[3]) & (Position<=genes$coorEnd[3]))

## if we are only interested in SNP variants we can subset further
variantsZFYsnpOnly <- subset(variantsZFY, Type == "SNP")

## the "variantsZFYsnpOnly" data.frame can also be created in a single step
variantsZFYsnpOnly <- subset(variants, (Position>=genes$coorStart[3]) & (Position<=genes$coorEnd[3]) & (Type == "SNP"))

## calculating the number of SNPs for the ZFY gene
dim(variantsZFYsnpOnly)[1]

############################################################################################
###########---- melt function example: Melting the "copyNumbers" data.frame ----############
############################################################################################

## the melt function is part of the "reshape2" library so we first need to install it and then load it.
install.packages("reshape2")
library("reshape2")

## We will now melt the "copyNumbers" data.frame so that we retain the "Haplogroup" and "Ind" as columns,
## and convert columns with gene symbol names into rows. This will allow us to subset the new data.frame
## by gene names.
cnMelt <- melt(data = copyNumbers, id.vars = c("Haplogroup", "Ind"), measure.vars = genes$Symbol)

## cnMelt data.frame contains gene names in rows of the "variable" column and copy number values are in
## the "value" column. Note that the values in "Haplogroup" and "Ind" columns have mutliplied in correspondence
## to the number of genes. We can now subset the cnMelt data.frame to the ZFY gene.
cnZFY <- subset(cnMelt, variable == "ZFY")

## calculating the mean copy number value for the ZFY gene across individuals
mean(cnZFY$value)
