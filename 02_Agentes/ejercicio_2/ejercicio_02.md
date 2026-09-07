# Descripción PEAS de agentes inteligentes

## Objetivo

Para cada una de las **8 aplicaciones** listadas abajo, redacta una descripción
PEAS completa y coherente. Debes pensar como diseñador del agente: qué optimiza,
dónde actúa, con qué puede mover o modificar el mundo, y qué puede observar.

## Aplicaciones a analizar

Describe PEAS para cada una de estas aplicaciones:

1. **Asistente virtual de voz** (p. ej. Siri, Alexa o Google Assistant en un altavoz inteligente).
2. **Robot aspirador doméstico** (p. ej. Roomba u otro robot que limpia pisos de un departamento).
3. **Sistema de recomendación de streaming** (p. ej. Netflix o Spotify que sugiere películas o canciones).
4. **Vehículo autónomo en ciudad** (conducción sin conductor en calles urbanas con tráfico y peatones).
5. **Agente de trading algorítmico en bolsa** (compra y venta automática de acciones en mercados financieros).
6. **Sistema de diagnóstico médico asistido por IA** (apoya a un médico a interpretar síntomas e imágenes clínicas).
7. **Dron de inspección de infraestructura** (revisa grietas, corrosión o fugas en puentes, tuberías o líneas eléctricas).
8. **Agente jugador de ajedrez** (programa que compite contra un humano u otro agente en partidas completas).

## Criterios de calidad

- **Performance:** incluye métricas concretas (precisión, tiempo, costo, satisfacción del usuario, ganancia, seguridad, etc.), no solo “hacerlo bien”.
- **Environment:** menciona si es parcialmente observable o totalmente observable, si es estocástico o determinista, episódico o secuencial, estático o dinámico, y discreto o continuo (según aplique).
- **Actuators:** lista acciones reales que el agente puede ejecutar, no capacidades vagas.
- **Sensors:** lista percepciones concretas (cámara, micrófono, API, historial de usuario, cotizaciones de mercado, etc.).

## Análisis

### 1. Asistente virtual de voz (ej. Siri, Alexa o Google Assistant en un altavoz inteligente)

- **Performance:** Maximizar el número de respuestas atendidas correctamente, minimizar el tiempo de respuesta, manejo de errores, precisión de las respuestas.
- **Environment:** Considerando que el asistente es un altavoz, el evironment donde opera podría ser el interior de una casa con un número variable de usuarios dependiendo de la hora. Este environment, podría clasificarse como: completamente observable, secuencial, determinístico, de agente único, dinámico y desconocido.
- **Actuators:** Como actuadores tendría el altavoz y una luz para indicar alguna advertencia visual.
- **Sensors:** Como sensores podría tener, un micrófono, un juego de botones para encendidido, subir y bajar volumen y uno para cerrar y abrir el micrófono.

**Comentario:** Razones por las que clasifiqué el environment de esa manera son:

- _Completamente observable:_ Considere que es completamente observable porque con el micrófono del asistente puede acceder a la solicitud del usuario en cualquier momento del tiempo. Y estoy considerando como estados: cuando el usuario hace una petición al asistente y cuando está en modo espera.
- _Secuencial:_ Una vez que el asistente da una respuesta, puede guardar el contexto para una instrucción subsecuente.
- _Determinístico:_ Considere que era determinístico, porque el siguiente estado siempre será un usuario con una respuesta (exitosa o no exitosa) o un estado en espera, lo cual se puede determinar desde el estado actual.
- _Single agent:_ Este asistente no busca modificar el performance de otro agente.
- _Dinámico:_ consideré que mientras el asistente busca la mejor respuesta el usuario podría cancelar la solicitud o solicitar que realice una nueva instrucción por lo que agente debe estar constantemente censando el entorno.
- _Desconocido:_ porque no sabe que es lo próximo que va a solicitar el usuario.

### 2. Robot aspirador doméstico

- **Performance:** Tiempo que está limpia un área, minimizar el consumo de energía, minimizar el ruido.
- **Environment:** Dado que es un aspirador doméstico, el environment donde el agente realiza su actividad puede ser una sección de la casa. Y estaría en un entorno parcialmente observable, multiagente, no determinístico, secuencial, dinámico y continuo.
- **Actuators:** ruedas para moverse, aspiradora
- **Sensors:** sensor de suciedad, temporizador, sensor de proximidad.

**Comentario:** Razones por las que clasifiqué el environment de esa manera son:

- _Parcialmente observable:_ Porque el sensor de suciedad no puede detectar cuando hay suciedad en cualquier lugar de esa área y tiene que desplazarse y realizar un escaneo.
- _Multiagente:_ Consideré que las personas que ensucian, minimizan el tiempo en que un área está limpia lo que altera el performance del agente.
- _No determinístico:_ Porque el agente no puede preveer cuando se ensuciará el área que debe mantener limpia
- _Secuencial:_ Una vez que el agente termina de limpiar una sección, continua a la siguiente para no quedar en atrapado en un bucle.
- _Dinámico:_ El área puede volver a ensuciarse mientras el agente está limpiando, por lo que el entorno cambia a pesar las decisiones que haya tomado.
- _Continuo:_ Porque se está considerando como una métrica de performance el tiempo en que un área está limpia, lo que implica que se continuamente se está censando el área a limpiar.


