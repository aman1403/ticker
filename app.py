import streamlit as st
import plotly.express as px
from services.stock_analysis_service import get_breakout_points
from utils.data_processing import DataProcessor

class BreakoutAnalysisApp:
    """
    A class-based implementation for the Breakout Points Analysis Streamlit app.
    """

    def __init__(self):
        """
        Initializes the app with any necessary configurations or state variables.
        """
        self.ticker = None

    def display_breakout_results(self, breakout_df):
        """
        Displays breakout points and related visualizations.

        Parameters:
            breakout_df (pd.DataFrame): DataFrame containing breakout points.
        """
        st.subheader(f"Breakout Points for {self.ticker}:")
        st.dataframe(breakout_df)

        # Scatter Plot: Returns After 20 Days
        st.subheader("Returns After 20 Days (Scatter Plot)")
        fig = px.scatter(
            breakout_df,
            x="Breakout Date",
            y="Return (%)",
            title="Returns After 20 Days",
            labels={"Breakout Date": "Date", "Return (%)": "Return (%)"},
            hover_data=["Breakout Day Close", "Price After 20 Days"],
        )
        st.plotly_chart(fig, use_container_width=True)

    def analyze_ticker(self):
        """
        Fetches and processes breakout points for the given ticker.

        Returns:
            pd.DataFrame: DataFrame containing breakout points.
        """

        # Call the service function to get breakouts
        breakouts = get_breakout_points(self.ticker)

        # Convert breakouts to DataFrame
        breakout_data = [breakout.to_dict() for breakout in breakouts]
        breakout_df = DataProcessor.format_breakout_data(breakout_data)

        return breakout_df
        

    def run(self):
        """
        Main entry point for the app, handling user input and displaying results.
        """
        st.title("Breakout Points Analysis")
        st.write("Analyze stock data for breakout points and visualize the results.")

        # Input for stock ticker
        self.ticker = st.text_input("Enter Stock Ticker (e.g., TSLA):")

        # Button to trigger analysis
        if st.button("Analyze"):
            if not self.ticker:
                st.error("Please enter a valid stock ticker.")
                return

            # Ensure the ticker is uppercase
            self.ticker = self.ticker.upper()

            try:
                # Analyze the ticker
                breakout_df = self.analyze_ticker()

                # Display results
                if breakout_df.empty:
                    st.write(f"No breakout points found for {self.ticker}.")
                else:
                    self.display_breakout_results(breakout_df)

            except ValueError as e:
                st.error(e)
            except Exception as e:
                st.error(f"Something went wrong while fetching breakout points for ticker {self.ticker}")


if __name__ == "__main__":
    app = BreakoutAnalysisApp()
    app.run()
