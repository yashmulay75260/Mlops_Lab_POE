import pandas as pd
from sklearn.datasets import load_iris
from evidently import Report
from evidently.presets import DataDriftPreset


def main():
    iris = load_iris(as_frame=True)
    data = iris.frame

    # Split the data into reference and current datasets
    reference_data = data.iloc[:75].copy()
    current_data = data.iloc[75:].copy()

    # Generate the data drift report
    report = Report([
        DataDriftPreset()
    ])

    result = report.run(
        current_data,
        reference_data
    )

    result.save_html("evidently_report.html")

    print("Evidently monitoring completed.")
    print("Report saved as evidently_report.html")


if __name__ == "__main__":
    main()
