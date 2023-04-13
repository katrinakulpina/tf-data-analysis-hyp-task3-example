import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

chat_id = 324047628 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    alpha = 0.07
    pval = mannwhitneyu(x, y, alternative='less').pvalue
    return pval < alpha
