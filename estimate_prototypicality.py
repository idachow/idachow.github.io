import pandas as pd
import numpy as np
import scipy as sp
from scipy.stats import kstest
import nlp
import networks
from statsmodels.distributions.empirical_distribution import ECDF

def cdf_an_idea(idea_nw):
    """Given an idea represented as edge weights, return its empirical cdf
    """
    # draw from statsmodels ECDF
    return None

def ideas_to_cdf(idea_network):
    """Expect result of nlp.ideas_to_network(), i.e., a set of ideas represented as edge weights
    Return a set of cdfs for each idea
    """

def average_distribution(ideas_cdf):
    """Given a set of cdfs, compute an average cdf.
    This is for creating the baseline "prototypical" distribution.
    Per toubia, average at each edge weight value across all ideas.
    """
    return None

def idea_prototypicality(ideas_cdf, baseline_avg_cdf):
    """Given a set of cdfs (of ideas), compute a prototypicality score for each idea
    where prototypicality is defined as the Kolmogorov-Smirnov distance of the idea cdf from the average baseline cdf
    return a pandas data frame that has each idea id, idea content, and prototypicality score
    """
    ideas_p = []
    for idea in ideas_cdf.iterrows():
        ks = kstest(idea['cdf'], baseline_avg_cdf)[0]; # kstest returns tuple of KS statistic and p value
        ideas_p.append({'id': idea['id'], ''})
    return 

def main():
    return None

    # create the baseline cdf
        # call networks.ideas_to_network()
        # call ideas_to_cdf()
        # call average_distribution()

    # compute the idea cdfs
        # call networks.ideas_to_network()
        # call ideas_to_cdf()
        # for measure prototypicality for each idea