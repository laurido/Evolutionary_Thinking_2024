## Chapter 7: Selection

The following exercises parallel the exercises following Chapter 7 from
the textbook (An introduction to Population Genetics - Nielsen and
Slatkin). This document can be updated with comments and be compiled to
a pdf version using the Knit command. Feel free to do it so! Good luck!
:)

This is an R Markdown document. Markdown is a simple formatting syntax
for authoring HTML, PDF, and MS Word documents. For more details on
using R Markdown see <http://rmarkdown.rstudio.com>.

When you click the **Knit** button a document will be generated that
includes both content as well as the output of any embedded R code
chunks within the document. You can embed an R code chunk like this:

    #Exercise 7.1

    # Here we have a haploid species with a novel allele A. We are given:

    s_coef <- 0.01

    # a. We now have an initial and a final allele freq for A (0.1 and 0.9, respectively). As explained in Box 7.1, the time needed to transition from fA_0 to fA_1

    fA_0 <- 0.1
    fA_1 <- 0.9

    # we define a function for calculating the time difference, based on the formula in Box 7.1:

    timefct <- function(sel_cf, fA_init, fA_fin){
      
      # simple function to incorporate the formula:
      
      plhlder <- ((fA_init/fA_fin)-fA_init)/(1-fA_init)
      
      trtime <- (log(plhlder)/log(1-sel_cf))
      
      return(trtime)
    }

    # then apply it for our s:

    timefct(s_coef, fA_0, fA_1)

    ## [1] 437.244

    # b. This is essentially the same question, but now with:

    s_coef <- 0.011

    # we solve it the same way:

    timefct(s_coef, fA_0, fA_1)

    ## [1] 397.2941

    # note that the textbook answer, 4370, is wrong and does not really make much sense

    #Exercise 7.2

    # for N=10^4, the initial allele frequency was:
    N <- 10^4
    f_A0 <- 1/(2*N)

    f_At <- 0.9
    freq_A <- 1/(2*N)
    s_coef <- 0.01

    # from Box 7.1:
    time_gen <- log(abs((f_A0/f_At - f_A0)/(1-f_A0)))/log(1-s_coef)
    print(time_gen)

    ## [1] 1204.006

    # same for N=10^5:

    N <- 10^5
    f_A0 <- 1/(2*N)
    f_At <- 0.9
    time_gen <- log(abs((f_A0/f_At - f_A0)/(1-f_A0)))/log(1-s_coef)
    print(time_gen)

    ## [1] 1433.116

    #Exercise 7.3

    # this question is ambiguously worded, but it means to say that the growth rate for A is 5% lower than the growth rate for a:

    # w_A = (1-0.05)*w_a = 0.95*w_a; so from equation (7.4):

    # w_a/0.95w_a = 1-s
    # 1/0.95 = 1-s
    # s = 1-1/0.95
    # so:

    s_coef <- 1-(1/0.95)

    # after this, as in 7.1, we use the same function - this time for a decreasing allele freq:

    fA_0 <- 0.1
    fA_1 <- 0.01

    timefct <- function(sel_cf, fA_init, fA_fin){
      
      # simple function to incorporate the formula:
      
      plhlder <- ((fA_init/fA_fin)-fA_init)/(1-fA_init)
      
      trtime <- (log(plhlder)/log(1-sel_cf))
      
      return(trtime)
    }

    # applying it gives:

    timefct(s_coef, fA_0, fA_1)

    ## [1] 46.74871

    # we get a slightly different result from the textbook because we did not round s_coef

    #Exercise 7.4

    # we are first given:

    s_aa <- 1 #as homozygotes for the recessive allele are lethal

    f_a <- 0.02 #again ambiguous wording within the problem - this is the allele frequency, as explained a little further

    # a. at mutation-selection equilibrium, mutation rate at the CF locus can be calculated from formula (7.13):

    #f_a = sqrt(mu/s_aa), from which:
    #f_a^2 = mu/s_aa
    #mu = s_aa*f_a^2

    mu <- s_aa*f_a^2
    print(mu)

    ## [1] 4e-04

    # b. now equilibrium is said to be maintained through heterozygote advantage; so, from formula (7.9):

    #(1-f_a) = s_aa/(s_AA + s_aa)
    #s_AA = s_aa*f_a/(1-f_a)

    s_AA <- s_aa*f_a/(1-f_a)
    print(s_AA)

    ## [1] 0.02040816

    # we also know from formula (7.8) that:
    #v_AA/v_aA = 1-s_AA
    # so, for our ambiguously worded problem:
    viab_prop <- 1-s_AA
    print(viab_prop)

    ## [1] 0.9795918

    # we can see that heterozygotes are <slightly> more advantageous

    #Exercise 7.5

    # A at H-W equilibrium, so f_A(t) constant. We are given:

    f_A <- 0.11
    s_AA <- 0.5

    # we can use equation (7.9) that describes f_A at equilibrium as a function of selection coefficients for the two homozygote genotypes, as we already know the equilibrium frequency:

    # f_A = s_BB/(s_AA + s_BB)

    # from which we get s_BB:

    #f_A*s_AA + f_A*s_BB = s_BB
    #s_BB - f_A*s_BB = f_A*s_AA
    #s_BB(1-f_A) = f_A*s_AA
    #s_BB = f_A*s_AA/(1-f_A)

    s_BB <- f_A*s_AA/(1-f_A)
    print(s_BB)

    ## [1] 0.06179775

    #Exercise 7.6

    # changed notations from B/b to A/a to reduce potential confusion
    # under H-W, we know that in the first generation:

    f_A0 <- 1/4

    f_AA0 <- f_A0^2
    f_Aa0 <- 2*f_A0*(1-f_A0)
    f_aa0 <- (1-f_A0)^2

    # there is no fertility effect on our locus; we also know the viabilities; so in the next generation we will have:

    v_AA <- 1/5
    v_Aa <- 1/6
    v_aa <- 1/10
    v_avg <- v_AA*(f_A0^2)+2*v_Aa*(f_A0*(1-f_A0))+v_aa*((1-f_A0)^2)

    # we can then calculate the new allele frequency:

    f_AA1 <- v_AA*(f_A0^2)/v_avg
    f_Aa1 <- 2*v_Aa*(f_A0*(1-f_A0))/v_avg

    f_A1 <- f_AA1 + f_Aa1/2

    print(f_A1)

    ## [1] 0.3333333

    #Exercise 7.7

    # under H-W, we are given:

    f_S <- 0.2
    f_A <- 1-f_S
    v_SS <- 0.1
    # v_AA <- 0.85*v_AS; but then we are given:
    v_AS <- 1
    # so then:
    v_AA <- 0.85

    # a. From Box 7.3, the third equation:

    v_avg <- v_AA*f_A^2 + 2*v_AS*f_A*f_S + v_SS*f_S^2

    print(v_avg)

    ## [1] 0.868

    # b. We first calculate genotype frequencies before selection:

    f_AA <- f_A^2
    f_AS <- 2*f_A*f_S
    f_SS <- f_S^2

    # then, using the 4th row of equations from Box 7,3, we calculate:

    fpr_AA <- f_AA*v_AA/v_avg
    fpr_AS <- f_AS*v_AS/v_avg
    fpr_SS <- f_SS*v_SS/v_avg

    print(fpr_AA)

    ## [1] 0.6267281

    print(fpr_AS)

    ## [1] 0.3686636

    print(fpr_SS)

    ## [1] 0.004608295

    #Exercise 7.8

    N <- 10^4

    # no drift; genic selection for newly introduced allele; we have:

    f_B0 <- 1/(2*N)
    f_B1 <- 0.99

    # apparently we assume a selection coefficient between 0.1 and 0.2, corresponding to v_AB of 0.8-0.9 (where A is the initial dark allele and B is the introduced light allele)

    s_coef <- 0.1
    t_gen <- log((f_B0/f_B1 - f_B0)/(1-f_B0))/log(1-s_coef)
    print(t_gen)

    ## [1] 137.609

    s_coef <- 0.2
    t_gen <- log((f_B0/f_B1 - f_B0)/(1-f_B0))/log(1-s_coef)
    print(t_gen)

    ## [1] 64.97413

    #Exercise 7.9

    #we first create dataframe containing all maternal/paternal genotype combinations and their offspring ratios:

    mat_v <- c("AA", "AA", "AA", "Aa", "Aa", "Aa", "aa", "aa", "aa")
    pat_v <- c("AA", "Aa", "aa", "AA", "Aa", "aa", "AA", "Aa", "aa")
    freq_v <- c(1/16, 1/8, 1/16, 1/8, 1/4, 1/8, 1/16, 1/8, 1/16)
    fert_v <- c(1, 1, 1, 1, 1, 1, 1, 1, 1/2)
    AA_v <- c(1, 1/2, 0, 1/2, 1/4, 0, 0, 0, 0)
    Aa_v <- c(0, 1/2, 1, 1/2, 1/2, 1/2, 1, 1/2, 0)
    aa_v <- c(0, 0, 0, 0, 1/4, 1/2, 0, 1/2, 1)

    matepairs <- data.frame(mat_v, pat_v, freq_v, fert_v, AA_v, Aa_v, aa_v)
    matepairs

    ##   mat_v pat_v freq_v fert_v AA_v Aa_v aa_v
    ## 1    AA    AA 0.0625    1.0 1.00  0.0 0.00
    ## 2    AA    Aa 0.1250    1.0 0.50  0.5 0.00
    ## 3    AA    aa 0.0625    1.0 0.00  1.0 0.00
    ## 4    Aa    AA 0.1250    1.0 0.50  0.5 0.00
    ## 5    Aa    Aa 0.2500    1.0 0.25  0.5 0.25
    ## 6    Aa    aa 0.1250    1.0 0.00  0.5 0.50
    ## 7    aa    AA 0.0625    1.0 0.00  1.0 0.00
    ## 8    aa    Aa 0.1250    1.0 0.00  0.5 0.50
    ## 9    aa    aa 0.0625    0.5 0.00  0.0 1.00

    # a. first we calculate the average viability:

    viab_avg <- sum(freq_v)-(freq_v[9]*fert_v[9])

    #we use the genotype frequency formulas in Box 7.3; in the second generation, the newborn offspring will have the frequencies:

    fpr_AA <- sum(matepairs$freq_v*matepairs$fert_v*matepairs$AA_v)/viab_avg
    fpr_Aa <- sum(matepairs$freq_v*matepairs$fert_v*matepairs$Aa_v)/viab_avg
    fpr_aa <- sum(matepairs$freq_v*matepairs$fert_v*matepairs$aa_v)/viab_avg

    print(cat (fpr_AA, fpr_Aa, fpr_aa))

    ## 0.2580645 0.516129 0.2258065NULL

    # b. to see if the genotype frequencies match H-W proportions, we first calculate the offspring allele A freq:

    fpr_A <- fpr_AA + fpr_Aa/2

    #then we simply test if the expected f_AA under H-W is equal to the one we calculated above:

    fexp_AA <- fpr_A^2

    print(fexp_AA == fpr_AA)

    ## [1] FALSE

    #Exercise 7.10

    # under H-W; no effect on viability, but reduced heterozygote fertility:

    f_AA0 <- 0.01
    f_Aa0 <- 0.18
    f_aa0 <- 0.81

    f_A0 <- 0.1

    # a. We can build a dataframe showing fertilities for all mating pairs:

    pat_v <- c("AA", "AA", "AA", "Aa", "Aa", "Aa", "aa", "aa", "aa")
    mat_v <- c("AA", "Aa", "aa", "AA", "Aa", "aa", "AA", "Aa", "aa")
    fert_v <- c(1, 0.5, 1, 0.5, 0.25, 0.5, 1, 0.5, 1)

    fert_df <- data.frame(pat_v, mat_v, fert_v)

    fert_df

    ##   pat_v mat_v fert_v
    ## 1    AA    AA   1.00
    ## 2    AA    Aa   0.50
    ## 3    AA    aa   1.00
    ## 4    Aa    AA   0.50
    ## 5    Aa    Aa   0.25
    ## 6    Aa    aa   0.50
    ## 7    aa    AA   1.00
    ## 8    aa    Aa   0.50
    ## 9    aa    aa   1.00

    # b. as the problem says - translocations reduce heterozygote fertility because half of their gametes are aneuploid, resulting in non-viable embryos. Also, for either allele being rare, most of its copies will be present in heterozygotes (which have lower viability than either homozygote); over time, this will drive extinction of the rare allele and fixation of the other.

    #Exercise 7.11

    # a. Same as before, for the genotypes table in Table 7.1, only now Rr are (Rh-):

    mat_v <- c("RR", "Rr", "Rr", "Rr", "rr")
    pat_v <- c("all", "RR", "Rr", "rr", "all")
    freq_v <- c("f_RR", "f_Rr*f_RR", "f_Rr^2", "f_Rr*F_rr", "f_rr")
    viab_v <- c("1", "1-s/2", "1-s/4", "1", "1")

    matepairs <- data.frame(mat_v, pat_v, freq_v, viab_v)
    matepairs

    ##   mat_v pat_v    freq_v viab_v
    ## 1    RR   all      f_RR      1
    ## 2    Rr    RR f_Rr*f_RR  1-s/2
    ## 3    Rr    Rr    f_Rr^2  1-s/4
    ## 4    Rr    rr f_Rr*F_rr      1
    ## 5    rr   all      f_rr      1

    # note that, under the new dominance model, any rr mother would result in r-phenotype (Rh-) offspring; viability is reduced only when maternal genotype is Rr and the paternal one is either RR or Rr; since paternal RR would result in twice as many Rr offspring as paternal Rr, viability loss in RRxRr would be twice as large as for RrxRr

    # b. As heterozygote disadvantage is still the observed pattern of selection, the trends shown in Figure 7.7 still apply - if either allele would be very rare, there would be decreased frequency - evidencing, as before, disruptive selection

    #Exercise 7.12

    # Very large population; five alleles S1-S5 of equal frequency 0.2:

    f_S1 <- 0.2
    f_S2 <- f_S1
    f_S3 <- f_S1
    f_S4 <- f_S1
    f_S5 <- f_S1

    # a. Random mating and no homozygotes would give:

    #S1S2; S1S3; S1S4; S1S5; S2S3; S2S4; S2S5; S3S4; S3S5; S4S5
    #a total of 10 possible heterozygotes, each at frequency 0.1

    # b. There is now a newly introduced allele S6; this has to be present in a heterozygote; since all other alleles have equal frequencies, it does not matter which one we pick; let's go with S1, our heterozygote will be S1S6; therefore, with non-viable self-fertilisation:

    # S1 pollen from the mutant will not be able to fertilise S1 hets from above, so 0.4 of other individuals; this is also the case for any given original allele in the population.
    # S6 pollen will be able to fertilise all other individuals; so whereas any other individual would fertilise 0.6*0.6 others, the mutant would be able to fertilise 0.6*1. So it will have:

    print((1*0.6)/(0.6*0.6))

    ## [1] 1.666667

    print("as many offspring as any other individual.")

    ## [1] "as many offspring as any other individual."

    # we can plot the cases by first defining the function for average viability based on the formula:
    avg_viab <- function(f_A, v_AA, v_Aa, v_aa){
      avviab <- ((f_A^2)*v_AA + 2*f_A*(1-f_A)*v_Aa + ((1-f_A)^2)*v_aa)
      return(avviab)
    }

    # now we define our viabilities and plot the avg_viab function across all possible f_A values:
    f_A <- seq(0, 1, by = 0.01)

    set_1 <- list(v_AA = 0.5, v_Aa = 0.4, v_aa = 0.3)
    set_2 <- list(v_AA = 0.4, v_Aa = 0.5, v_aa = 0.3)
    set_3 <- list(v_AA = 0.5, v_Aa = 0.3, v_aa = 0.4)

    # we then calculate the average viability for each case:
    y_values_1 <- sapply(f_A, function(f) avg_viab(f, v_AA = set_1$v_AA, v_Aa = set_1$v_Aa, v_aa = set_1$v_aa))
    y_values_2 <- sapply(f_A, function(f) avg_viab(f, v_AA = set_2$v_AA, v_Aa = set_2$v_Aa, v_aa = set_2$v_aa))
    y_values_3 <- sapply(f_A, function(f) avg_viab(f, v_AA = set_3$v_AA, v_Aa = set_3$v_Aa, v_aa = set_3$v_aa))

    # and plot the curves (remember how colours are assigned to each curve):
    plot(f_A, y_values_1, type = "l", col = "blue", xlab = "f_A", ylab = "avg_viab", ylim = range(c(y_values_1, y_values_2, y_values_3)))
    lines(f_A, y_values_2, col = "red")
    lines(f_A, y_values_3, col = "green")

    # we can also add a legend to more easily follow what each curve corresponds to:
    legend("topright", legend = c("Set 1", "Set 2", "Set 3"), col = c("blue", "red", "green"), lty = 1)

![](NS_ch7_files/figure-markdown_strict/unnamed-chunk-13-1.png)