### 3. Sistema de recomendación de streaming (ej. Netflix o spotify)

- **Performance:** Número de películas o canciones reproducidas de la sección de sugerencias, categorías sugeridas acorde a las preferencias del usuario.
- **Environment:** Es la plataforma de reproducción, puede ser un portal web, una App móvil o una App para TV. Este entorno puede ser parcialmente observable, agente único, estocástico, secuencial, dinámico y discreto.
- **Actuators:** Listado de películas o canciones recomendadas.
- **Sensors:** Historial de reproducción, usuario logeado, búsquedas recientes.

**Comentario:** Razones por las que clasifiqué el environment de esa manera son:

- _Parcialmente observable:_ es parcialmente observable porque el agente no puede saber si el usuario está solo o con compañía, su estado de ánimo o simplemente dejo su cuenta abierta y otra persona está interactuando con la plataforma.
- _Single agent:_ Aunque el usuario puede utilizar el buscador, se considera como parte de los sensores del agente y este no compite contra este.
- _Estocástico:_ Considere que es estocástico porque el listado de sugerencias puede tener un 99% de afinidad con los gustos del usuario, no tenemos la certeza de si hara no clic en la sugerencia.
- _Secuencial:_ Porque cada vez que el usuario reproduce una película o canción, esta se considera como parte del contexto para la próxima sugerencia y evita que se le sugiera reproducir algo que ya vio o escucho.
- _Dinámico:_ es dinámico porque el repertorio de películas o canciones está en constante actualización lo que puede afectar el listado de sugerencias.
- _Discreto:_ Lo considero discreto porque se podría hacer una actualización del listado de recomendaciones después de cada evento si importar si el usuario pasa mucho tiempo conectado a la plataforma.

### 4. Vehículo autónomo en ciudad

- **Performance:** Para este agente se pueden considerar si llega a su destino, el confort del pasajero, el consumo de combustible o energía por la distancia recorrida, el número de accidentes y el tiempo en que llega a su destino.
- **Environment:** El environment donde se desenvuelve el agente son las calles y avenidas de una ciudad, donde interactúa con otros carros, semáforos, baches, peatones, animales y objetos estáticos. Por lo que se podría considerar como un entorno parcialmente observable, multiagente, estocástico, secuencial, dinámico y continuo.
- **Actuators:** Acelerador, freno, volante, direccionales, faros, claxon y altavoz.
- **Sensors:** Micrófono, pantalla táctil, cámaras, radares, GPS, acelerómetro, medidor de combustible o energía.

**Comentario:** Razones por las que clasifiqué el environment de esa manera son:

- _Parcialmente observable:_ Porque el agente no puede saber lo que van a hacer otros conductores, peatones o cosas en  movimiento.
- _Multiagente_ Considere que es multiagente, porque aunque no se sabe lo que van a hacer los demás, podemos considerar que tampoco buscan tener un accidente por lo que podrían colaborar para evitarlos.
- _Estocástico:_ El agente debe trabajar con la probabilidad de colisionar con los demás elementos del entorno.
- _Secuencial:_ Es secuencial porque debe mantener el estado en el que se encuentra para poder ejecutar una acción que le llevara a un nuevo estado, por ejemplo si está en movimiento no podrá ejecutar la acción de abrir la puerta, primero deberá estacionarse.
- _Dinámico:_ Como el vehículo autónomo está en constante movimiento, debe estar censando el entorno para poder y preguntarse que quiere hacer.
- _Continuo:_ Es continuo porque la cantidad de estados podría ser infinita, ya que este depende de la posición y la velocidad. 

### 5. Agente de trading algorítmico en bolsa

- **Performance:** Como medida de desempeño se puede considerar la maximización de utilidades por compra y venta de acciones.
- **Environment:** El agente podría trabajar sobre una plataforma de la bolsa de valores en un portal web. Y se podría considerar su environment como: completamente observable, multiagente, estocástico, secuencial, dinámico y continuo. 
- **Actuators:** Compra y venta de acciones.
- **Sensors:** Listado de empresas que cotizan en la bolsa, precio de la acción, volumen de compra o venta, sensor de noticias recientes, portafolio de acciones y capital disponible.

**Comentario:** Razones por las que clasifiqué el environment de esa manera son:

