Instrucciones:

1. colocar las siguientes lineas que instalan las librerias necesarias para correr el programa
   - pip install sklearn
   - pip install pickle
   - pip install flask
   - pip install numpy
   - pip install pandas
   - pip install matplotlib
2. si van a crear otro proyecto diferente solo copien el codigo del archivo "proyecto3.py" y el codigo del archivo "proyecto3_pkl.py", el archivo "proyecto3.py" se encarga de generar la IA que es el archivo llamado
"modelo_entrenado.pkl" y va a ser diferente para cada proyecto porque dependiendo del archivo con la que se le entrene (osea el excel)
3. dentro de la misma carpeta donde estan los archivos "proyecto3.py" y "proyecto3_pkl.py" crear otra carpeta llamada "templates" y dentro el "index.html", para el caso de este proyecto tocaba
llenar un formulario y por eso tiene ese codigo, por lo que posiblemente allan casos que no sea necesario hacer un formulario, entonces ese codigo quedaria muy diferente a como esta en el index, si tambien es un formulario
solo es cambiar los nombres de las variables que esten ahi.
4. cuando tengan todo listo tienen que correr el archivo "proyecto3_pkl.py", porque si le dan en abrir el server live al index no les va a funcionar, entonces cuando corrar el archivo "proyecto3_pkl.py"
y todo les funciona bien debe aparecer el siguiente mensaje:


 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 279-022-806


ahi tienen que oprimir la tecla control y darle click donde dice "http://127.0.0.1:5000", con eso les va a abrir la pagina del index y asi si pueden llenar los datos necesarios para que la IA les de la informacion que quieran

y con eso mi querido amigo o amiga has creado a la proxima skynet

!!!!!!!!!!!!NOTA!!!!!!!!!!!!
importante el nombre de las etiquetas que le pongan en el archivo index.html, porque esas luego van a ser guardadas en la parte de JS, y de ahi al archivo de python, entonces traten de que sean iguales.
