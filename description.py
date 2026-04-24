import pandas as pd
from matplotlib import pyplot as plt

class Container:
    def __init__(self, path: str):
        # Construct the data frame
        self.df = pd.read_csv(path)
    
    def get_stats(self):
        """
        return a summary of the statistics for two grpups (AAA vs Indie)
        """
        return self.df.groupby('is_aaa')['review_score'].agg(
                ['mean', 'std', 'count', 'median']
                )

    def plot_comparision(self):
        """
        Plots comparsion between AAA vs Indie Games
        """
        _, (ax1, ax2) = plt.subplots(1, 2, figsize=(15,6))

        # Distribution Plot

        # Filter into two series for density plots
        aaa = self.df[self.df['is_aaa'] == True]["review_score"]
        indie = self.df[self.df['is_aaa'] == False]["review_score"]

        aaa.plot(kind='kde', ax = ax1, label = 'AAA Games', color='blue', lw=2)
        indie.plot(kind='kde', ax = ax1, label = 'Indie Games', color = 'red', lw=2)

        ax1.set_title("Density of Review Scores", fontsize=14)
        ax1.set_xlabel("Review Score (%)")
        ax1.set_xlim(0, 100)
        ax1.legend()
        ax1.grid(alpha=0.3)

        # Box Plot
        self.df.boxplot(column='review_score', by='is_aaa', ax=ax2, patch_artist=True, grid=False)
        ax2.set_title("Score Variance & Medians", fontsize=14)
        ax2.set_xticklabels(["Indie", "AAA"])
        ax2.set_xlabel("Game Type (AAA or Indie)")
        ax2.set_ylabel("Score (%)")

        plt.suptitle("AAA vs Indie: User Satisfaction Analysis", fontsize=18)
        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        plt.show()
        
def run_analysis(data_path: str):
    container = Container(data_path)
    # Print stats to stdout
    print("\nSummary Of Statistics\n")
    stats = container.get_stats();
    print(stats)

    # Visualizations
    print("\nGenerating Visualizations\n")
    container.plot_comparision()

if __name__ == "__main__":
    print("----Constructing Description of Given Data-Set----")
    data_path = str(input("Path of the data-set: "))
    run_analysis(data_path)
