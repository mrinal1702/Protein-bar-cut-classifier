# What Are the Best Protein Bars Available in Ireland?

This project is designed for **consumers aiming to cut** and **trainers looking to guide their clients** on better nutrition choices.  
Protein bars are often marketed with flashy claims — “high protein,” “low sugar,” “healthy fuel” — but not all are truly cutting-friendly.  

Using open-source nutrition data and a structured scoring framework, this project applies **data analysis and machine learning** to cut through the clutter and identify which bars actually support fat loss goals.

---

## Project Goal

The goal of this project is two-fold:

1. **Consumer clarity**  
   Help individuals focused on fat loss make informed choices by ranking protein bars sold in Ireland on their true cutting-friendliness.  

2. **Trainer guidance**  
   Provide a simple, explainable framework that gym trainers and nutrition coaches can use when recommending bars — grounded in both nutritional science and machine learning validation.  

---

## Cleaning Up the Protein Bar Aisle  

The raw dataset came from [OpenFoodFacts](https://world.openfoodfacts.org/), an open-source nutrition database. I focused on **protein bars available in Ireland**, which gave me around **310 products** to analyze.  

Like all crowd-sourced data, OpenFoodFacts comes with its own caveats — incomplete nutrition labels, missing values, and the occasional bizarre entry (one bar claimed 15,000 kcal per 100g). To make the data usable, I applied some basic cleaning rules:  

- **Dropped rows with missing or zero calories** (these rows are clearly unusable).  
- **Dropped rows with missing or zero protein values** (since protein is central to this study).  
- **Filled blanks in other nutrient fields** (sugar, fiber, fats) with zeros).  
- **Removed obvious rogue outliers** (e.g., a bar with 5 kcal and 40g protein per 100g — clearly a mislabel).  

Finally, I introduced a key feature:  

- **Protein per 100 kcal (“protein density”)** → this tells us how much protein you get for every 100 calories consumed. A lean, cutting-friendly bar should score high here.  

---

### Interactive Chart — Calories vs Protein Density

Here, I started with only factoring calories in the bar and protein density. I plot all the 309 bars on this interactive chart, to divide them into the 4 quadrants you see below.