- _Completamente observable:_ Es completamente observable porque en el mometo en que el agente tome una decisión este conoce el precio de todas las empresas listadas en la bolsa.
- _Multiagente:_ Se considera multiagente porque los otros traders compiten activamente para maximizar sus ganancias.
- _Estocástico:_ Porque el agente trabaja con probabilidades para poder realizar la compra o venta de acciones.
- _Secuencia:_ Es secuencial porque la compra o venta de acciones afecta directamente la siguiente acción de compra.
- _Dinámico:_ Porque al subir o bajar el precio de las acciones la medida de desempeño cambia aunque el agente no haya realizado ninguna acción.
- _Continuo:_ Considere que fuera continuo porque el precio de las acciones no trabajan sobre rangos para subir y bajar, si no que el precio fluctúa de manera continua.

### 6. Sistema de diagnóstico médico asistido por IA (apoya a un médico a interpretar síntomas e imágenes clínicas)

- **Performance:** Como medida de desempeño podríamos considerar el número de diagnósticos correctos.
- **Environment:** Este agente puede trabajar en un environment con la información de un hospital, ya sea a través de servicios de información, bases de datos o una plataforma web. Y se puede considerar que su environment es: parcialmente observable, agente único, estocástico, secuencial, dinámico y discreto.
- **Actuators:** Display con el resultado del diagnóstico.
- **Sensors:** Servicios para consulta de historial médico, imágenes, temporalidad, padecimientos comunes y resultados de análisis.

**Comentario:** Razones por las que clasifiqué el environment de esa manera son:

- _Parcialmente observable:_ Es parcialmente observable porque el agente no puede conocer con exactitud el estado actual del paciente.
- _Single agent:_ El agente recaba la información para realizar el diagnóstico del paciente y no compite con el médico.
- _Estocástico:_ Porque el diagnostico debe indicar la probabilidad de padecimiento de alguna enfermedad y no puede fijar la postura determinista.
- _Episódico:_ Cuando el agente este realiza el diagnóstico de una paciente, este no debe afectar el diagnóstico de otro paciente. Pero en el caso de que ses el mismo paciente podría considerarse secuencial con el historial médico y últimos tratamientos.
- _Dinámico:_ Es dimánico porque el paciente puede presentar nuevos padecimientos, los cuales debe considerar el agente para hacer un nuevo diagnóstico.
- _Discreto:_ Considero que es discreto porque los resultados de análisis aunque pueden tomar valores numéricos continuos o el estado del paciente puede mejorara o empeorar, el asistente no está continuamente recibiendo información de sus síntomas o análisis.

### 7. Dron de inspección de infraestructura (revisa grietas, corrosión o fugas en puentes, tuberías o líneas eléctricas)

- **Performance:** Como medida de rendimiento se podría considerar el número de problemas detectados.
- **Environment:** El environment donde el agente desempeña su actividad puede acotarse a bienes inmuebles o grandes infraestructuras y el laboratorio de diagnóstico. Y puede clasificarse como: parcialmente observable, agente único, estocástico, secuencial, estático y continuo.
- **Actuators:** Sistema de vuelo y estabilidad. 
- **Sensors:** Cámara 4k, cámara termográfica, sensores para detección de objetos y obstáculos.

**Comentario:** Razones por las que clasifiqué el environment de esa manera son:

- _Parcialmente observable:_ Aunque se cuenta con los planos de los inmuebles, no es posible conocer el estado actual de todas las secciones de la infraestructura.
- _Single agent:_ Considere que es de agente único, porque no compite o colabora con otros agentes para maximizar su métrica de desempeño.
- _Estocástico:_ Es estocástico porque no tenemos la certeza de poder realizar la inspección sin obstáculos.
- _Secuencial:_ Es secuencial porque debe saber porque áreas ya realizo su recorrido y evitar volver a inspeccionarlas.
- _Estático:_ Considero que es estático porque no aparecerán nuevos problemas durante la misma inspección.
- _Continuo:_ Pienso que es un entorno continuo porque al igual que el vehículo autónomo, este también está en movimiento pero ahora con distintas coordenadas.

### 8. Agente jugador de ajedrez

- **Performance:** Para este agente se puede considerar el número de partidas ganadas, el número de movimientos.
- **Environment:** Su environment se limita al tablero de ajedrez. Y se puede considerar como: completamente observable, multiagente, determinístico, secuencial, estático, y discreto.
- **Actuators:** mover piezas del tablero.
- **Sensors:** las posiciones de las piezas en el tablero.

**Comentario:** Razones por las que clasifiqué el environment de esa manera son:

- _Completamente observable:_ Porque el agente puede conocer donde esta posicionada cada pieza en todo momento.
- _Multiagente:_ Es multiagente porque el contrincante intenta maximizar su rendimiento, mientras minimiza el del agente.
- _Determinístico:_ Debido a que el siguiente estado será determinado por la acción del agente sobre el estado actual y que el agente puede observar completamente el tablero podemos establecer que en entorno es determinístico.
- _Secuencial:_ El agente deberá tener en cuenta la secuencia de acciones que le llevaran a ganar la partida.
- _Estático:_ Considerando que no hay penalizaciones por tiempo, el puntaje del agente no cambia con el paso del tiempo.
- _Discreto:_ Es discreto porque tanto el tablero y las posiciones de las piezas tienen valores determinados y contables.

