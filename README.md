## Project Goals:
    - Create documented files to clean and prepare Telco dataset for processing by a classification ML algorithm.
    - Use ML algorithms to create a model that best predicts customer churn on both in and out-of-sample data.
    - Extrapolate valuable analysis from the model that best fits the data.
    - Document processes, findings, and takeaways in a final draft Jupyter Notebook
    - Present on my final Jupyter Notebook, giving a high-level overview of the process used to create the model of best fit



## Data dictionary
Target  | Description   | Data Type
--|--|--
placeholder_target    | indicates if a customer has fiber, if their tenure is less than ___ and they have churned. Created from the original churn, tenure and internet_service_id columns | int64

Categorical Features   | Description |    Data Type
--|--|--
gender    |   indicates the the customers' gender identity |    int8
senior_citizen|    indicates if the customer is a senior citizen    |int64
partner|    indicates if the customer has a partner    |int64
dependents|        indicates if the customer has dependents    |int64
phone_service|    indicates if the customer has phone service with Telco    | int64
multiple_lines |    indicates if the customer with phone service has multiple lines    | int64
internet_service_type_id |    indicates which internet service (if any) the customer has |    int64
online_security|    indicates if the customer has online security services |    int 64
online_backup|    indicates if the customer has online backup services |    int64
device_protection    | indicates if the customer has device protection services |    int64
tech_support |  indicates if the customer has tech support services |    int64
streaming_tv |    indicates if the customer has tv streaming services |    int64
streaming_movies |    indicates if the customer has movie streaming services |    int64
payment_type    | indicates the type of payment method a customer is using | int64
contract_type_id |     indicates the type of contract the customer has with Telco |    int64
paperless_billing |     indicates if a customer has paperless billing |    int64
payment_type_id |     indicates the type of payment type the customer uses |    int64

Continuous Features | Description | Data Type
--|--|--
monthly_charges | how much a customer pays per month in dollars| float64
total_charges   | how much a customer has paid over the course of their tenure | float64
tenure          | how many months the customer has been with the company| int64

Engineered Features  | Description   | Data Type
--|--|--
auto_bill    | indicates if a customer has a form of automatic payment | int64
fbr_multi_line    | indicates if a customer fiber internet and multiple phone lines | int64


Other   | Description   | Data Type
--|--|--
churn   | indicates whether or not a customer churned | int64
customer_id | customer id number                       | object

## Hypotheses:
    - Month-to-month customers with fiber internet are more likely to churn than overall customers
    - Month-to-month customers monthly tenure is lower than average and significantly contributes to churn rate
        - at what point does tenure correlate to churn?



## Executive Summary:


## Plan:
- [x] Create repo on github to save all files related to the project.
- [] Create README.md with [x]goals, [x]initial hypotheses, [x]data dictionary, []executive summary, and [x]outline plans for the project.
- [x] Acqiure telco data using acquire.py file drawing directly from Codeups `telco_churn` database with SQL queries. Create functions for use in conjunction with prepare.py. Document each function.
- [x] Clean, tidy, and encode data in such a way that it is usable in a machine learning algorithm. Includes dropping unneccesary columns, creating dummies where needed and changing string values to numeric values. Document each function.
- [x] Create hypotheses based on preliminary statistical tests
- [x] Test hypotheses with tests such as t-test, chi-squared among others to determine the viability of said hypotheses by comparing p-values to alpha.
- [] Establish a baseline accuracy.
- [] Train three different classification models from kNN, random forrest, decision trees, and regression models, testing a variety of parameters and features, both engineered and pre-existing.
- [] Compute accuracy of models on in-sample and out-of-sample datasets using a variety of equations and functions.
- [] Once a single, best preforming model has been chosen, evaluate the preformance of the model on the test dataset.
- [] Create csv file with the .
- [] Document conclusions, takeaways, and next steps in the Final Report Notebook.
