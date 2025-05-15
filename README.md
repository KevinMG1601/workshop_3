# ***Workshop 3: Machine learning and Data streaming 💻***

## **OVERVIEW**
This project aims to train a regression model to predict the happiness score of different countries using historical data distributed in five CSV files (2015.csv, 2016.csv, 2017.csv, 2018.csv, 2019.csv). The process involves scanning, cleaning, and unifying the data to build a robust model, followed by implementing real-time streaming using Apache Kafka to predict scores as new data is received. Finally, the results are stored in a database for further analysis and evaluation.

## **DATASETS**
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


## **PROJECT STRUCTURE**
| Folder / File | Description |
| ------------- |:-------------:|
| Assets        | |
| Data          | |
| Docs          | |
| Model         | |
| Notebooks     | |

## **INSTALLATION AND SETUP**

**1. Clone the repository:**
```
git clone https://github.com/KevinMG1601/workshop_3.git
```
**2. Installation Poetry:**
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

**3. Creating and activate a virtual environment:**

Installs the dependencies defined in `pyproject.toml`:
```
poetry install
```
Finally, we activate the environment with :
```
poetry env activate
```

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
