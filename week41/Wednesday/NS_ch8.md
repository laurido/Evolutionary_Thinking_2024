## Chapter 8: Selection in a Finite Population

The following exercises parallel the exercises following Chapter 8 from
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

    #Exercise 8.1

    # we are given:

    mu <- 2.2*(10^-9)

    # a. for selection coefficient at multiple N:

    s_coef <- -0.001
    N1 <- 10^4
    N2 <- 10^3
    N3 <- 10^2

    # a. We use formulas (8.1) and (8.2):

    u_sN1 <- (1-exp(-2*s_coef))/(1-exp(-4*N1*s_coef))
    r_sN1 <- 2*N1*mu*u_sN1
    print(r_sN1)

    ## [1] 3.742293e-25

    u_sN2 <- (1-exp(-2*s_coef))/(1-exp(-4*N2*s_coef))
    r_sN2 <- 2*N2*mu*u_sN2
    print(r_sN2)

    ## [1] 1.643491e-10

    u_sN3 <- (1-exp(-2*s_coef))/(1-exp(-4*N3*s_coef))
    r_sN3 <- 2*N3*mu*u_sN3
    print(r_sN3)

    ## [1] 1.791046e-09

    # b. We just calculate the deleterious substitutions to all mutations ratio:

    fr_ratio1 <- r_sN1/mu
    print(fr_ratio1)

    ## [1] 1.701042e-16

    fr_ratio2 <- r_sN2/mu
    print(fr_ratio2)

    ## [1] 0.07470412

    fr_ratio3 <- r_sN3/mu
    print(fr_ratio3)

    ## [1] 0.8141118

    #Exercise 8.2

    #same as before, but now s_coef will be positive:

    mu <- 2.2*(10^-9)

    s_coef <- 0.001
    N1 <- 10^4
    N2 <- 10^3
    N3 <- 10^2

    # a.

    u_sN1 <- (1-exp(-2*s_coef))/(1-exp(-4*N1*s_coef))
    r_sN1 <- 2*N1*mu*u_sN1
    print(r_sN1)

    ## [1] 8.791206e-08

    u_sN2 <- (1-exp(-2*s_coef))/(1-exp(-4*N2*s_coef))
    r_sN2 <- 2*N2*mu*u_sN2
    print(r_sN2)

    ## [1] 8.955227e-09

    u_sN3 <- (1-exp(-2*s_coef))/(1-exp(-4*N3*s_coef))
    r_sN3 <- 2*N3*mu*u_sN3
    print(r_sN3)

    ## [1] 2.666588e-09

    # b.

    fr_ratio1 <- r_sN1/mu
    print(fr_ratio1)

    ## [1] 39.96003

    fr_ratio2 <- r_sN2/mu
    print(fr_ratio2)

    ## [1] 4.070558

    fr_ratio3 <- r_sN3/mu
    print(fr_ratio3)

    ## [1] 1.212085

    #Exercise 8.3

    # we have a recessive advantageous mutant for allele A; we are given:

    fix_prob <- 0.002

    N <- 10^4

    # and we know that fix_prob = sqrt(2*s_coef/N*pi); we then extract s_coef as:

    s_coef <- (fix_prob^2 * N * pi)/2
    print(s_coef)

    ## [1] 0.06283185

    #Exercise 8.4

    # we know:
    L_seq <- 10^3
    d_seq <- 4

    # and we would like to use formula (8.3), but for that we also need the time of species divergence, which the textbook answers provide as:

    T_div <- 6*10^6

    # then we just apply the formula:

    r_nss <- d_seq/(2*L_seq*T_div)
    print(r_nss)

    ## [1] 3.333333e-10

    #Exercise 8.5

    # we are given:

    r_N_ins <- 0.13 * 10^-9

    r_N_hist <- 10^-13

    mu <- 2.2 * 10^-9

    # we then want to calculate alpha. We know that r_N = (1-alpha) * mu from formula (8.4):

    ndm_frac_ins <- 1-(r_N_ins/mu)
    print(ndm_frac_ins)

    ## [1] 0.9409091

    ndm_frac_hist <- 1-(r_N_hist/mu)
    print(ndm_frac_hist)

    ## [1] 0.9999545

    #Exercise 8.6

    # we are given:

    r_syn <- 0.8*10^-9
    N <- 100
    mu <- 2.2*10^-9

    del_ns_ratio <- 2/3
    sdel_ss_ratio <- 1/3
    s_coef <- 10^-3

    # we want to calculate ndm_alpha; we know that r_syn = (1-ndm_alpha)*mu + sdel_ss_ratio*ndm_alpha*mu*2*N*u_sn/3
    # from (8.1) we also know that:
    u_sn = (1-exp(-2*s_coef))/(1-exp(-4*N*s_coef))

    #we calculate ndm_alpha from above:

    ndm_alpha <- mu-r_syn/(mu*sdel_ss_ratio*2*N*u_sn)
    print(ndm_alpha)

    ## [1] -0.9000266

    #Exercise 8.7

    # we remember from page 157 that, for strongly advantageous alleles, u~=2s; so we apply formula (8.1)

    N <- 10^4
    s_coef <- 0.01
    mu <- 2.2*10^-9

    adv <- 8*10^-4
    r_sub_adv <- 4*N*s_coef*mu

    # we also know that r_tot = r_sub_adv + r_sub_neu, and r_sub_neu = 1-ndm_alpha-adv; from here we get ndm_alpha:
    #(adv*4*N*s_coef+1-ndm_alpha-adv)= (0.8*10^-9)/(2.2*10^-9)
    # we then obtain alpha:

    ndm_alpha <- (adv*4*N*s_coef+1-adv-(0.8*10^-9)/(2.2*10^-9))
    print(ndm_alpha)

    ## [1] 0.9555636

    #Exercise 8.8

    dlt <- 47/54
    c_dist <- 0.023
    f_B <- 0.086

    # from Box 8.5, formula B8.1:
    t <- log((dlt-f_B)/(1-f_B))/log(1-c_dist)
    print(t)

    ## [1] 6.573196

    #Exercise 8.9

    # we use LD mapping to estimate recombination distance between the CSF1R allele and DTD-causing locus using the formula B8.1 in Box 8.5; we are given:

    t <- 100
    f_B <- 0.03
    dlt <- 139/146

    log_dist <- log(dlt-f_B/1-f_B)/t
    #we then calculate the distance; log_dist is ln(1-c)

    dist = 1-exp(log_dist)
    print(dist)

    ## [1] 0.001141625

    # dist is expressed in centiMorgans; 1cM ~ 1mb; also, it looks about twice as large as in the textbook answer...

    #Exercise 8.10

    # no homozygotes at our locus; 10 alleles; 10 islands, each of population N/10

    # a. The effective migration rate is the probability that recombination will move the neutral locus on one genetic background (say S1) to any other genetic background (S2, . . . S10). Because there are no homozygotes, every copy of S1 is in a heterozygote, so every recombination event will move the neutral locus to another genetic background. Therefore, the effective migration rate is c, the recombination rate. 

    # b. for any given allele (e.g. S1) in a specific deme, the probability for another to be in the same deme is 0.1 and in another deme 0.9; from page 69, formula (4.17), and considering that for an island model M = 2Nm (so here: M = 2Nc/10), here we have: H_T = (1+(9/4Nc)) * theta/k

    # c. The number of alleles s_no is present in the numerator above (as 1-s_no = 9 in (1+(9/4Nc))). If s_no were to increase, Ht would also increase
