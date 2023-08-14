# Deploy Machine Learning model with FastAPI

This repo consist of a deployment a Machine Learning model using FastAPI (https://fastapi.tiangolo.com/) library by Sebastián Ramírez (https://github.com/tiangolo). 

A web application to show the project structure for a deep learning model deployed using shiny has been developed.

The Machine Learning model was built using scikit-learn.

* Random Forest
* Min Max Scaler 

Each of these components are developed within the project in an offline setting inside `/model`. 
The scikit-learn model and Min-Max scaler process will still be needed in a production 
or testing setting in order to be able to predict user-submitted queries, 
so they can be serialized via python's pickle functionality and stored within the `/model` folder.


## Installation

Create a conda virtual environment in the project directory.

```
conda create -n venv python=3.9
```

Activate the virtual environment.
```
conda activate venv
```

While in the virtual environment, install required dependencies from `requirements.txt`.

```
pip install -r requirements.txt
```

Now we can deploy the web application via

```
uvicorn execute:app --reload
```

and navigate to `http://127.0.0.1:8000/predict` to see it live. 
I recommend the use of postman to check the correct operation of the api (https://www.postman.com/)

The application may then be terminated with the following commands.

```
ctrl - c
```

## Project Structure 

```
├── data
├── notebooks
├── model
│   ├── model.joblib
│   ├── calibrated_model.joblib
│   └── normalize.joblib
├── execute.py
├── basic_execute.py
├── _utils.py
├── aux_params.py
├── requirements.txt
└── README.md
```
