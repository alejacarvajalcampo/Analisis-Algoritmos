## 1584. Min Cost to Connect All Points

Autor: Josue Acosta Londono (`Josue`)

https://leetcode.com/problems/min-cost-to-connect-all-points/description/

Familia: grafos (árbol de recubrimiento mínimo)  
Idea: A diferencia de Dijkstra que busca caminos más cortos, aquí el objetivo es conectar a todos los nodos minimizando la suma total de la red (un Árbol de Recubrimiento Mínimo o MST)[cite: 4]. El grafo es completo (todos se pueden conectar) y el peso es la distancia Manhattan. Se optó por usar el algoritmo de Prim: se inicia en un punto arbitrario y, usando una cola de prioridad (min-heap), se hace crecer el árbol seleccionando iterativamente la arista más barata que conecte el árbol actual con un punto no visitado[cite: 4].  
Complejidad: Tiempo $O(n^2 \log n)$ implementado con un min-heap, donde n es `points.length`; como el grafo es denso y exploramos todas las conexiones posibles desde cada nodo hacia los demás, se insertan hasta $n^2$ aristas en el heap, y cada extracción cuesta $O(\log n^2) = O(\log n)$. Espacio $O(n^2)$ en el peor caso para mantener la frontera de aristas en la cola de prioridad.

![Accepted — Min Cost to Connect All Points](evidencias/min-cost-to-connect-all-points-accepted.png)