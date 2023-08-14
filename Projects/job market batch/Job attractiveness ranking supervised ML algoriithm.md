Input : jobs with features
Output : jobs with features + scores

### Standard parameters

| Criteria          | Columns containing the info | Points |
| ----------------- | --------------------------- | ------ |
| remote total      | remote                      | 3      |
| remote partiel 3h | remote + location           | 1      |
| junior            | title / text / experience   | 3      |
| interesting       | text                        | 3      |
| Python, SQL, ETL  | stack                       | 3      |
| keywords          | text                        | 3      |
| education         | education / text            | 2      |
| english           |                             | 2       |

# Classification model pipeline

## 1. Create Dataset

- Define your collection of documents or items as a matrix, where each row represents a document or item, and each column represents a feature or attribute.
	- Read 'relevant' into a dataframe
	- Extract features into columns in numerical form
		- remote : 0 1 2 na
		- junior : 1 0
	- Keep job id + numerical features 
- Define the weights for each feature
- Multiple the matrix by the weight vector
- Calculate similarity scores

## 2. Exploratory Data Analysis

- Histogram
- Grouped bar chart
- Box plot

## 3. Split Dataset into Training and Testing Sets

