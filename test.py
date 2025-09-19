from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd


model = LinearRegression()


data = pd.read_csv('synthetic_coffee_health_10000.csv')




from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel

