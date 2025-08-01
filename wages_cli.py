#!/usr/bin/env python3
import sys
import matplotlib.pyplot as plt
from prompt_toolkit import prompt
from prompt_toolkit.completion import FuzzyWordCompleter
from prompt_toolkit.shortcuts import radiolist_dialog
from tabulate import tabulate
import pandas as pd
from data_loader import load_all_wage_data, get_unique_occupations, get_industries, filter_data

# Configure matplotlib for better display
plt.style.use('seaborn-v0_8-darkgrid')
plt.rcParams['figure.figsize'] = (10, 6)

def display_wage_data(data: pd.DataFrame, occupation: str, industry: str):
    """Display wage data in a formatted table."""
    print(f"\n{'='*80}")
    print(f"Occupation: {occupation}")
    print(f"Industry: {industry}")
    print(f"{'='*80}\n")
    
    if data.empty:
        print("No data found for this occupation and industry combination.")
        return
    
    # Prepare table data
    table_data = []
    for _, row in data.iterrows():
        table_row = [
            row['Year'],
            f"${row['Basic_P25']:,.0f}" if pd.notna(row['Basic_P25']) else 'N/A',
            f"${row['Basic_Median']:,.0f}" if pd.notna(row['Basic_Median']) else 'N/A',
            f"${row['Basic_P75']:,.0f}" if pd.notna(row['Basic_P75']) else 'N/A',
            f"${row['Gross_P25']:,.0f}" if pd.notna(row['Gross_P25']) else 'N/A',
            f"${row['Gross_Median']:,.0f}" if pd.notna(row['Gross_Median']) else 'N/A',
            f"${row['Gross_P75']:,.0f}" if pd.notna(row['Gross_P75']) else 'N/A'
        ]
        table_data.append(table_row)
    
    headers = ['Year', 'Basic P25', 'Basic Median', 'Basic P75', 
               'Gross P25', 'Gross Median', 'Gross P75']
    
    print(tabulate(table_data, headers=headers, tablefmt='grid'))

def plot_wage_trends(data: pd.DataFrame, occupation: str, industry: str):
    """Plot wage trends over years."""
    if data.empty or len(data) < 2:
        print("\nInsufficient data for plotting (need at least 2 years).")
        return
    
    # Create figure with subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Plot Basic Wages
    years = data['Year'].values
    
    # Basic wages
    if data['Basic_Median'].notna().any():
        ax1.plot(years, data['Basic_Median'], 'b-o', label='Median', linewidth=2, markersize=8)
    if data['Basic_P25'].notna().any():
        ax1.plot(years, data['Basic_P25'], 'g--o', label='25th Percentile', linewidth=1.5, markersize=6)
    if data['Basic_P75'].notna().any():
        ax1.plot(years, data['Basic_P75'], 'r--o', label='75th Percentile', linewidth=1.5, markersize=6)
    
    ax1.set_xlabel('Year', fontsize=12)
    ax1.set_ylabel('Basic Wage ($)', fontsize=12)
    ax1.set_title('Basic Wage Trends', fontsize=14, fontweight='bold')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Format y-axis as currency
    ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x:,.0f}'))
    
    # Gross wages
    if data['Gross_Median'].notna().any():
        ax2.plot(years, data['Gross_Median'], 'b-o', label='Median', linewidth=2, markersize=8)
    if data['Gross_P25'].notna().any():
        ax2.plot(years, data['Gross_P25'], 'g--o', label='25th Percentile', linewidth=1.5, markersize=6)
    if data['Gross_P75'].notna().any():
        ax2.plot(years, data['Gross_P75'], 'r--o', label='75th Percentile', linewidth=1.5, markersize=6)
    
    ax2.set_xlabel('Year', fontsize=12)
    ax2.set_ylabel('Gross Wage ($)', fontsize=12)
    ax2.set_title('Gross Wage Trends', fontsize=14, fontweight='bold')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    # Format y-axis as currency
    ax2.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x:,.0f}'))
    
    # Set x-axis to show only integer years
    for ax in [ax1, ax2]:
        ax.set_xticks(years)
        ax.set_xticklabels(years)
    
    # Main title
    fig.suptitle(f'{occupation} - {industry}', fontsize=16, fontweight='bold')
    
    plt.tight_layout()
    plt.show()

