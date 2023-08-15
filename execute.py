import pandas as pd
import uvicorn
from fastapi import FastAPI
from _utils import check_key_input, check_values_input
from aux_params import Constants, output_model

app = FastAPI(debug=True)


@app.post('/predict')
def deploy_model(request: dict):

    try:
        # check errores en los inputs (nombres de las variables, formatos, etc)
        check_key_input(features_names=list(request.keys()))
        check_values_input(request)

        df = pd.DataFrame(request)  # convertir a dataframe
        minor_class_prob = output_model(df=df)  # salida del modelo (probabilidades para la clase minoritaria)

        minor_class_fd = [1 if value >= Constants.THRESHOLD.value else 0 for value in minor_class_prob]
        output_dict = {'minor class: probability': minor_class_prob,
                       'minor class - final decision': minor_class_fd,
                       'Error': ''
                       }
    except Exception as e:
        output_dict = {
            'minor class: probability': None,
            'minor class - final decision': None,
            'Error': f"No es posible ejecutar el modelo - {e}'"
        }
    return output_dict


if __name__ == "__main__":
    uvicorn.run(app, port=8000)
