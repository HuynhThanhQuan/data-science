"""
MMM Helper Functions

This module contains utility functions for Media Mix Modeling analysis.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from typing import Dict, List, Tuple, Optional

def adstock_transformation(x: np.ndarray, decay_rate: float = 0.5, max_lag: int = 8) -> np.ndarray:
    """
    Apply adstock transformation to a media channel.
    
    Parameters:
    -----------
    x : array-like
        Media spend values
    decay_rate : float, default 0.5
        Rate at which effect decays (0-1)
    max_lag : int, default 8
        Maximum number of periods for carryover
        
    Returns:
    --------
    numpy.ndarray
        Adstocked values
    """
    adstocked = np.zeros_like(x, dtype=float)
    
    for i in range(len(x)):
        for j in range(max_lag + 1):
            if i - j >= 0:
                adstocked[i] += x[i - j] * (decay_rate ** j)
    
    return adstocked

def hill_saturation(x: np.ndarray, half_saturation: float = 1.0, shape: float = 1.0) -> np.ndarray:
    """
    Hill saturation curve (S-curve transformation).
    
    Parameters:
    -----------
    x : array-like
        Input values (e.g., adstocked spend)
    half_saturation : float, default 1.0
        Point at which curve reaches 50% of maximum
    shape : float, default 1.0
        Controls the steepness of the curve
        
    Returns:
    --------
    numpy.ndarray
        Saturated values
    """
    return x ** shape / (half_saturation ** shape + x ** shape)

def diminishing_returns(x: np.ndarray, alpha: float = 0.5) -> np.ndarray:
    """
    Simple diminishing returns transformation.
    
    Parameters:
    -----------
    x : array-like
        Input values
    alpha : float, default 0.5
        Saturation parameter (0-1)
        
    Returns:
    --------
    numpy.ndarray
        Transformed values with diminishing returns
    """
    return x ** alpha

def calculate_roas(conversions: np.ndarray, spend: np.ndarray, conversion_value: float = 1.0) -> float:
    """
    Calculate Return on Ad Spend (ROAS).
    
    Parameters:
    -----------
    conversions : array-like
        Number of conversions
    spend : array-like
        Marketing spend
    conversion_value : float, default 1.0
        Value per conversion
        
    Returns:
    --------
    float
        ROAS value
    """
    total_revenue = np.sum(conversions) * conversion_value
    total_spend = np.sum(spend)
    
    if total_spend == 0:
        return 0
    
    return total_revenue / total_spend

def calculate_contribution_share(contributions: Dict[str, float]) -> Dict[str, float]:
    """
    Calculate percentage contribution share for each channel.
    
    Parameters:
    -----------
    contributions : dict
        Dictionary of channel contributions
        
    Returns:
    --------
    dict
        Dictionary of percentage shares
    """
    total = sum(contributions.values())
    if total == 0:
        return {k: 0 for k in contributions.keys()}
    
    return {k: (v / total) * 100 for k, v in contributions.items()}

def create_synthetic_mmm_data(n_periods: int = 104, 
                             channels: Optional[List[str]] = None,
                             start_date: str = '2022-01-01') -> pd.DataFrame:
    """
    Create synthetic MMM dataset for testing and learning.
    
    Parameters:
    -----------
    n_periods : int, default 104
        Number of time periods (weeks)
    channels : list, optional
        List of media channel names
    start_date : str, default '2022-01-01'
        Start date for the dataset
        
    Returns:
    --------
    pandas.DataFrame
        Synthetic MMM dataset
    """
    if channels is None:
        channels = ['tv_spend', 'digital_spend', 'radio_spend', 'print_spend']
    
    np.random.seed(42)
    dates = pd.date_range(start=start_date, periods=n_periods, freq='W')
    
    # Base trend and seasonality
    trend = np.linspace(1, 1.5, n_periods)
    week_of_year = pd.Series(dates).dt.isocalendar().week
    seasonality = 1 + 0.3 * np.sin(2 * np.pi * week_of_year / 52)
    
    data = {'date': dates}
    
    # Generate spend data for each channel
    spend_params = {
        'tv_spend': {'base': 8000, 'noise': 1000},
        'digital_spend': {'base': 5000, 'noise': 800},
        'radio_spend': {'base': 3000, 'noise': 500},
        'print_spend': {'base': 2000, 'noise': 400}
    }
    
    for channel in channels:
        if channel in spend_params:
            params = spend_params[channel]
            base_spend = params['base'] * trend * seasonality
            noise = np.random.normal(0, params['noise'], n_periods)
            data[channel] = np.maximum(base_spend + noise, 0)
        else:
            # Default for custom channels
            base_spend = 4000 * trend * seasonality
            noise = np.random.normal(0, 600, n_periods)
            data[channel] = np.maximum(base_spend + noise, 0)
    
    # Generate conversions based on spend with realistic MMM effects
    base_conversions = 1000 * trend
    media_effects = np.zeros(n_periods)
    
    for channel in channels:
        spend = data[channel]
        # Apply adstock and saturation
        adstocked = adstock_transformation(spend, decay_rate=0.6)
        saturated = diminishing_returns(adstocked, alpha=0.7)
        media_effects += saturated * 0.1  # Channel coefficient
    
    conversions = base_conversions + media_effects * seasonality
    conversions += np.random.normal(0, 100, n_periods)  # Noise
    data['conversions'] = np.maximum(conversions, 0)
    
    return pd.DataFrame(data)

def plot_channel_performance(data: pd.DataFrame, 
                           channels: List[str],
                           target: str = 'conversions') -> None:
    """
    Plot channel spend vs target variable performance.
    
    Parameters:
    -----------
    data : pandas.DataFrame
        Dataset containing channels and target
    channels : list
        List of channel column names
    target : str, default 'conversions'
        Target variable column name
    """
    n_channels = len(channels)
    n_cols = min(2, n_channels)
    n_rows = (n_channels + n_cols - 1) // n_cols
    
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(12, 4 * n_rows))
    if n_channels == 1:
        axes = [axes]
    elif n_rows == 1:
        axes = axes.flatten()
    else:
        axes = axes.flatten()
    
    for i, channel in enumerate(channels):
        if i < len(axes):
            axes[i].scatter(data[channel], data[target], alpha=0.6)
            axes[i].set_xlabel(f'{channel} Spend')
            axes[i].set_ylabel(target.title())
            axes[i].set_title(f'{channel.replace("_", " ").title()} vs {target.title()}')
    
    # Hide extra subplots
    for i in range(len(channels), len(axes)):
        axes[i].set_visible(False)
    
    plt.tight_layout()
    plt.show()

def validate_mmm_data(data: pd.DataFrame, 
                     channels: List[str],
                     target: str = 'conversions') -> Dict[str, str]:
    """
    Validate MMM dataset for common issues.
    
    Parameters:
    -----------
    data : pandas.DataFrame
        Dataset to validate
    channels : list
        List of channel column names
    target : str, default 'conversions'
        Target variable column name
        
    Returns:
    --------
    dict
        Dictionary of validation results
    """
    results = {}
    
    # Check for missing columns
    missing_cols = [col for col in channels + [target] if col not in data.columns]
    if missing_cols:
        results['missing_columns'] = f"Missing columns: {missing_cols}"
    else:
        results['missing_columns'] = "All required columns present"
    
    # Check for missing values
    missing_values = data[channels + [target]].isnull().sum().sum()
    results['missing_values'] = f"Missing values: {missing_values}"
    
    # Check for negative values
    negative_values = (data[channels + [target]] < 0).sum().sum()
    results['negative_values'] = f"Negative values: {negative_values}"
    
    # Check data range
    date_range = None
    if 'date' in data.columns:
        date_range = f"{data['date'].min()} to {data['date'].max()}"
    results['date_range'] = date_range or "No date column found"
    
    # Check for outliers (values > 3 std devs)
    outliers = {}
    for col in channels + [target]:
        if col in data.columns:
            mean_val = data[col].mean()
            std_val = data[col].std()
            outlier_count = ((data[col] - mean_val).abs() > 3 * std_val).sum()
            outliers[col] = outlier_count
    results['outliers'] = outliers
    
    return results