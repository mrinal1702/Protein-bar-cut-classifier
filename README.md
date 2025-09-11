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


