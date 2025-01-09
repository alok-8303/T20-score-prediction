
import gradio as gr
import pickle
import pandas as pd

# Load the trained model pipeline
with open("model.pkl", "rb") as file:
    pipe = pickle.load(file)

# Define the prediction function
def predict_score(batting_team, bowling_team, city, current_score, overs, wickets, last_five_overs_runs):
    # Create a dataframe for the input data
    input_df = pd.DataFrame(
        {
            "batting_team": [batting_team],
            "bowling_team": [bowling_team],
            "city": [city],
            "current_score": [current_score],
            "overs": [overs],
            "wickets": [wickets],
            "last_five_overs_runs": [last_five_overs_runs],
        }
    )
    # Make prediction
    result = pipe.predict(input_df)
    return result[0]

# Gradio interface
interface = gr.Interface(
    fn=predict_score,
    inputs=[
        gr.Dropdown(["Team1", "Team2", "Team3"], label="Batting Team"),
        gr.Dropdown(["TeamA", "TeamB", "TeamC"], label="Bowling Team"),
        gr.Textbox(label="City"),
        gr.Number(label="Current Score"),
        gr.Number(label="Overs"),
        gr.Number(label="Wickets"),
        gr.Number(label="Last Five Overs Runs"),
    ],
    outputs=gr.Number(label="Predicted Score"),
    title="T20 Cricket Score Predictor",
    description="Predict the final score of a T20 match based on match conditions.",
)

if __name__ == "__main__":
    interface.launch()
