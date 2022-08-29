# OptimizacionHeuristica
Implementation of an evolutionary algorithm 2021

**1 Opciones de práctica**

Para esta práctica debemos desarrollar un algoritmo de optimización basado en la evolución diferencial.
Además durante la etapa de mutación usaremos la función current to rand, y durante la etapa de
recombinación haremos uso del binomial crossover.

**2 Estructura del algoritmo**

Para el desarrollo del algoritmo se han dividido las distintas clases en archivos separados de manera que al
modificar uno no se vean alterados el resto. En la clase Genome únicamente se ha implementado el 
constructor de la clase, ya que no era necesario nada más para la implementación del resto de elementos. En
la clase Population se han implementado a parte del constructor numerosos métodos para conocer la posición
de un Genoma dentro de la población, métodos para borrarlo, insertar nuevos genomas, u ordenar la
población, aunque la gran mayoría no han sido utilizados. Finalmente la clase EA incluye un método run
(int),que recibe el número de iteraciones que se desean realizar sobre una población inicial, y es sobre el que
se implementa el algoritmo. Además consta de un método best, que devuelve el genoma con mejor fitness
obtenido tras la última ejecución del método run.
Los operadores necesarios para la implementación del algoritmo se han creado a partir de una clase Operator,
la cual implementan.
Por último con el objetivo obtener ejemplos visuales de la ejecución del algoritmo se ha creado una clase
Tester que incluye métodos que nos permiten modificar los valores de las variables F (etapa de mutación) y
CR (etapa de recombinación), así como introducir varias funciones a optimizar en la misma ejecución. Estos
métodos devuelven una serie de gráficas que representan el proceso de optimización de las funciones
introducidas.
