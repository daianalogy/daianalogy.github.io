My portfolio its also containerized on Docker and using a nginx server, just for practices purposes. 

Go to: <url>https://hub.docker.com/r/reithe/portafolio</url> Follow the instructions down bellow 

## English

Hi, thank you for taking the time to visit.

I will provide you with the necessary commands and concise instructions to view my portfolio without taking up much of your time.

I know your time is valuable, as is mine.

After pulling the image, the second step is to **run the container and remap the port** to the port number that you want or have available.

<pre><code>sudo docker run --rm -d -p [YOUR_PORT_HERE]:80 reithe/portafolio </pre></code>

Then, you can **view it in a browser by entering the address with the chosen port**

At this point, I hope to have made a good impression on you.

The last step would be to **stop the container (when it stops container automatically will be destroy) and delete the image** of my portfolio. I will also provide you with the commands for that.

**1. Stop and automatically delete container**

<pre><code>docker stop reithe/portafolio </pre></code>

**3. Delete image. (high-risk command, verify)**

<pre><code>docker rmi reithe/portafolio </pre></code>

## Español

Hola, gracias por tomarte el tiempo de visitar.

Aquí te dejaré los comandos que necesitas e instrucciones claras y concisas para visualizar mi portafolio sin la necesidad de quitarte mucho tiempo.

Sé que tu tiempo es importante, también el mio. 

Despues de jalar la imagen, el segundo paso es **correr el contenedor y remapear el puerto** al número de puerto que tú quieras o tengas disponible.

<pre><code>sudo docker run --rm -d -p  [TU_PUERTO_AQUI]:80 reithe/portafolio </pre></code>

Luego puedes **visualizar en un navegador, colocando la dirección con el puerto** elegido.

En este punto, espero haber logrado una buena impresión en ti.

El último paso sería, **detener el contenedor, destruirlo  y borrar la imagen de mi portafolio**, te dejaré los comandos para eso también.

**1. Detener y automaticamente borrar container**

<pre><code>docker stop reithe/portafolio </pre></code>

**2. Borrar la imagen (alto riesgo, verifica)**

<pre><code>docker rmi reithe/portafolio </pre></code>