def select_occupation(occupations: list) -> str:
    """Interactive occupation selection with fuzzy search."""
    print("\nSearch for an occupation (type to search):")
    
    # Create fuzzy completer
    completer = FuzzyWordCompleter(occupations, match_middle=True)
    
    while True:
        try:
            selected = prompt('Occupation: ', completer=completer)
            
            # Find exact match (case-insensitive)
            matches = [occ for occ in occupations if occ.lower() == selected.lower()]
            
            if matches:
                return matches[0]
            else:
                # Find partial matches
                partial_matches = [occ for occ in occupations if selected.lower() in occ.lower()]
                
                if len(partial_matches) == 0:
                    print(f"No occupation found matching '{selected}'. Please try again.")
                elif len(partial_matches) == 1:
                    confirm = input(f"Did you mean '{partial_matches[0]}'? (y/n): ")
                    if confirm.lower() == 'y':
                        return partial_matches[0]
                else:
                    print(f"\nMultiple matches found for '{selected}':")
                    for i, match in enumerate(partial_matches[:10], 1):
                        print(f"{i}. {match}")
                    if len(partial_matches) > 10:
                        print(f"... and {len(partial_matches) - 10} more")
                    print("\nPlease be more specific.")
                    
        except (EOFError, KeyboardInterrupt):
            print("\nCancelled.")
            return None

def select_industry(industries: list) -> str:
    """Interactive industry selection using radio list."""
    print("\nSelect an industry:")
    
    # Create choices for radiolist
    choices = [(industry, industry) for industry in industries]
    
    try:
        result = radiolist_dialog(
            title="Industry Selection",
            text="Use arrow keys to navigate, Enter to select:",
            values=choices
        ).run()
        
        return result
    except (EOFError, KeyboardInterrupt):
        print("\nCancelled.")
        return None

def main():
    """Main CLI application."""
    print("Loading wage data...")
    
    # Load all data
    try:
        df = load_all_wage_data()
    except Exception as e:
        print(f"Error loading data: {e}")
        print("Please ensure the Excel files are in the current directory.")
        sys.exit(1)
    
    if df.empty:
        print("No data found. Please ensure Excel files are in the current directory.")
        sys.exit(1)
    
    print(f"Loaded {len(df)} records from {df['Year'].nunique()} years")
    
    # Get unique occupations and industries
    occupations = get_unique_occupations(df)
    industries = get_industries()
    
    print(f"Found {len(occupations)} unique occupations across {len(industries)} industries")
    
    # Main loop
    while True:
        print("\n" + "="*80)
        print("WAGE ANALYSIS TOOL")
        print("="*80)
        
        # Select occupation
        occupation = select_occupation(occupations)
        if not occupation:
            break
        
        # Select industry
        industry = select_industry(industries)
        if not industry:
            break
        
        # Filter and display data
        filtered_data = filter_data(df, occupation, industry)
        
        # Display table
        display_wage_data(filtered_data, occupation, industry)
        
        # Plot trends if data available
        if not filtered_data.empty and len(filtered_data) >= 2:
            plot_choice = input("\nWould you like to see the trend chart? (y/n): ")
            if plot_choice.lower() == 'y':
                plot_wage_trends(filtered_data, occupation, industry)
        
        # Ask if user wants to continue
        continue_choice = input("\nWould you like to search for another occupation? (y/n): ")
        if continue_choice.lower() != 'y':
            break
    
    print("\nThank you for using the Wage Analysis Tool!")

if __name__ == "__main__":
    main()