[▶️ **Open the interactive Plotly chart**](https://mrinal1702.github.io/Protein-bar-cut-classifier/irish_protein_bars_scatter.html)

<a href="https://mrinal1702.github.io/Protein-bar-cut-classifier/irish_protein_bars_scatter.html">
  <img src="assets/irish_protein_bars_scatter.png" alt="Protein Bars: Calories vs Protein Density (interactive link)" />
</a>

This gives us an idea of which bars are better for cutting, which are better for bulking, which are light on both calories and protein and which are relatively "junk" bars - high on calories and low on protein.

---

## How the “Top 5” Lists Were Derived

To find the strongest candidates for **cutting-friendly** and **bulking-oriented** bars, I used a simple **distance-from-origin** method based on the scatter plot axes:

- I defined the axes center as the **median value** of calorie-per-100g (x) and protein-per-100-kcal (y).
- For each bar, I calculated its Euclidean distance from that center point.
- Bars in the **top-left quadrant** (low calories, high protein density) that were furthest from the center appear in the **Top 5 Cutting** list.
- Bars in the **top-right quadrant** (high calories, high protein density) that were furthest appear in the **Top 5 Bulking** list.
- Bars in the **bottom-right quadrant** (high calories, low protein) that were furthest appear in the **Bottom 5 Worst** list (not shown here for brevity).

---

### Top 5 Cutting-Friendly Protein Bars

These are the five bars that combine **very low calories** and **high protein density**, making them stand out as excellent choices for cutting:

| Rank | Bar Name | Brand | Link |
|------|----------|-------|------|
| 1 | Protein bar | Linea | [Linea official site](https://www.linea.ie) |
| 2 | Milk Chocolate Crunch Protein Bar | Fulfil | [FULFIL Nutrition](https://www.livefulfil.com) |
| 3 | Proteín bar | Ritter | [Ritter Sport](https://www.ritter-sport.com/en) |
| 4 | Simply Protein Crispy Bar | SimplyProtein | [SimplyProtein Crispy Bars](https://simplyprotein.com/collections/snack-bars) |
| 5 | Dark Chocolate Sea Salt Protein Bar | SimplyProtein | [SimplyProtein Crispy Bars](https://simplyprotein.com/collections/snack-bars) |

---

### Top 5 Bulking-Oriented Protein Bars

These bars pack both **high calories** and **high protein density**, making them suitable for users looking to gain or maintain bulk while still getting strong protein value:

| Rank | Bar Name | Brand | Link |
|------|----------|-------|------|
| 1 | 43% Protein Bar | — | [OpenFoodFacts entry](https://ie.openfoodfacts.org/product/5214002412364/43-protein-bar) (no detailed info available) |
| 2 | Premium Protein Bar | Sports Factory | [OpenFoodFacts entry](https://ie-ga.openfoodfacts.org/product/2200256157468/premium-protien-bar-sports-factory) |
| 3 | Pretty Pistachio Protein Bar | Personal Protein | [OpenFoodFacts entry](https://world.openfoodfacts.org/product/2493229327405/pretty-pistachio-protein-bar-personal-protein) (limited info available) |
| 4 | Peanut & Chia Protein Bar | Nutrim | [OpenFoodFacts entry](https://ie.openfoodfacts.org/product/9860062801745/peanut-chia-protein-bar-nutrim) |
| 5 | Chocolate Peanut Butter Protein Bar | Pure Protein | [PureProtein official site](https://www.pureprotein.com/products/chocolate-peanut-butter-protein-bar) |

---

> ℹ Bottom 5 “Worst” bars (high calories, low protein density) are also computed but not shown here. They may indicate bars to avoid when cutting.

---

## Beyond Protein and Calories  

Protein and calories are crucial metrics — but they don’t tell the whole story.  
To get a more **holistic view of health**, we expanded the analysis to include:  

- **Fiber** → promotes satiety with minimal calories, supports gut health.  
- **Sugar** → adds empty calories, spikes insulin, and encourages cravings.  
- **Saturated Fat** → linked to higher LDL cholesterol and cardiovascular risk.  

Of course, health has many different dimensions — micronutrients, processing level, ingredient quality — and encompassing *all* of them would be overly complex (if not impossible) in a single study. This analysis narrows its focus to the most impactful and widely-available macronutrient measures.

---

## Building the Cutting Score  

Since the aim of this project is to evaluate **cutting-friendly protein bars**, we placed all the chosen nutrients onto a **comparable scale** by computing **z-scores** (standardized scores relative to the dataset).  

We then applied **weights** to reflect their relative importance for cutting:

- **Calories** → 50% (lower is better)  
- **Protein density** → 35% (higher is better)  
- **Sugar** → 6% (lower is better)  
- **Fiber** → 6% (higher is better)  
- **Saturated fat** → 3% (lower is better)  

These weights are based on a mix of nutritional science and practical intuition. Importantly, the code is fully flexible:  
if a nutrition expert or coach believes the weights should differ, they can simply adjust the values and rerun the model — the Cutting Score will update automatically.  

The end result is a **single “Cutting Score” (0–100)** for each bar, allowing us to directly rank products on how supportive they are for fat loss goals.  

The code output prints the top 10 bars based on cutting score.

### Top 10 Bars by Cutting Score  

Below are the ten highest-ranked protein bars according to the Cutting Score (0–100), with links to official brand pages or OpenFoodFacts entries where available. I have to caveat this score by saying that all information was not available for every bar, and hence the score might not be completely accurate. Openfoodfacts is an open source database, so information is not necessarily complete or up-to-date.

| Rank | Bar Name                                            | Brand           | Cutting Score | Link                                                                 |
|------|-----------------------------------------------------|-----------------|---------------|----------------------------------------------------------------------|
| 1    | Twenty’s Protein Bar – Chocolate Brownie            | Your Goal       | 92.9          | [Your Goal – Twenty’s Chocolate Brownie](https://yourgoal.cl/?srsltid=AfmBOorh6PYS6fTi0tiX2MeC-lmrVSWW-v0cruoT47C0Dbb-XefgJx4l) |
| 2    | Quest Protein Bar                                   | Quest           | 89.0          | [OpenFoodFacts entry](https://world.openfoodfacts.org/product/0866496004621/quest-protein-bar) |
| 3    | Sour Watermelon Cold Pressed Protein Bar – Fibre Boost | Fibre Boost   | 89.0          | [Fibre Boost](https://fibre-boost.com/) |
| 4    | No Cow Protein Bar                                  | No Cow          | 88.7          | [No Cow Official Site](https://nocow.com/) |
| 5    | Quest Protein Bar                                   | Quest           | 88.0          | [OpenFoodFacts entry](https://world.openfoodfacts.org/product/0712649000005/quest-protein-bar) |
| 6    | Protein Bar                                         | Linea           | 87.5          | [Linea Official Site](https://www.linea.ie) |
| 7    | Chocolate Chip Cookie Dough Protein Bar             | Quest           | 87.3          | [Quest – Cookie Dough Bar](https://www.questnutrition.com/products/chocolate-chip-cookie-dough-protein-bar) |
| 8    | Quest Protein Bar                                   | Quest           | 86.4          | [OpenFoodFacts entry](https://world.openfoodfacts.org/product/0882649011285/quest-quest-protein-bar) |
| 9    | Dark Chocolate Sea Salt Protein Bar                 | SimplyProtein   | 86.0          | [SimplyProtein Bars](https://simplyprotein.com/collections/snack-bars) |
| 10   | Chocolate Deluxe Protein Bar                        | Pure Protein    | 85.8          | [Pure Protein Chocolate Deluxe](https://www.pureprotein.com/products/chocolate-deluxe-protein-bar) |

---

## Training a Machine Learning Classifier  

Since the nutrition data is not always complete, we trained a **machine learning model** to learn the relationships between nutrients and whether a bar is “cutting friendly.”  

The idea:  
- **Input:** nutrition facts of any protein bar (calories, protein density, fiber, sugar, saturated fat).  
- **Output:** classification → *cutting friendly ✅* or *not cutting friendly ❌*.  

This way, the model can be applied not just to the 310 Irish bars in the dataset, but also to **any new bar in the world**, even those released in the future.

---

### Labeling the Data  

To train the model, we first needed to **label each bar** as cutting-friendly or not.  
We did this using the **Cutting Score**:  
- Any bar with a score **≥ 60** was labeled cutting-friendly.  
- Any bar below 60 was labeled not cutting-friendly.  

This cutoff gave us roughly **30% cutting-friendly bars**, a balanced-enough dataset for training.  
The threshold is adjustable: if you want a stricter model, you can raise the cutoff.

---

### Model Training  

We used **Stratified K-Fold Cross Validation**, which works like this:  
- The dataset is split into 5 “folds.”  
- In each round, 4 folds are used to train, 1 fold is used to test.  
- This repeats 5 times, so every bar gets tested once.  
- Results are averaged → more reliable than a single train/test split.  

---

### Results  

The model achieved:  

- **F1 score ≈ 0.92** → the model is very good at correctly identifying cutting-friendly bars (balance of precision and recall).  
- **ROC-AUC ≈ 0.99** → almost perfect ability to rank cutting-friendly bars above non-friendly ones.  

Since the F1 score is high, we can be confident moving forward with this model.  

---

### Feature Coefficients  

We trained a **logistic regression model**, which gives us coefficients for each nutrient.  
These show both the **importance** and the **direction** of each factor:

| Feature              | Coefficient | Interpretation |
|-----------------------|-------------|----------------|
| Calories (per 100g)   | -3.99       | Higher calories strongly reduce the chance of being cutting-friendly. |
| Protein density       | +2.36       | Higher protein-per-100 kcal strongly increases cutting-friendliness. |
| Fiber                 | +0.86       | More fiber helps (makes bars slightly more cutting-friendly). |
| Sugar                 | -0.64       | More sugar reduces cutting-friendliness. |
| Saturated fat         | -0.16       | Slight negative effect, but weaker compared to calories or protein. |

**Key takeaway:** Calories are the strongest negative predictor, while protein density is the strongest positive predictor — exactly what you’d expect for fat loss goals.  


