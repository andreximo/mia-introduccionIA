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

### 1. Asistente virtual de voz

- **Performance:** Maximizar el número de respuestas atendidas correctamente, minimizar el tiempo de respuesta, manejo de errores, precisión de las respuestas.
- **Environment:** Considerando que el asistente es un altavoz, el evironment donde opera podría ser el interior de una casa con un número variable de personas dependiendo de la hora.
Este environment, podría clasificarse como: comlpetamente observable, episódico, determinístico, de agente único, dinámico y desconocido.
- **Actuators:** Como actuadores tendría el altavoz y una luz para indicar alguna advertencia visual.
- **Sensors:** Como sensores podría tener, un microfono, unjuego de botones para encendidido, subir y bajar volumen y uno para cerrar y abrir el micrófono.

**Comentario:** Razones por las que calsifique el environment de esta manera son:
- _Completamente observable:_ Considere que es completamente observable porque con el micrófono el asistente puede acceder a la solicitud del usuario en cualquier moemento del tiempo.
- _Episódico:_ Una vez que el asistente da una respuesta, no se espera que está afecte de alguna manera la siguiente instrucción.
- _Determinístico:_ Considere que era determinístico porque el siguente estado siempre será un usuario con una respuesta.
- _Single agent:_ Este asistente no busca modificar el performance de otro agente.
- _Dinámico:_ considere que mientras el asistente busca la mejor respuesta el usuario podría cancelar la solicitud y que además el asistente necesita estar sensando cuando el usuario le de una nueva instrucción.
- _Desconocido:_ porque no sabe que es los próximo que va a solicitar el usuario.

### 2. Robot aspirador doméstico

- **Performance:** 
- **Environment:** ...
- **Actuators:** ...
- **Sensors:** ...

### 3. Sistema de recomendación de streaming

- **Performance:** ...
- **Environment:** ...
- **Actuators:** ...
- **Sensors:** ...

### 4. Vehículo autónomo en ciudad

- **Performance:** ...
- **Environment:** ...
- **Actuators:** ...
- **Sensors:** ...

### 5. Agente de trading algorítmico en bolsa

- **Performance:** ...
- **Environment:** ...
- **Actuators:** ...
- **Sensors:** ...

### 6. Sistema de diagnóstico médico asistido por IA

- **Performance:** ...
- **Environment:** ...
- **Actuators:** ...
- **Sensors:** ...

### 7. Dron de inspección de infraestructura

- **Performance:** ...
- **Environment:** ...
- **Actuators:** ...
- **Sensors:** ...

### 8. Agente jugador de ajedrez

- **Performance:** ...
- **Environment:** ...
- **Actuators:** ...
- **Sensors:** ...

