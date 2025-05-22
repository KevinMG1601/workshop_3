# ***Workshop 3: Machine learning and Data streaming 💻***

## **OVERVIEW**
This project aims to train a regression model to predict the happiness score of different countries using historical data distributed in five CSV files (2015.csv, 2016.csv, 2017.csv, 2018.csv, 2019.csv). The process involves scanning, cleaning, and unifying the data to build a robust model, followed by implementing real-time streaming using Apache Kafka to predict scores as new data is received. Finally, the results are stored in a database for further analysis and evaluation.

## **OBJETIVES**
* Conduct exploratory data analysis (EDA).
* Unify historical global happiness data (2015-2019).
* Train a regression model to predict happiness score.
* Implement a data flow with Kafka (producer → consumer).
* Store predictions and features in a relational database.

## **PROJECT STRUCTURE**
| Folder / File | Description |
| ------------- |:-------------:|
| Assets/       | folder to store graphic or multimedia resources used in the project.|
| Data/         | It contains all the data used in the project.|
|├── output/    | Processed files or final results, such as the happiness_merged.csv dataset.|
|├── raw/       | Store the original CSV files for the different years (2015-2019).|
| Docs/         | Additional project documents.|
| Kafka/        | contains the scripts for the streaming process with kafka.|
|├── consumer.py | Script that consumes messages from the happiness_merged topic and makes predictions using the trained model.|
|├── producer.py | Script that produces messages by sending the transformed CSV data to the Kafka topic.|
| Model/        | Folder where the trained regression model is stored (.pkl).|
| Notebooks/    | Jupyter notebooks with the analysis and development of the model.|
|├── 01_eda.ipynb       | Exploratory Data Analysis (EDA) Notebook.|
|├── 02_training.ipynb  | Training and validation of the regression model.|
|├── 03_model.ipynb     | Prediction, evaluation and final testing of the model with test data.|
| Utils/                    | Reusable auxiliary functions for the entire project.|
|├── connection_db.py       | Funciones para conectar y crear tablas en la base de datos MySQL .|
|├── eda_functions.py       | Customized functions for exploratory data analysis.|
|├── training_functions.py  | Support functions for model training.|
| .env.example       | Example file with environment variables.|
| .gitattributes     | Configuration file for Git, useful for version control and text normalization.|
| .gitignore         | List of files or folders to be ignored by Git.|
| docker-compose.yml | Define and run Docker services such as Kafka, Zookeeper and the database.|
| Pyproject.toml     | Python environment configuration file and dependencies (using Poetry).|
| README.md          | Main document with instructions, objectives and details of the project.|


## **DATASETS**
The project uses multiple CSV files with worldwide happiness data extracted from annual reports from different years. The columns of each CSV are shown below:
| **2015**                      | **2016**                      | **2017**                      | **2018**                     | **2019**                     |
|-------------------------------|-------------------------------|-------------------------------|------------------------------|------------------------------|
| Country                       | Country                       | Country                       | Overall rank                 | Overall rank                 |
| Region                        | Region                        | Happiness.Rank                | Country or region            | Country or region            |
| Happiness Rank                | Happiness Rank                | Happiness.Score               | Score                        | Score                        |
| Happiness Score               | Happiness Score               | Whisker.high                  | GDP per capita               | GDP per capita               |
| Standard Error                | Lower Confidence Interval     | Whisker.low                   | Social support               | Social support               |
| Economy (GDP per Capita)      | Upper Confidence Interval     | Economy..GDP.per.Capita.      | Healthy life expectancy      | Healthy life expectancy      |
| Family                        | Economy (GDP per Capita)      | Family                        | Freedom to make life choices | Freedom to make life choices |
| Health (Life Expectancy)      | Family                        | Health..Life.Expectancy.      | Generosity                   | Generosity                   |
| Freedom                       | Health (Life Expectancy)      | Freedom                       | Perceptions of corruption    | Perceptions of corruption    |
| Trust (Government Corruption) | Freedom                       | Generosity                    |                              |                              |
| Generosity                    | Trust (Government Corruption) | Trust..Government.Corruption. |                              |                              |
| Dystopia Residual             | Generosity                    | Dystopia.Residual             |                              |                              |
|                               | Dystopia Residual             |                               |                              |                              |


