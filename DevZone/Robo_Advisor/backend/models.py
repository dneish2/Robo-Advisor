# backend/models.py

import pandas as pd
import os
import json  # Ensure json is imported

class UserProfile:
    def __init__(self, goals, risk_tolerance, available_investment):
        self.goals = goals
        self.risk_tolerance = risk_tolerance
        self.available_investment = available_investment
    
    def save_to_csv(self, filepath):
        df = pd.DataFrame([{
            'goals': json.dumps(self.goals),  # Proper JSON serialization
            'risk_tolerance': self.risk_tolerance,
            'available_investment': self.available_investment
        }])
        df.to_csv(filepath, mode='a', header=not os.path.exists(filepath), index=False)
    
    @staticmethod
    def load_from_csv(filepath):
        if os.path.exists(filepath):
            # Attempt to read with headers
            try:
                df = pd.read_csv(filepath)
                # Check if expected columns exist
                expected_columns = ['goals', 'risk_tolerance', 'available_investment']
                if all(col in df.columns for col in expected_columns):
                    return df
                else:
                    # If headers are missing or incorrect, read without headers and assign column names
                    df = pd.read_csv(filepath, header=None, names=['goals', 'risk_tolerance', 'available_investment'])
                    return df
            except pd.errors.ParserError:
                # In case of parsing error, read without headers
                df = pd.read_csv(filepath, header=None, names=['goals', 'risk_tolerance', 'available_investment'])
                return df
        else:
            return pd.DataFrame()