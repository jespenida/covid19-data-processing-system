import pandas as pd

# Load the correlation matrix
correlation_matrix = pd.read_csv("focused_correlation_matrix.csv", index_col=0)

# Extract significant correlations (above 0.9)
significant_correlations = correlation_matrix[correlation_matrix > 0.9].stack().reset_index()
significant_correlations.columns = ["Country1", "Country2", "Correlation"]

# Remove self-correlations
significant_correlations = significant_correlations[
    significant_correlations["Country1"] != significant_correlations["Country2"]
]

# Remove duplicate pairs (A-B and B-A are the same)
significant_correlations = significant_correlations[
    significant_correlations[["Country1", "Country2"]].apply(frozenset, axis=1).duplicated(keep="first") == False
]

# Save to CSV
significant_correlations.to_csv("significant_correlations.csv", index=False)
print("Significant correlations saved to 'significant_correlations.csv'.")