## **TECHNOLOGIES USED**
* [Python 3.11.9](https://www.python.org/downloads/release/python-3119/)
* [Jupyter Notebook](https://docs.jupyter.org/en/latest/)
* [Scikit-learn](https://scikit-learn.org/0.21/install.html)
* [Kafka](https://kafka.apache.org/documentation/)
* [Docker](https://docs.docker.com/)
* [MySQL](https://dev.mysql.com/downloads/installer/)
* [Poetry](https://python-poetry.org/docs/)


## **INSTALLATION AND SETUP**

### **1. Clone the repository:**
```
git clone https://github.com/KevinMG1601/workshop_3.git
```
### **2. Installation Poetry:**
* *Linux:*
```
curl -sSL https://install.python-poetry.org | python3 -
```
or install with pip:
```
pip install poetry
```
* *Windows:*
```
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```
* *Verify that Poetry is installed correctly:*
```
poetry --version
``` 

### **3. Creating and activate a virtual environment:**

Installs the dependencies defined in `pyproject.toml`:
```
poetry install
```
Finally, we activate the environment with :
```
poetry env activate
```
### **4. Create .env file:**
Create an `.env` file based on `.env.example` with your variables.

### **5. Run the notebooks:**
you have to run the notebooks in order to perform the eda, model training and export in PLK format.

* **01_eda.ipynb**
* **02_training.ipynb** 
* **03_model.ipynb**

### **6. Start Kafka services with Doker:**
1. First we raise the services with the following command:
```
docker compose up -d
```
![Capture docker up](/assets/docker_up.png)

2. We check the services with:
```
docker ps
```
![Capture docker ps](/assets/docker_ps.png)

### **7. Run the producer and consumer:**
1. First we run the producer:
```
poetry run python kafka/producer.py
```
![producer](/assets/salida_producer.png)

2. Then we run the consumer:
```
poetry run python kafka/consumer.py
```
![consumer](/assets/salida_consumer.png)

3. Check if the data was saved in the db:
In the producer's image we can see how it says that he sent 157 messages.
```
SELECT COUNT(*) FROM happines_data;
```
![mysql](/assets/mysql.png)

### **Demonstration video**
See the video in the following link: https://drive.google.com/drive/folders/1uhBrtENBddcwd1h5flnFHll4kjgTXQ7G?usp=drive_link

## **CONCLUSION**

The development of this project allowed the construction of a comprehensive solution ranging from data exploration and transformation to the implementation of a real-time prediction system through streaming. The choice of the regression model, particularly the Random Forest Regressor, was based on its ability to handle non-linear relationships, its resistance to over-fitting and its good performance with datasets that present some heterogeneity between years, as was the case with the global happiness data between 2015 and 2019.

During the exploratory analysis phase (EDA), the most relevant variables to explain the variation of the happiness score were identified, including GDP per capita, social support, life expectancy and perception of corruption. These characteristics were selected and standardized to feed the regression model, ensuring consistency across the different annual sources.

The model was trained using a 80% split for training and 20% for testing, and evaluated using metrics such as MSE, RMSE, MAE and R², obtaining results that reflect a good predictive capacity. This quantitative evaluation, together with the interpretation of the importance of the features, confirmed the suitability of the selected model compared to other alternatives considered during the process.

In addition, a real-time processing flow was implemented using Apache Kafka, where a producer sends the processed data to the topic, and a consumer receives it, applies the prediction model and stores the results (predictions and inputs) in a relational database. This architecture simulates a productive real-time analysis environment, demonstrating the applicability of the model beyond a static environment.

Finally, it highlights the use of modern tools such as Docker for service containerization, Poetry for dependency management, and the modular organization of the code, which facilitates the scalability and maintenance of the system. In summary, this project demonstrates how to combine data analysis techniques, machine learning and distributed systems to build a robust, automated and production-oriented predictive solution.

## **AUTHOR**
<table style="border-collapse: collapse; border: none;">
  <tr>
    <td align="center" width="150" style="border: none;">
      <a href="https://github.com/KevinMG1601">
        <img src="https://avatars.githubusercontent.com/u/143461336?v=4" width="100px" alt="Kevin Muñoz"/><br />
        <span style="color: black; font-weight: bold;">Kevin Muñoz</span>
      </a>
    </td>
    <td style="border: none; vertical-align: top;">
      Created by <b>Kevin Muñoz</b>. I would like to know your opinion about this project. You can write me by <a href="mailto:kevin.andres2636@gmail.com">email</a> or connect with me on <a href="https://www.linkedin.com/in/kevin-mu%C3%B1oz-231b80303/">LinkedIn</a>.
    </td>
  </tr>
</table>
