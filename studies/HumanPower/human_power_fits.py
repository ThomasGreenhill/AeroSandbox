import aerosandbox as asb
import aerosandbox.numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(font_scale=1)

datasets = [
    "Healthy_Men",
    "First-Class_Athletes",
    "World-Class_Athletes",
]

for dataset in datasets:
    # Ingest data
    data = np.genfromtxt(
        "data/" + dataset + ".csv",
        delimiter=","
    )
    data = data[data[:, 0].argsort()]
    durations = data[:, 0]  # in minutes
    powers = data[:, 1]  # in Watts


    def human_power_model(x, p):
        d = x["d"]
        logd = np.log10(d)

        return (
                p["a"] * d ** (
                p["b0"] + p["b1"] * logd + p["b2"] * logd ** 2
        )
        )  # essentially, a cubic in log-log space


    params = asb.FittedModel(
        model=human_power_model,
        x_data={"d": durations},
        y_data=powers,
        parameter_guesses={
            "a" : 408,
            "b0": -0.17,
            "b1": 0.08,
            "b2": -0.04,
        },
        put_residuals_in_logspace=True
    ).parameters

    # Plot fit
    fig, ax = plt.subplots(1, 1, figsize=(6.4, 4.8), dpi=200)
    plt.loglog(durations, powers, ".")
    durations = np.logspace(-2, 4)
    plt.loglog(durations, human_power_model({"d": durations}, params))
    plt.xlabel(r"Duration [mins]")
    plt.ylabel(r"Maximum Sustainable Power [W]")
    plt.title(f"Human Power Output ({dataset})\n(Fig. 2.4, Bicycling Science by D. Wilson)")
    plt.tight_layout()
    plt.show()
